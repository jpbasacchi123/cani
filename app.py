import html
import os
import re
from datetime import datetime, timezone

import httpx
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
from streamlit_javascript import st_javascript
from supabase import create_client

from diet_rules import DIETS

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

st.set_page_config(page_title="Can I?", page_icon="🥦", layout="centered")

st.markdown("""
<style>
    .main .block-container {
        max-width: 480px;
        margin: 0 auto;
        padding: 1.5rem 1rem 2rem;
    }
    /* Welcome */
    .welcome-hero {
        text-align: center;
        padding: 3rem 0 2rem;
    }
    .welcome-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #1a6b2f;
        line-height: 1.1;
        margin-bottom: 0.6rem;
    }
    .welcome-sub {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2.5rem;
    }
    /* Diet setup cards */
    .diet-card-desc {
        font-size: 0.84rem;
        color: #555;
        line-height: 1.5;
        margin-top: 0.1rem;
    }
    /* Scanner greeting */
    .scanner-greeting {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1a6b2f;
        line-height: 2;
    }
    /* Result banners */
    .banner {
        border-radius: 12px;
        padding: 1rem 1.5rem;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1.25rem;
    }
    .banner-green  { background: #d4edda; color: #155724; }
    .banner-yellow { background: #fff3cd; color: #856404; }
    .banner-red    { background: #f8d7da; color: #721c24; }
    /* Result diet cards */
    .diet-card {
        border-radius: 10px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        line-height: 1.8;
    }
    .card-green  { background: #d4edda; border-left: 4px solid #28a745; }
    .card-yellow { background: #fff3cd; border-left: 4px solid #ffc107; }
    .card-red    { background: #f8d7da; border-left: 4px solid #dc3545; }
    .pill {
        display: inline-block;
        background: rgba(0,0,0,0.12);
        border-radius: 20px;
        padding: 1px 9px;
        margin: 2px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .ingredients-box {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        font-size: 0.82rem;
        color: #555;
        margin-top: 0.75rem;
        line-height: 1.6;
        word-break: break-word;
    }
    /* Green primary buttons */
    div.stButton > button[kind="primary"] {
        background-color: #1a6b2f !important;
        border-color: #1a6b2f !important;
        color: white !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #145524 !important;
        border-color: #145524 !important;
    }
    div.stButton > button {
        border-radius: 10px !important;
        font-size: 1rem !important;
        min-height: 48px !important;
    }
    /* "Change My Diets" looks like a muted link */
    div[data-testid="column"] div.stButton > button[kind="secondary"] {
        background: transparent !important;
        border: none !important;
        color: #888 !important;
        font-size: 0.82rem !important;
        min-height: unset !important;
        padding: 0.25rem 0.5rem !important;
        text-decoration: underline;
    }
    /* Active diet tags on scanner screen */
    .diet-tags-wrap {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin: 0.4rem 0 1.1rem;
    }
    .diet-tag {
        display: inline-block;
        background: #e8f5ec;
        color: #1a6b2f;
        border: 1.5px solid #b2d9bc;
        border-radius: 20px;
        padding: 3px 10px;
        font-size: 0.78rem;
        font-weight: 600;
        white-space: nowrap;
    }
</style>
""", unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────────────────
for _k, _v in [
    ("screen", "welcome"),
    ("selected_diets", []),
    ("user", None),
    ("auth_error", ""),
    ("access_token", None),
    ("refresh_token", None),
    ("scanned_barcode", ""),
    ("auto_search", False),
    ("_ls_checked", False),
    ("_tokens_persisted", False),
    ("_clear_ls", False),
]:
    if _k not in st.session_state:
        st.session_state[_k] = _v

# Restore the auth session on every rerun so the supabase client stays
# authenticated and RLS policies see the correct user JWT.
if st.session_state.access_token:
    try:
        supabase.auth.set_session(
            st.session_state.access_token,
            st.session_state.refresh_token or "",
        )
    except Exception:
        pass

# ── Diet definitions for setup screen (all 20 diets) ─────────────────────────
SETUP_DIETS = [
    ("gluten_free",        "🌾", "Gluten-Free",
     "Avoids wheat, barley, and rye. Good if you have gluten sensitivity or intolerance."),
    ("celiac",             "⚕️", "Celiac",
     "Stricter than gluten-free. Also flags oats due to cross-contamination risk."),
    ("dairy_free",         "🥛", "Dairy-Free",
     "No milk, cheese, butter, or dairy proteins like whey and casein."),
    ("lactose_free",       "🧈", "Lactose Free",
     "Avoids lactose (milk sugar) found in milk, cream, soft cheeses, and whey."),
    ("vegan",              "🌱", "Vegan",
     "No animal products including meat, fish, dairy, eggs, honey, or gelatin."),
    ("keto",               "🥑", "Keto",
     "Avoids sugars, grains, starchy vegetables, and high-carb ingredients."),
    ("atkins",             "💪", "Atkins",
     "Very low-carb, high-protein approach. Eliminates all sugar, grains, starchy veg, and legumes."),
    ("eubiotic",           "🦠", "Eubiotic",
     "Avoids artificial sweeteners, preservatives, and emulsifiers that disrupt gut bacteria."),
    ("anti_inflammatory",  "🔥", "Anti-Inflammatory",
     "Cuts trans fats, inflammatory seed oils, refined sugar, processed meats, and artificial additives."),
    ("low_fodmap",         "🫁", "Low FODMAP",
     "Avoids fermentable carbs that cause gas and bloating. Cuts garlic, onion, legumes, and sugar alcohols."),
    ("sibo",               "🧫", "SIBO",
     "Avoids fermentable fibres and sugars that feed bacterial overgrowth in the small intestine."),
    ("crohns",             "🩹", "Crohn's Disease",
     "Avoids high-fibre, spicy, and gas-producing foods that can irritate an inflamed gut."),
    ("soy_free",           "🫘", "Soy Free",
     "No soy or soya products — including tofu, miso, soy sauce, soy lecithin, and soy oils."),
    ("nut_free",           "🌰", "Nut Free",
     "No tree nuts, peanuts, or coconut. Covers nut milks, oils, flours, and butters."),
    ("refined_sugar_free", "🍬", "Refined Sugar Free",
     "Cuts all refined and processed sugars — white sugar, corn syrup, molasses, and most syrups."),
    ("low_histamine",      "🤧", "Low Histamine",
     "Avoids fermented, aged, and smoked foods high in histamine. Ideal for histamine intolerance."),
    ("lectin_free",        "🌰", "Lectin Free",
     "Avoids high-lectin foods like grains, legumes, nightshades, and certain seeds and oils."),
    ("low_cholesterol",    "❤️", "Low Cholesterol",
     "Limits saturated fat, egg yolks, organ meats, and full-fat dairy that raise LDL cholesterol."),
    ("diabetic",           "🩸", "Diabetic",
     "Avoids high-glycaemic sugars, refined flours, and rapidly-digested starches that spike blood sugar."),
    ("alkaline",           "⚡", "Alkaline Diet",
     "Avoids acid-forming foods like meat, dairy, refined grains, and sugar. Prioritises plant foods."),
]
SETUP_DIETS.sort(key=lambda d: d[2])

# ── Helpers ───────────────────────────────────────────────────────────────────
def _friendly_error(e):
    msg = str(e).lower()
    if "invalid login" in msg or "invalid credentials" in msg or "email not confirmed" in msg:
        return "Incorrect email or password. Please try again."
    if "already registered" in msg or "user already exists" in msg:
        return "An account with this email already exists. Try signing in."
    if "password" in msg and ("weak" in msg or "short" in msg):
        return "Password is too weak. Use at least 6 characters."
    if "rate limit" in msg:
        return "Too many attempts. Please wait a moment and try again."
    return f"Something went wrong: {str(e)}"


def _load_user_diets():
    """Fetch saved diets from Supabase for the current user. Returns list or []."""
    try:
        result = (
            supabase.table("user_diets")
            .select("selected_diets")
            .eq("user_id", str(st.session_state.user.id))
            .limit(1)
            .execute()
        )
        if result.data:
            return result.data[0].get("selected_diets") or []
        return []
    except Exception:
        return []


def _save_scan_history(barcode, product_name, ingredients, result):
    if not st.session_state.user:
        return
    try:
        supabase.table("scan_history").insert({
            "user_id":      str(st.session_state.user.id),
            "barcode":      barcode,
            "product_name": product_name or "",
            "ingredients":  ingredients,
            "scanned_at":   datetime.now(timezone.utc).isoformat(),
            "result":       result,
        }).execute()
    except Exception:
        pass


def _after_login():
    """Route after successful auth: scanner if diets saved, otherwise diet setup."""
    diets = _load_user_diets()
    if diets:
        st.session_state.selected_diets = diets
        go("scanner")
    else:
        go("diet_setup")


def go(screen):
    st.session_state.screen = screen
    st.rerun()


_OFF_ENDPOINTS = [
    "https://world.openfoodfacts.org/api/v0/product/{code}.json",
    "https://ca.openfoodfacts.org/api/v0/product/{code}.json",
    "https://us.openfoodfacts.org/api/v0/product/{code}.json",
    "https://uk.openfoodfacts.org/api/v0/product/{code}.json",
    "https://world.openbeautyfacts.org/api/v0/product/{code}.json",
    "https://world.openpetfoodfacts.org/api/v0/product/{code}.json",
]

def fetch_product(code):
    first_found = None
    for url_tmpl in _OFF_ENDPOINTS:
        try:
            r = httpx.get(url_tmpl.format(code=code), timeout=10,
                headers={"User-Agent": "CanIApp/1.0 (contact@cani.app)"})
            r.raise_for_status()
            data = r.json()
            if data.get("status") != 1:
                continue
            product = data.get("product", {})
            has_ingredients = bool(
                (product.get("ingredients_text") or "").strip()
                or (product.get("ingredients_text_en") or "").strip()
            )
            if has_ingredients:
                return data
            if first_found is None:
                first_found = data
        except Exception:
            continue

    # Fallback: Open Food Repo (Swiss database, good for international products)
    try:
        r = httpx.get(
            f"https://www.foodrepo.org/api/v3/products?barcodes={code}",
            timeout=10,
            headers={"User-Agent": "CanIApp/1.0 (contact@cani.app)"},
        )
        r.raise_for_status()
        repo_data = r.json()
        items = repo_data.get("data") or []
        if items:
            item = items[0]
            ingredients_en = (
                (item.get("ingredients_texts") or {}).get("en") or ""
            ).strip()
            product_name = (item.get("name_translations") or {}).get("en") or item.get("name") or ""
            if ingredients_en or first_found is None:
                return {
                    "status": 1,
                    "product": {
                        "product_name": product_name,
                        "ingredients_text": ingredients_en,
                        "ingredients_text_en": ingredients_en,
                    },
                }
    except Exception:
        pass

    # Fallback: Go-UPC
    try:
        r = httpx.get(
            f"https://go-upc.com/api/v1/code/{code}",
            headers={"Authorization": f"Bearer {os.getenv('GO_UPC_KEY')}"},
            timeout=10,
        )
        data = r.json()
        product = data.get("product", {})
        ingredients = product.get("ingredients", "")
        name = product.get("name", "Unknown Product")
        if ingredients:
            return {
                "status": 1,
                "product": {
                    "product_name": name,
                    "ingredients_text": ingredients,
                    "ingredients_text_en": ingredients,
                    "ingredients": [],
                },
            }
    except Exception:
        pass

    # Fallback: UPC Item DB (100 free lookups/day, no key needed)
    try:
        r = httpx.get(
            f"https://api.upcitemdb.com/prod/trial/lookup?upc={code}",
            timeout=10,
            headers={"User-Agent": "CanIApp/1.0"},
        )
        data = r.json()
        items = data.get("items", [])
        if items:
            item = items[0]
            ingredients = item.get("ingredients", "")
            name = item.get("title", "Unknown Product")
            if ingredients:
                return {
                    "status": 1,
                    "product": {
                        "product_name": name,
                        "ingredients_text": ingredients,
                        "ingredients_text_en": ingredients,
                        "ingredients": [],
                    },
                }
    except Exception:
        pass

    return first_found


def split_ingredients(text):
    pattern = r'(?:may contain|traces? of|could contain|produced in a|manufactured in|made in a facility|contains traces)'
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return text[:m.start()].strip().rstrip(".,;"), text[m.start():].strip()
    return text.strip(), ""


def find_hits(text, keywords):
    matched = [kw for kw in keywords
               if re.search(r'(?<!\w)' + re.escape(kw) + r'(?!\w|[\s-]+free)', text)]
    return [kw for kw in matched if not any(kw != other and kw in other for other in matched)]


def make_pills(hits):
    return " ".join(f'<span class="pill">{html.escape(h)}</span>' for h in hits)


# ── Barcode scanner component ─────────────────────────────────────────────────
SCANNER_HTML = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 60px; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: transparent; padding: 4px 0; }

  #scan-btn {
    width: 100%; padding: 14px 20px; font-size: 16px; font-weight: 600;
    border: none; border-radius: 10px; background: #1a6b2f; color: white;
    cursor: pointer;
  }
  #scan-btn:disabled { background: #bbb; cursor: default; }

  #reader-wrap { display: none; margin-top: 8px; }

  /* Contain and round the html5-qrcode viewfinder */
  #reader {
    border-radius: 12px;
    overflow: hidden;
    border: none !important;
  }
  /* Hide the library's own button/select dashboard */
  #reader__dashboard,
  #reader__dashboard_section,
  #reader__dashboard_section_swaplink,
  #reader__filescan_input { display: none !important; }

  #close-btn {
    display: none; width: 100%; padding: 10px; font-size: 15px; font-weight: 600;
    border: none; border-radius: 8px; background: #f8d7da; color: #721c24;
    cursor: pointer; margin-bottom: 8px;
  }
  #torch-btn {
    display: none; width: 100%; padding: 8px; font-size: 14px;
    border: 1.5px solid #ddd; border-radius: 8px;
    background: white; color: #555; cursor: pointer; margin-top: 6px;
  }
  #torch-btn.on { background: #fff8dc; font-weight: 700; border-color: #f0c040; }

  #status { text-align: center; padding: 8px 4px; font-size: 13px;
            color: #555; min-height: 24px; }
</style>
</head>
<body>

<button id="scan-btn" onclick="startScan()">📷 Scan Barcode</button>

<div id="reader-wrap">
  <button id="close-btn" onclick="stopScan()">✕ Close Camera</button>
  <div id="reader"></div>
  <button id="torch-btn" onclick="toggleTorch()">🔦 Torch</button>
</div>
<div id="status"></div>

<script src="https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js"></script>
<script>
  var scanBtn    = document.getElementById('scan-btn');
  var readerWrap = document.getElementById('reader-wrap');
  var closeBtn   = document.getElementById('close-btn');
  var torchBtn   = document.getElementById('torch-btn');
  var statusEl   = document.getElementById('status');
  var scanner      = null;
  var activeTrack  = null;
  var torchOn      = false;
  var detected     = false;
  var refocusTimer = null;

  function applyBestFocus() {
    if (!activeTrack) return;
    try {
      var modes = (activeTrack.getCapabilities() || {}).focusMode || [];
      if (modes.indexOf('continuous') !== -1) {
        activeTrack.applyConstraints({ advanced: [{ focusMode: 'continuous' }] }).catch(function(){});
      } else if (modes.indexOf('macro') !== -1) {
        activeTrack.applyConstraints({ advanced: [{ focusMode: 'macro' }] }).catch(function(){});
      } else if (modes.indexOf('single-shot') !== -1) {
        activeTrack.applyConstraints({ advanced: [{ focusMode: 'single-shot' }] }).catch(function(){});
      }
    } catch(e) {}
  }

  // ── Streamlit bridge (identical to previous) ──────────────────────────────
  (function setupBridge() {
    try {
      if (window.parent._bcBridgeReady) return;
      window.parent._bcBridgeReady = true;
      window.parent.addEventListener('message', function(e) {
        if (!e.data || e.data.type !== 'bc_scan') return;
        var val = e.data.value;
        var inp = window.parent.document.querySelector(
          'input[placeholder="e.g. 5449000000996"]'
        );
        if (!inp) return;
        var setter = Object.getOwnPropertyDescriptor(
          window.parent.HTMLInputElement.prototype, 'value'
        ).set;
        setter.call(inp, val);
        inp.dispatchEvent(new window.parent.Event('input',  { bubbles: true }));
        inp.dispatchEvent(new window.parent.Event('change', { bubbles: true }));
        inp.dispatchEvent(new window.parent.FocusEvent('blur', { bubbles: true }));
        setTimeout(function() {
          var btns = Array.from(window.parent.document.querySelectorAll('button'));
          var btn = btns.find(function(b) {
            return b.textContent.trim().indexOf('Check Ingredients') !== -1;
          });
          if (btn) btn.click();
        }, 600);
      });
    } catch(e) {}
  })();

  // ── Parent input visibility helpers ──────────────────────────────────────
  var _hidden = [];

  function _hideParentInputs() {
    _hidden = [];
    try {
      var pd = window.parent.document;
      // Barcode text input
      var inp = pd.querySelector('input[placeholder="e.g. 5449000000996"]');
      if (inp) {
        var c = inp.closest('[data-testid="stTextInput"]');
        if (c) { c.style.display = 'none'; _hidden.push(c); }
      }
      // "Or paste ingredients manually" label (stMarkdown containing that text)
      pd.querySelectorAll('[data-testid="stMarkdownContainer"]').forEach(function(el) {
        if (el.textContent.indexOf('paste ingredients') !== -1) {
          var p = el.parentElement;
          if (p) { p.style.display = 'none'; _hidden.push(p); }
        }
      });
      // Textarea
      var ta = pd.querySelector('textarea');
      if (ta) {
        var tc = ta.closest('[data-testid="stTextArea"]');
        if (tc) { tc.style.display = 'none'; _hidden.push(tc); }
      }
    } catch(e) {}
  }

  function _showParentInputs() {
    try {
      _hidden.forEach(function(el) { el.style.display = ''; });
      _hidden = [];
    } catch(e) {}
  }

  // ── Scanner controls ──────────────────────────────────────────────────────
  function startScan() {
    detected = false;
    scanBtn.style.display = 'none';
    statusEl.textContent  = 'Starting camera…';
    // Expand iframe first; wait 200 ms for Streamlit to resize before
    // html5-qrcode measures #reader (needs non-zero dimensions to initialise)
    setIframeHeight(420);
    setTimeout(function() {
      readerWrap.style.display = 'block';

    scanner = new Html5Qrcode('reader');
    scanner.start(
      { facingMode: 'environment' },
      { fps: 10, qrbox: { width: 250, height: 150 }, aspectRatio: 1.7 },
      function(decodedText) {
        if (!detected) { detected = true; onFound(decodedText); }
      },
      function() { /* per-frame misses — ignore */ }
    ).then(function() {
      closeBtn.style.display = 'block';
      statusEl.textContent = '📷 Center barcode in box · Tap to focus';
      _hideParentInputs();

      // Apply best available focus mode, start periodic refocus, detect torch
      setTimeout(function() {
        try {
          var vid = document.querySelector('#reader video');
          if (!vid || !vid.srcObject) return;
          var track = vid.srcObject.getVideoTracks()[0];
          activeTrack = track;
          applyBestFocus();
          // Periodic nudge: single-shot every 2.5 s keeps older Android AF from locking
          refocusTimer = setInterval(function() {
            if (!activeTrack || detected) { clearInterval(refocusTimer); refocusTimer = null; return; }
            activeTrack.applyConstraints({ advanced: [{ focusMode: 'single-shot' }] })
              .then(function() { setTimeout(applyBestFocus, 400); })
              .catch(function() {});
          }, 2500);
          if ((track.getCapabilities() || {}).torch) { torchBtn.style.display = 'inline-block'; }
        } catch(e) {}
      }, 800);

      // Tap-to-focus: immediate single-shot nudge then back to best mode
      document.getElementById('reader').addEventListener('click', function() {
        if (!activeTrack) return;
        activeTrack.applyConstraints({ advanced: [{ focusMode: 'single-shot' }] })
          .then(function() { return new Promise(function(r) { setTimeout(r, 400); }); })
          .then(applyBestFocus)
          .catch(function() {});
        statusEl.textContent = '🔍 Refocusing…';
        setTimeout(function() { statusEl.textContent = '📷 Center barcode in box · Tap to focus'; }, 1200);
      });

    }).catch(function(err) {
      readerWrap.style.display = 'none';
      scanBtn.style.display    = 'block';
      setIframeHeight(60);
      handleError(err);
    });
    }, 200); // end setTimeout — iframe has now had time to expand
  }

  function setIframeHeight(h) {
    document.documentElement.style.height = h + 'px';
    document.body.style.height = h + 'px';
    window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height: h }, '*');
  }
  setIframeHeight(60);

  function stopScan() {
    _showParentInputs();
    readerWrap.style.display = 'none';
    closeBtn.style.display   = 'none';
    torchBtn.style.display   = 'none';
    torchBtn.textContent     = '🔦 Torch';
    torchBtn.classList.remove('on');
    torchOn     = false;
    activeTrack = null;
    if (refocusTimer) { clearInterval(refocusTimer); refocusTimer = null; }
    scanBtn.style.display = 'block';
    scanBtn.disabled      = false;
    setIframeHeight(60);
    if (scanner) {
      scanner.stop().catch(function() {});
      scanner = null;
    }
  }

  function toggleTorch() {
    if (!activeTrack) return;
    torchOn = !torchOn;
    activeTrack.applyConstraints({ advanced: [{ torch: torchOn }] })
      .then(function() {
        torchBtn.textContent = torchOn ? '🔦 On' : '🔦 Torch';
        torchBtn.classList.toggle('on', torchOn);
      })
      .catch(function() {
        torchOn = false;
        statusEl.textContent = '⚠️ Torch not supported on this device.';
      });
  }

  function onFound(barcode) {
    stopScan();
    statusEl.textContent = '✅ ' + barcode;
    window.parent.postMessage({ type: 'bc_scan', value: barcode }, '*');
    setTimeout(function() {
      try {
        window.parent.location.replace('?barcode=' + encodeURIComponent(barcode));
      } catch(e) {}
    }, 700);
  }

  function handleError(err) {
    scanBtn.disabled = false;
    var msg;
    if (typeof err === 'string') {
      if (/permission|notallowed/i.test(err))
        msg = '⚠️ Camera permission denied. Check browser settings and try again.';
      else if (/notfound|devices/i.test(err))
        msg = '⚠️ No camera found on this device.';
      else
        msg = '⚠️ ' + err;
    } else {
      var n = (err && err.name) || '';
      if (n === 'NotAllowedError' || n === 'PermissionDeniedError')
        msg = '⚠️ Camera permission denied. Check browser settings and try again.';
      else if (n === 'NotFoundError' || n === 'DevicesNotFoundError')
        msg = '⚠️ No camera found on this device.';
      else if (n === 'NotSupportedError')
        msg = '⚠️ Camera not supported. Try Chrome or Safari.';
      else
        msg = '⚠️ ' + ((err && err.message) || 'Could not start camera.');
    }
    statusEl.textContent = msg;
  }
</script>
</body>
</html>"""


# ── Screen 1: Welcome / Auth ──────────────────────────────────────────────────
def show_welcome():
    st.markdown("""
<div class="welcome-hero">
  <div class="welcome-title">Can I? 🥦</div>
  <div class="welcome-sub">Find out if you can eat it — instantly</div>
</div>
""", unsafe_allow_html=True)

    if st.session_state.auth_error:
        st.error(st.session_state.auth_error)
        st.session_state.auth_error = ""

    tab_in, tab_up = st.tabs(["Sign In", "Create Account"])

    with tab_in:
        si_email    = st.text_input("Email",    key="si_email",    placeholder="you@example.com")
        si_password = st.text_input("Password", key="si_password", placeholder="Password",
                                    type="password")
        if st.button("Sign In", type="primary", use_container_width=True, key="btn_signin"):
            if not (si_email.strip() and si_password):
                st.warning("Please enter your email and password.")
            else:
                try:
                    res = supabase.auth.sign_in_with_password(
                        {"email": si_email.strip(), "password": si_password}
                    )
                    st.session_state.user = res.user
                    st.session_state.access_token  = res.session.access_token
                    st.session_state.refresh_token = res.session.refresh_token
                    _after_login()
                except Exception as e:
                    st.session_state.auth_error = _friendly_error(e)
                    st.rerun()

    with tab_up:
        su_email    = st.text_input("Email",            key="su_email",    placeholder="you@example.com")
        su_password = st.text_input("Password",         key="su_password", placeholder="At least 6 characters",
                                    type="password")
        su_confirm  = st.text_input("Confirm Password", key="su_confirm",  placeholder="Repeat password",
                                    type="password")
        if st.button("Create Account", type="primary", use_container_width=True, key="btn_signup"):
            if not (su_email.strip() and su_password and su_confirm):
                st.warning("Please fill in all fields.")
            elif su_password != su_confirm:
                st.warning("Passwords do not match.")
            else:
                try:
                    res = supabase.auth.sign_up(
                        {"email": su_email.strip(), "password": su_password}
                    )
                    st.session_state.user = res.user
                    if res.session:
                        st.session_state.access_token  = res.session.access_token
                        st.session_state.refresh_token = res.session.refresh_token
                    _after_login()
                except Exception as e:
                    st.session_state.auth_error = _friendly_error(e)
                    st.rerun()


# ── Screen 2: Diet Setup ───────────────────────────────────────────────────────
def show_diet_setup():
    st.markdown("## What's your diet?")
    st.caption("Select all that apply — we'll check every scan against your choices")
    st.markdown("")

    current = set(st.session_state.selected_diets)
    new_selection = []

    for diet_key, emoji, label, desc in SETUP_DIETS:
        checked = diet_key in current
        with st.container(border=True):
            col_cb, col_text = st.columns([1, 9])
            with col_cb:
                selected = st.checkbox(
                    "", key=f"cb_{diet_key}", value=checked,
                    label_visibility="collapsed",
                )
            with col_text:
                st.markdown(f"**{emoji} {label}**")
                st.markdown(
                    f'<div class="diet-card-desc">{desc}</div>',
                    unsafe_allow_html=True,
                )
        if selected:
            new_selection.append(diet_key)

    st.markdown("")
    if st.button("💚 Save & Start Scanning", type="primary", use_container_width=True):
        st.session_state.selected_diets = new_selection
        if st.session_state.user:
            try:
                supabase.table("user_diets").upsert({
                    "user_id": str(st.session_state.user.id),
                    "selected_diets": new_selection,
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                }).execute()
            except Exception as e:
                st.error(f"Could not save diets: {e}")
                st.stop()
        go("scanner")


# ── Screen 3: Scanner ─────────────────────────────────────────────────────────
def show_scanner():
    col_greet, col_hist, col_change, col_out = st.columns([3, 2, 2, 1])
    with col_greet:
        st.markdown('<div class="scanner-greeting">Ready to scan 👋</div>', unsafe_allow_html=True)
    with col_hist:
        if st.button("📋 History", key="btn_history"):
            go("history")
    with col_change:
        if st.button("⚙️ Diets", key="btn_change_diets"):
            go("diet_setup")
    with col_out:
        if st.button("🚪", key="btn_signout", help="Sign Out"):
            try:
                supabase.auth.sign_out()
            except Exception:
                pass
            st.session_state.user              = None
            st.session_state.selected_diets    = []
            st.session_state.screen            = "welcome"
            st.session_state.auth_error        = ""
            st.session_state.access_token      = None
            st.session_state.refresh_token     = None
            st.session_state["_tokens_persisted"] = False
            st.session_state["_ls_checked"]    = False
            st.session_state["_clear_ls"]      = True
            st.rerun()

    selected_keys = st.session_state.selected_diets

    # Load from Supabase if session diets are empty (e.g. after page refresh)
    if not selected_keys and st.session_state.user:
        diets = _load_user_diets()
        if diets:
            st.session_state.selected_diets = diets
            selected_keys = diets

    if not selected_keys:
        st.warning("Please set up your diets first.")
        if st.button("Set Up Diets →", type="primary"):
            go("diet_setup")
        return

    # Show active diet tags
    _diet_meta = {d[0]: (d[1], d[2]) for d in SETUP_DIETS}
    tags_html = "".join(
        f'<span class="diet-tag">{_diet_meta[k][0]} {_diet_meta[k][1]}</span>'
        for k in selected_keys if k in _diet_meta
    )
    st.markdown(f'<div class="diet-tags-wrap">{tags_html}</div>', unsafe_allow_html=True)

    # Pre-fill barcode from URL (camera scan bridge)
    prefilled_barcode = st.query_params.get("barcode", "")
    if prefilled_barcode and prefilled_barcode != st.session_state.get("_last_url_barcode"):
        st.session_state["_last_url_barcode"] = prefilled_barcode
        st.session_state["scanned_barcode"]   = prefilled_barcode
        st.session_state["barcode_input"]     = prefilled_barcode
        st.session_state["auto_search"]       = True

    auto_search = st.session_state.get("auto_search", False)
    if auto_search:
        st.session_state["auto_search"] = False

    components.html(SCANNER_HTML, height=None)
    if prefilled_barcode:
        st.caption(f"Last scan: `{prefilled_barcode}`")

    barcode = st.text_input(
        "Or enter barcode manually",
        key="barcode_input",
        placeholder="e.g. 5449000000996",
    )

    st.markdown("**Or paste ingredients manually**")
    manual_text = st.text_area(
        "Paste or type the ingredients list",
        key="manual_ingredients",
        placeholder="e.g. Water, Sugar, Wheat Flour, Palm Oil, Salt…",
        height=110,
        label_visibility="collapsed",
    )

    if st.button("🔍 Check Ingredients", type="primary", use_container_width=True) or auto_search:
        raw = ""
        name = None

        if barcode.strip():
            with st.spinner("Searching product databases…"):
                data = fetch_product(barcode.strip())

            if data:
                product = data["product"]
                name = product.get("product_name") or "Unknown Product"
                raw = product.get("ingredients_text") or product.get("ingredients_text_en") or ""
                if not raw.strip():
                    st.warning("Product found but no ingredients text available — try typing them below.")
                    raw = ""
            else:
                st.warning("Product not found — try typing the ingredients manually")

        if not raw.strip() and manual_text.strip():
            raw = manual_text.strip()
            name = None  # manual mode — no product name

        if not raw.strip():
            if not barcode.strip() and not manual_text.strip():
                st.warning("Please scan a barcode, enter one manually, or paste the ingredients.")
            st.stop()

        if name:
            st.subheader(f"📦 {html.escape(name)}")
        else:
            st.subheader("📝 Manual ingredients check")

        lowered = raw.lower()
        main_text, traces_text = split_ingredients(lowered)

        results = {}
        for key in selected_keys:
            kws = DIETS[key]["keywords"]
            main_hits = find_hits(main_text, kws)
            trace_hits = [kw for kw in find_hits(traces_text, kws) if kw not in main_hits]
            results[key] = {"main": main_hits, "traces": trace_hits}

        has_main   = any(r["main"]   for r in results.values())
        has_traces = any(r["traces"] for r in results.values())

        if barcode.strip() and raw.strip():
            _result_str = "violation" if has_main else ("traces" if has_traces else "safe")
            _save_scan_history(barcode.strip(), name, raw, _result_str)

        if has_main:
            st.markdown('<div class="banner banner-red">❌ Ingredient violation detected</div>',
                        unsafe_allow_html=True)
        elif has_traces:
            st.markdown('<div class="banner banner-yellow">⚠️ Possible traces — check label carefully</div>',
                        unsafe_allow_html=True)
        else:
            st.markdown('<div class="banner banner-green">✅ All clear for selected diets</div>',
                        unsafe_allow_html=True)

        for key in selected_keys:
            d = DIETS[key]
            r = results[key]
            if r["main"]:
                cls, icon, msg = "card-red", "❌", f"Contains: {make_pills(r['main'])}"
            elif r["traces"]:
                cls, icon, msg = "card-yellow", "⚠️", f"May contain traces: {make_pills(r['traces'])}"
            else:
                cls, icon, msg = "card-green", "✅", "No forbidden ingredients found"

            st.markdown(f"""<div class="diet-card {cls}">
  <strong>{icon} {d['emoji']} {html.escape(d['label'])}</strong><br>
  <span style="font-size:0.88rem">{msg}</span>
</div>""", unsafe_allow_html=True)

        st.markdown("**Full Ingredients:**")
        st.markdown(f'<div class="ingredients-box">{html.escape(raw)}</div>',
                    unsafe_allow_html=True)


# ── Screen 4: History ────────────────────────────────────────────────────────
def show_history():
    if st.button("← Back", key="btn_history_back"):
        go("scanner")

    st.markdown("## 📋 Scan History")

    if not st.session_state.user:
        st.warning("Please sign in to view history.")
        return

    try:
        res = (
            supabase.table("scan_history")
            .select("*")
            .eq("user_id", str(st.session_state.user.id))
            .order("scanned_at", desc=True)
            .limit(50)
            .execute()
        )
        items = res.data or []
    except Exception as e:
        st.error(f"Could not load history: {e}")
        return

    if not items:
        st.info("No scans yet. Start scanning to build your history!")
        return

    selected_keys = st.session_state.selected_diets or _load_user_diets()
    _diet_meta = {d[0]: (d[1], d[2]) for d in SETUP_DIETS}

    for item in items:
        result_val  = item.get("result", "")
        result_icon = "✅" if result_val == "safe" else ("⚠️" if result_val == "traces" else "❌")
        raw_dt      = item.get("scanned_at", "")
        try:
            dt       = datetime.fromisoformat(raw_dt.replace("Z", "+00:00"))
            date_str = dt.strftime("%b %d, %Y %I:%M %p")
        except Exception:
            date_str = raw_dt[:10] if raw_dt else "Unknown date"

        name        = item.get("product_name") or item.get("barcode") or "Unknown Product"
        ingredients = item.get("ingredients", "")

        with st.expander(f"{result_icon} {name} — {date_str}"):
            if ingredients and selected_keys:
                lowered = ingredients.lower()
                main_text, traces_text = split_ingredients(lowered)
                results = {}
                for key in selected_keys:
                    kws        = DIETS[key]["keywords"]
                    main_hits  = find_hits(main_text, kws)
                    trace_hits = [kw for kw in find_hits(traces_text, kws) if kw not in main_hits]
                    results[key] = {"main": main_hits, "traces": trace_hits}

                for key in selected_keys:
                    if key not in _diet_meta:
                        continue
                    d = DIETS[key]
                    r = results[key]
                    if r["main"]:
                        cls, icon, msg = "card-red",    "❌", f"Contains: {make_pills(r['main'])}"
                    elif r["traces"]:
                        cls, icon, msg = "card-yellow", "⚠️", f"May contain traces: {make_pills(r['traces'])}"
                    else:
                        cls, icon, msg = "card-green",  "✅", "No forbidden ingredients found"
                    st.markdown(f"""<div class="diet-card {cls}">
  <strong>{icon} {d['emoji']} {html.escape(d['label'])}</strong><br>
  <span style="font-size:0.88rem">{msg}</span>
</div>""", unsafe_allow_html=True)

                st.markdown("**Full Ingredients:**")
                st.markdown(f'<div class="ingredients-box">{html.escape(ingredients)}</div>',
                            unsafe_allow_html=True)
            elif ingredients:
                st.caption(ingredients[:300])
            else:
                st.caption("No ingredients recorded.")

    st.markdown("---")
    if st.button("🗑️ Clear History", key="btn_clear_history"):
        try:
            supabase.table("scan_history").delete().eq(
                "user_id", str(st.session_state.user.id)
            ).execute()
            st.success("History cleared.")
            st.rerun()
        except Exception as e:
            st.error(f"Could not clear history: {e}")


# ── Persistent login (localStorage bridge) ───────────────────────────────────
# 1. Sign-out requested: clear localStorage (deferred flag avoids rerun race)
if st.session_state.get("_clear_ls"):
    st.session_state["_clear_ls"] = False
    st_javascript(
        "localStorage.removeItem('cani_at');"
        "localStorage.removeItem('cani_rt');"
        "localStorage.removeItem('cani_lt');"
    )

# 2. Fresh login/signup: persist tokens to localStorage once per session
elif st.session_state.access_token and not st.session_state["_tokens_persisted"]:
    _at = st.session_state.access_token.replace("'", "\\'")
    _rt = (st.session_state.refresh_token or "").replace("'", "\\'")
    st_javascript(
        f"localStorage.setItem('cani_at','{_at}');"
        f"localStorage.setItem('cani_rt','{_rt}');"
        f"localStorage.setItem('cani_lt',Date.now().toString());"
    )
    st.session_state["_tokens_persisted"] = True

# 3. Page load with no active session: check localStorage for saved tokens
elif st.session_state.user is None and not st.session_state["_ls_checked"]:
    # JS returns '' if no token or token is older than 24 h, else the token string.
    # st_javascript returns 0 (int) on first render while the JS is still in flight.
    _ls_at = st_javascript(
        "(function(){"
        "var at=localStorage.getItem('cani_at'),"
        "lt=localStorage.getItem('cani_lt');"
        "if(!at||!lt)return '';"
        "if(Date.now()-parseInt(lt)>86400000){"
        "localStorage.removeItem('cani_at');"
        "localStorage.removeItem('cani_rt');"
        "localStorage.removeItem('cani_lt');"
        "return '';}"
        "return at;})()"
    )
    _ls_rt = st_javascript("localStorage.getItem('cani_rt')||''")
    if _ls_at == 0 or _ls_rt == 0:
        st.stop()  # JS not resolved yet — blank frame, rerun will follow
    else:
        st.session_state["_ls_checked"] = True
        if _ls_at:
            try:
                _resp = supabase.auth.set_session(_ls_at, _ls_rt or "")
                if _resp and _resp.user:
                    st.session_state.user             = _resp.user
                    st.session_state.access_token     = _ls_at
                    st.session_state.refresh_token    = _ls_rt
                    st.session_state["_tokens_persisted"] = True
                    _after_login()  # navigates and reruns
            except Exception:
                # Token expired or revoked — wipe localStorage
                st_javascript(
                    "localStorage.removeItem('cani_at');"
                    "localStorage.removeItem('cani_rt');"
                    "localStorage.removeItem('cani_lt');"
                )
                st.session_state.access_token  = None
                st.session_state.refresh_token = None

# ── Router ────────────────────────────────────────────────────────────────────
_screen = st.session_state.screen
if st.session_state.user is None:
    show_welcome()
elif _screen == "diet_setup":
    show_diet_setup()
elif _screen == "history":
    show_history()
else:
    show_scanner()

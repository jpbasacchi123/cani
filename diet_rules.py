DIETS = {
    # ── Existing diets ────────────────────────────────────────────────────────
    "gluten_free": {
        "label": "Gluten Free",
        "emoji": "🌾",
        "keywords": [
            "wheat starch", "wheat flour", "wheat bran", "wheat germ", "wheat germ oil",
            "wheat protein", "wheat dextrin", "wheat berry", "wheat berries",
            "hydrolyzed wheat protein", "hydrolysed wheat protein",
            "wheat extract", "vital wheat gluten", "wheat gluten", "wheat",
            "barley malt extract", "barley malt", "barley flour", "pearl barley",
            "malt extract", "malt vinegar", "malt flour", "malt syrup",
            "malted barley flour", "malted barley", "barley",
            "rye flour", "rye bread", "rye",
            "oat flour", "oat bran", "oat flakes", "rolled oats",
            "oatmeal", "oat extract", "oats",
            "spelt", "kamut", "triticale", "emmer", "einkorn",
            "farro", "freekeh", "bulgur", "durum", "semolina",
            "vital wheat gluten", "wheat gluten", "gluten",
            "couscous", "seitan", "panko", "breadcrumbs",
            "malt",
            "brewer's yeast", "brewers yeast",
        ],
    },

    "dairy_free": {
        "label": "Dairy Free",
        "emoji": "🥛",
        "keywords": [
            "whole milk powder", "skimmed milk powder", "semi-skimmed milk powder",
            "full cream milk powder", "milk powder",
            "dried whole milk", "dried skimmed milk", "dried milk",
            "milk protein concentrate", "milk protein isolate", "milk proteins",
            "milk solids", "milk serum", "milk fat", "milk sugar",
            "pasteurized milk", "homogenized milk", "UHT milk",
            "full cream milk", "full fat milk", "low fat milk",
            "semi-skimmed milk", "skimmed milk", "skim milk",
            "whole milk", "fresh milk", "condensed milk", "evaporated milk",
            "milk chocolate", "white chocolate", "milk",
            "anhydrous milk fat", "anhydrous butter fat",
            "butter oil", "butter fat", "butterfat",
            "clarified butter", "cultured butter",
            "buttermilk powder", "dried buttermilk", "buttermilk",
            "butter",
            "soured cream", "sour cream",
            "crème fraîche", "creme fraiche",
            "double cream", "whipping cream", "single cream",
            "clotted cream", "fresh cream", "thick cream", "heavy cream", "cream",
            "greek yogurt", "greek yoghurt", "yogurt", "yoghurt", "kefir", "skyr",
            "cream cheese", "cottage cheese", "ricotta", "mascarpone", "quark",
            "fromage frais", "fromage blanc",
            "mozzarella", "parmesan", "parmigiano", "pecorino", "grana padano",
            "gruyère", "gruyere", "emmental", "gouda", "edam", "cheddar",
            "brie", "camembert", "roquefort", "gorgonzola", "stilton",
            "feta", "halloumi", "paneer",
            "processed cheese", "cheese spread", "cheese powder", "cheese",
            "ghee",
            "whey protein isolate", "whey protein concentrate", "whey protein",
            "whey powder", "demineralized whey", "sweet whey", "acid whey",
            "whey permeate", "whey solids", "whey",
            "calcium caseinate", "sodium caseinate", "potassium caseinate",
            "magnesium caseinate", "ammonium caseinate", "caseinate", "casein",
            "lactose", "milk sugar", "lactulose",
            "lactalbumin", "beta-lactoglobulin", "lactoglobulin",
            "lactoferrin", "lactoperoxidase",
            "nougat", "dulce de leche", "rennet",
        ],
    },

    "celiac": {
        "label": "Celiac",
        "emoji": "🍞",
        "keywords": [
            "modified wheat starch", "wheat starch", "wheat flour",
            "wheat protein", "wheat bran", "wheat germ", "wheat dextrin",
            "hydrolyzed wheat protein", "hydrolysed wheat protein",
            "wheat extract", "vital wheat gluten", "wheat gluten", "wheat",
            "barley malt extract", "barley malt", "barley flour",
            "malt extract", "malt vinegar", "malt flour", "barley",
            "rye flour", "rye",
            "oat flour", "oat bran", "oat flakes", "rolled oats", "oatmeal", "oats",
            "spelt", "kamut", "triticale", "emmer", "einkorn",
            "farro", "freekeh", "bulgur", "durum", "semolina",
            "wheat gluten", "gluten",
            "couscous", "seitan", "panko", "breadcrumbs",
            "malt",
            "brewer's yeast", "brewers yeast",
        ],
    },

    "eubiotic": {
        "label": "Eubiotic",
        "emoji": "🦠",
        "keywords": [
            "sucralose", "aspartame", "acesulfame potassium", "acesulfame-k", "acesulfame",
            "saccharin", "sodium saccharin", "cyclamate", "neotame", "advantame",
            "maltitol syrup", "maltitol", "sorbitol", "xylitol", "erythritol",
            "mannitol", "isomalt", "lactitol", "polydextrose",
            "artificial flavour", "artificial flavor",
            "artificial flavouring", "artificial flavoring",
            "carrageenan", "polysorbate 80", "polysorbate 60", "polysorbate 65",
            "carboxymethylcellulose", "sodium carboxymethylcellulose", "methylcellulose",
            "sodium benzoate", "potassium benzoate", "calcium benzoate", "benzoic acid",
            "potassium sorbate", "sodium sorbate", "sorbic acid",
            "sodium nitrite", "sodium nitrate", "potassium nitrite", "potassium nitrate",
            "calcium propionate", "sodium propionate", "propionic acid",
            "sodium metabisulphite", "sodium metabisulfite",
            "sulphur dioxide", "sulfur dioxide", "sulphites", "sulfites",
            "BHA", "BHT", "TBHQ", "propyl gallate", "octyl gallate",
            "tartrazine", "quinoline yellow", "sunset yellow", "allura red",
            "carmoisine", "amaranth dye", "ponceau 4r", "ponceau",
            "erythrosine", "brilliant blue", "indigotine", "patent blue",
            "high fructose corn syrup",
            "partially hydrogenated", "hydrogenated vegetable oil",
        ],
    },

    "vegan": {
        "label": "Vegan",
        "emoji": "🌱",
        "keywords": [
            # Fish
            "sardines", "sardine", "pilchards", "pilchard",
            "anchovies", "anchovy",
            "tuna", "salmon", "cod", "haddock", "mackerel", "herring",
            "halibut", "plaice", "pollock", "pollack", "tilapia", "trout",
            "sea bass", "sea bream", "snapper", "grouper", "flounder", "turbot",
            "sprats", "sprat", "smelt", "whitebait", "eel", "catfish",
            "carp", "bream", "perch", "pike", "dace", "barramundi",
            "mahi mahi", "swordfish", "monkfish", "sole", "skate",
            "lemon sole", "oily fish", "white fish", "river fish",
            # Fish products
            "fish sauce", "fish stock", "fish broth", "fish extract",
            "fish oil", "fish meal", "fish powder", "fish paste",
            "fish gelatin", "fish gelatine",
            "caviar", "roe", "fish roe", "surimi",
            "cod liver oil", "seafood", "shellfish", "fish",
            # Crustaceans
            "prawns", "prawn", "shrimp", "shrimps",
            "crab", "lobster", "langoustine", "scampi", "crayfish",
            # Molluscs
            "clams", "clam", "oysters", "oyster", "oyster sauce",
            "mussels", "mussel", "scallops", "scallop",
            "cockles", "cockle", "whelk",
            "squid", "calamari", "cuttlefish", "cuttlefish ink", "squid ink",
            "octopus", "abalone",
            # Meat
            "beef", "veal", "ox", "oxtail",
            "pork", "ham", "bacon", "pancetta", "prosciutto", "guanciale",
            "lard", "salami", "pepperoni", "chorizo", "mortadella", "coppa",
            "chicken", "turkey", "duck", "goose", "quail", "pheasant",
            "partridge", "pigeon", "guinea fowl", "grouse",
            "lamb", "mutton", "venison", "rabbit", "hare",
            "bison", "buffalo", "wild boar", "boar",
            "horse", "horsemeat", "kangaroo", "ostrich",
            "sausage", "hot dog", "frankfurter", "meatballs",
            "offal", "liver", "kidney", "heart", "tripe", "tongue", "brain",
            "blood", "bone broth", "bone meal", "bone marrow",
            "meat extract", "meat stock", "meat broth",
            "meat", "poultry", "game",
            # Animal fats
            "tallow", "beef tallow", "suet", "beef suet",
            "dripping", "schmaltz", "animal fat", "rendered fat",
            # Dairy
            "whole milk powder", "milk powder", "milk solids",
            "skimmed milk", "whole milk", "condensed milk", "milk",
            "anhydrous milk fat", "butter fat", "butter oil", "butter",
            "buttermilk", "soured cream", "sour cream", "cream",
            "lactose", "casein", "calcium caseinate", "caseinate",
            "whey protein isolate", "whey protein concentrate", "whey protein", "whey",
            "cheese powder", "cheese", "milk chocolate", "white chocolate",
            "yogurt", "yoghurt", "ghee", "kefir",
            "lactalbumin", "lactoglobulin", "nougat",
            # Eggs
            "whole egg powder", "dried whole egg",
            "egg white powder", "dried egg white",
            "egg yolk powder", "dried egg yolk",
            "whole egg", "dried egg", "egg white", "egg yolk",
            "egg powder", "egg albumin",
            "egg", "eggs", "mayonnaise", "aioli", "hollandaise",
            "lysozyme",
            # Collagen / gelatin
            "hydrolyzed collagen", "hydrolysed collagen",
            "marine collagen", "collagen peptides", "collagen",
            "gelatin", "gelatine", "isinglass",
            # Insect-derived
            "carmine", "cochineal", "natural red 4", "crimson lake", "carminic acid",
            "shellac", "confectioners glaze", "confectionery glaze",
            # Bee products
            "honey", "beeswax", "royal jelly", "propolis", "bee pollen",
            # Other animal-derived
            "lanolin", "albumin", "blood albumin",
            "rennet", "animal rennet", "pepsin",
            "L-cysteine", "cysteine",
            "glucosamine", "chondroitin",
        ],
    },

    "keto": {
        "label": "Keto",
        "emoji": "🥩",
        "keywords": [
            "high fructose corn syrup", "high-fructose corn syrup",
            "glucose-fructose syrup", "glucose fructose syrup",
            "glucose syrup", "corn syrup", "golden syrup",
            "brown rice syrup", "rice syrup", "malt syrup",
            "maple syrup", "agave syrup", "agave nectar", "agave",
            "treacle", "black treacle", "molasses", "blackstrap molasses",
            "date syrup", "barley malt syrup",
            "invert sugar syrup", "invert sugar",
            "coconut sugar", "palm sugar", "jaggery", "panela",
            "cane sugar", "raw cane sugar", "beet sugar", "turbinado sugar",
            "demerara sugar", "muscovado sugar", "brown sugar",
            "caster sugar", "icing sugar", "powdered sugar",
            "white sugar", "granulated sugar", "sugar",
            "dextrose", "fructose", "sucrose", "glucose",
            "maltose", "lactose", "galactose", "honey",
            "modified tapioca starch", "modified potato starch",
            "modified corn starch", "modified wheat starch",
            "modified food starch", "modified starch",
            "tapioca starch", "potato starch", "corn starch", "cornstarch",
            "rice starch", "wheat starch", "arrowroot", "tapioca",
            "maltodextrin", "dextrin",
            "wheat flour", "rye flour", "oat flour", "rice flour",
            "corn flour", "barley flour", "buckwheat flour",
            "plain flour", "all-purpose flour", "self-raising flour",
            "bread flour", "breadcrumbs", "panko",
            "oats", "barley", "rye", "wheat",
            "corn", "maize", "millet", "sorghum",
            "bulgur", "couscous", "semolina",
            "brown rice", "white rice", "basmati rice", "jasmine rice", "rice",
            "pasta", "spaghetti", "macaroni", "penne", "fusilli",
            "lasagne", "lasagna", "gnocchi", "ravioli",
            "rice noodles", "egg noodles", "noodles",
            "chickpeas", "chick peas", "garbanzo",
            "lentils", "red lentils", "green lentils",
            "kidney beans", "black beans", "cannellini beans",
            "haricot beans", "navy beans", "pinto beans",
            "butter beans", "lima beans", "broad beans", "fava beans",
            "split peas", "edamame", "soya beans", "soybeans", "baked beans",
            "potato", "sweet potato", "yam", "cassava", "parsnip", "plantain",
            "raisins", "sultanas", "currants", "dates", "dried cranberries",
            "dried fruit", "fruit leather",
            "apple juice concentrate", "grape juice concentrate",
            "fruit juice concentrate", "fruit concentrate", "fruit juice",
        ],
    },

    # ── New diets ─────────────────────────────────────────────────────────────
    "low_fodmap": {
        "label": "Low FODMAP",
        "emoji": "🫁",
        "keywords": [
            # Fructans — major FODMAP trigger
            "garlic", "garlic powder", "garlic extract", "garlic oil", "roasted garlic",
            "onion", "onion powder", "onion extract", "onion flakes", "dried onion",
            "shallot", "shallots", "leek", "leek powder",
            "wheat", "rye", "barley",
            # GOS (galacto-oligosaccharides)
            "kidney beans", "black beans", "chickpeas", "chick peas",
            "lentils", "soybeans", "soya beans", "split peas",
            # Fructose excess
            "honey", "agave", "agave syrup",
            "high fructose corn syrup", "glucose-fructose syrup",
            "apple juice", "apple juice concentrate", "apple puree", "apple powder",
            "pear juice", "pear puree",
            "mango puree", "mango concentrate",
            # Polyols (sugar alcohols)
            "sorbitol", "mannitol", "xylitol", "maltitol",
            "isomalt", "lactitol", "erythritol",
            # Polyol-rich stone fruits (as ingredients)
            "peach", "nectarine", "plum", "cherry", "cherries", "apricot",
            # Lactose
            "lactose", "milk", "yogurt", "yoghurt", "kefir",
            "cream cheese", "ricotta", "cottage cheese", "mascarpone",
            "condensed milk", "evaporated milk", "milk powder",
            # High-FODMAP nuts
            "cashew", "cashews", "pistachio", "pistachios",
            # Prebiotic / fermentable fibers
            "inulin", "chicory root", "chicory root extract", "chicory inulin",
            "fructooligosaccharides", "fructo-oligosaccharides",
            "galactooligosaccharides", "galacto-oligosaccharides",
            # High-FODMAP vegetables (commonly in processed food)
            "asparagus", "cauliflower",
            "mushroom", "mushrooms", "dried mushroom",
            "beetroot", "beet",
        ],
    },

    "alkaline": {
        "label": "Alkaline Diet",
        "emoji": "⚡",
        "keywords": [
            # Animal proteins (strongly acid-forming)
            "beef", "pork", "chicken", "turkey", "lamb", "veal",
            "duck", "goose", "venison", "rabbit",
            "salmon", "tuna", "cod", "haddock", "sardine", "sardines",
            "mackerel", "herring", "fish",
            "sausage", "salami", "pepperoni", "chorizo", "hot dog", "bacon", "ham",
            "meat", "poultry",
            # Dairy (acid-forming)
            "milk", "cheese", "butter", "cream", "yogurt", "yoghurt",
            "whey", "casein", "lactose",
            # Eggs
            "egg", "eggs", "egg white", "egg yolk",
            # Refined carbohydrates
            "white flour", "refined flour", "wheat flour", "plain flour",
            "white rice", "refined rice",
            "white sugar", "cane sugar", "brown sugar", "sugar",
            "corn syrup", "high fructose corn syrup", "glucose syrup",
            "maltodextrin", "dextrose",
            # Highly processed / artificial
            "artificial flavour", "artificial flavor",
            "artificial colour", "artificial color",
            "sodium benzoate", "potassium sorbate",
            "BHA", "BHT",
            "partially hydrogenated", "hydrogenated vegetable oil",
            # Caffeine (acid-forming)
            "caffeine",
            # Alcohol
            "alcohol", "ethanol",
            # Phosphoric acid (soft drinks)
            "phosphoric acid",
        ],
    },

    "atkins": {
        "label": "Atkins",
        "emoji": "💪",
        "keywords": [
            # All sugars
            "high fructose corn syrup", "glucose syrup", "corn syrup", "golden syrup",
            "maple syrup", "agave syrup", "agave", "treacle", "molasses",
            "invert sugar syrup", "invert sugar",
            "coconut sugar", "cane sugar", "beet sugar", "brown sugar",
            "caster sugar", "icing sugar", "white sugar", "granulated sugar", "sugar",
            "dextrose", "fructose", "sucrose", "glucose", "maltose", "honey",
            # Starches
            "maltodextrin", "dextrin",
            "modified starch", "modified food starch",
            "tapioca starch", "potato starch", "corn starch", "wheat starch",
            "tapioca", "arrowroot",
            # Flours and grains
            "wheat flour", "oat flour", "rice flour", "corn flour", "rye flour",
            "plain flour", "all-purpose flour", "breadcrumbs",
            "oats", "wheat", "corn", "maize", "rice", "barley", "rye",
            "bulgur", "couscous", "semolina",
            # Pasta, bread, noodles
            "pasta", "noodles", "spaghetti", "macaroni", "penne", "lasagne",
            "gnocchi", "bread",
            # High-carb legumes
            "chickpeas", "lentils", "kidney beans", "black beans",
            "cannellini beans", "pinto beans", "butter beans",
            "soybeans", "split peas", "baked beans",
            # High-carb vegetables
            "potato", "sweet potato", "yam", "cassava", "parsnip",
            # Fruit juice and concentrates
            "fruit juice concentrate", "fruit concentrate", "fruit juice",
            "apple juice concentrate", "grape juice concentrate",
            # Dried fruit
            "raisins", "sultanas", "currants", "dates", "dried fruit",
        ],
    },

    "lactose_free": {
        "label": "Lactose Free",
        "emoji": "🧈",
        "keywords": [
            # Lactose itself
            "lactose", "milk sugar", "lactulose",
            # Liquid and fresh milk (high lactose)
            "whole milk", "full cream milk", "skimmed milk", "skim milk",
            "semi-skimmed milk", "fresh milk", "pasteurized milk",
            "condensed milk", "evaporated milk", "UHT milk", "milk",
            # Milk powders (contain lactose)
            "whole milk powder", "skimmed milk powder", "milk powder",
            "dried whole milk", "dried skimmed milk", "dried milk",
            "milk solids", "milk proteins",
            # Cream (lactose-containing)
            "double cream", "whipping cream", "single cream",
            "fresh cream", "soured cream", "sour cream",
            "crème fraîche", "creme fraiche", "cream",
            "buttermilk",
            # Soft / fresh cheeses (high lactose)
            "ricotta", "cottage cheese", "cream cheese",
            "mascarpone", "quark", "fromage frais",
            "brie", "camembert",
            # Fermented dairy (still contains some lactose)
            "yogurt", "yoghurt", "kefir", "skyr",
            # Milk chocolate / white chocolate
            "milk chocolate", "white chocolate",
            # Whey (contains lactose unless specifically hydrolyzed)
            "whey protein concentrate", "whey protein", "whey powder", "sweet whey",
            "acid whey", "whey permeate", "whey",
            # Milk proteins that indicate dairy origin
            "lactalbumin", "lactoglobulin",
        ],
    },

    "soy_free": {
        "label": "Soy Free",
        "emoji": "🫘",
        "keywords": [
            "soybeans", "soybean", "soya beans", "soya bean",
            "soya", "soy",
            "edamame",
            "tofu", "firm tofu", "silken tofu", "bean curd",
            "tempeh", "miso", "natto", "miso paste",
            "soy sauce", "soya sauce", "tamari", "shoyu",
            "teriyaki sauce", "hoisin sauce",
            "soy milk", "soya milk", "soy cream", "soy yogurt",
            "soy flour", "soya flour",
            "soy protein isolate", "soy protein concentrate", "soy protein",
            "soya protein", "isolated soy protein",
            "textured soy protein", "textured soya protein",
            "textured vegetable protein",
            "soy lecithin", "soya lecithin",
            "hydrolyzed soy protein", "hydrolysed soy protein",
            "soybean oil", "soya oil",
            "fermented soybean",
        ],
    },

    "nut_free": {
        "label": "Nut Free",
        "emoji": "🥜",
        "keywords": [
            # Almonds
            "almond flour", "almond meal", "almond milk", "almond butter",
            "almond paste", "almond extract", "almond oil", "ground almonds",
            "almonds", "almond",
            # Cashews
            "cashew butter", "cashew milk", "cashew cream", "cashew oil",
            "cashew nuts", "cashew nut", "cashews", "cashew",
            # Walnuts
            "walnut oil", "walnuts", "walnut",
            # Pecans
            "pecans", "pecan",
            # Pistachios
            "pistachios", "pistachio",
            # Macadamia
            "macadamia nuts", "macadamia nut", "macadamia", "macadamia oil",
            # Hazelnuts
            "hazelnut spread", "hazelnut paste", "hazelnut oil",
            "hazelnuts", "hazelnut", "filbert",
            # Brazil nuts
            "brazil nuts", "brazil nut",
            # Pine nuts
            "pine nuts", "pine nut", "pignoli",
            # Chestnuts
            "chestnuts", "chestnut",
            # Peanuts (legume but common allergen grouped with nuts)
            "peanut butter", "peanut oil", "peanut flour",
            "peanuts", "peanut", "groundnuts", "groundnut",
            "monkey nuts", "monkey nut", "arachis oil",
            # Coconut (FDA tree nut classification)
            "coconut cream", "coconut milk", "coconut oil",
            "coconut flour", "desiccated coconut", "coconut water",
            "coconut", "creamed coconut",
            # Nut-based products
            "marzipan", "praline", "nougat",
            "nut butter", "nut oil", "mixed nuts", "tree nuts", "nuts",
            "satay", "satay sauce",
        ],
    },

    "refined_sugar_free": {
        "label": "Refined Sugar Free",
        "emoji": "🍬",
        "keywords": [
            "high fructose corn syrup", "high-fructose corn syrup",
            "glucose-fructose syrup", "glucose fructose syrup",
            "glucose syrup", "corn syrup", "golden syrup",
            "brown rice syrup", "rice syrup",
            "invert sugar syrup", "invert sugar",
            "barley malt syrup", "malt syrup",
            "cane sugar", "raw cane sugar", "evaporated cane juice",
            "beet sugar", "turbinado sugar", "muscovado sugar",
            "demerara sugar", "soft brown sugar", "dark brown sugar",
            "brown sugar", "light brown sugar",
            "caster sugar", "icing sugar", "confectioners sugar",
            "powdered sugar", "white sugar", "granulated sugar",
            "crystal sugar", "refined sugar", "sugar",
            "dextrose", "sucrose", "maltose", "fructose",
            "maltodextrin", "dextrin",
            "treacle", "black treacle", "molasses",
            "maple syrup", "agave syrup", "agave nectar", "agave",
            "date syrup", "coconut sugar",
            "fruit juice concentrate", "apple juice concentrate",
            "grape juice concentrate", "fruit concentrate",
        ],
    },

    "lectin_free": {
        "label": "Lectin Free",
        "emoji": "🌰",
        "keywords": [
            # Grains (high lectin)
            "wheat", "wheat germ", "wheat bran", "wheat flour",
            "corn", "maize", "corn starch", "cornflour", "corn flour",
            "rice flour", "brown rice", "white rice", "rice",
            "oats", "oat flour", "barley", "rye",
            "quinoa", "millet", "sorghum", "buckwheat",
            # Legumes (very high lectin — especially raw/undercooked)
            "kidney beans", "red kidney beans",
            "black beans", "chickpeas", "chick peas",
            "lentils", "peanuts", "peanut",
            "soybeans", "soya beans", "edamame",
            "peas", "split peas", "broad beans", "fava beans",
            "cannellini beans", "haricot beans",
            "beans",
            # Nightshades (contain lectins and related compounds)
            "tomato paste", "tomato puree", "tomato powder",
            "tomato sauce", "tomato ketchup", "ketchup", "tomato",
            "potato", "potato starch", "potato flour",
            "eggplant", "aubergine",
            "bell pepper", "red pepper", "green pepper", "yellow pepper",
            "chili pepper", "chilli pepper", "chili powder", "chilli powder",
            "paprika", "cayenne pepper", "cayenne",
            "goji berries", "goji",
            # High-lectin seeds
            "sunflower seeds", "sunflower seed",
            "pumpkin seeds", "pumpkin seed",
            "chia seeds", "chia seed",
            "hemp seeds", "hemp seed",
            "sesame seeds", "sesame seed", "sesame",
            # High-lectin seed oils
            "sunflower oil", "soybean oil", "corn oil",
            "canola oil", "rapeseed oil", "cottonseed oil",
            "safflower oil", "peanut oil", "grapeseed oil",
            # Dairy (A1 casein)
            "milk", "casein", "skimmed milk", "whole milk", "milk powder",
        ],
    },

    "low_histamine": {
        "label": "Low Histamine",
        "emoji": "🤧",
        "keywords": [
            # Vinegar — all types trigger histamine
            "red wine vinegar", "white wine vinegar", "balsamic vinegar",
            "cider vinegar", "apple cider vinegar", "malt vinegar",
            "rice vinegar", "sherry vinegar", "vinegar",
            # Fermented vegetables
            "sauerkraut", "kimchi", "pickles", "pickled vegetables",
            "fermented vegetables",
            # Fermented beverages
            "kombucha",
            # Fermented soy and condiments
            "miso", "soy sauce", "tamari", "shoyu", "teriyaki sauce",
            "fish sauce", "worcestershire sauce",
            "tempeh", "natto",
            # Aged / fermented cheeses (very high histamine)
            "parmesan", "parmigiano", "pecorino", "grana padano",
            "gruyère", "gruyere", "emmental", "cheddar",
            "gouda", "roquefort", "gorgonzola", "stilton", "blue cheese",
            "brie", "camembert", "provolone",
            "processed cheese",
            # Fermented dairy
            "yogurt", "yoghurt", "kefir",
            "sour cream", "soured cream", "buttermilk",
            "cream cheese",
            # Cured / smoked meats (histamine forms during curing)
            "salami", "pepperoni", "chorizo", "nduja",
            "prosciutto", "serrano ham", "cured ham",
            "bacon", "smoked bacon",
            "hot dog", "frankfurter", "sausage",
            "smoked meat", "smoked salmon", "smoked fish",
            "anchovies", "anchovy",
            "sardines", "sardine",
            "tuna", "canned tuna",
            "mackerel", "herring",
            # Histamine-rich vegetables and fruits
            "tomato paste", "tomato puree", "tomato sauce", "ketchup", "tomato",
            "avocado", "avocado puree",
            "eggplant", "aubergine",
            "spinach",
            # Citrus — histamine liberators
            "lemon juice", "lemon zest", "lemon",
            "lime juice", "lime",
            "orange juice", "orange zest", "orange",
            "grapefruit juice", "grapefruit",
            "clementine", "mandarin", "tangerine",
            # Tropical fruits
            "pineapple juice", "pineapple",
            "papaya", "kiwi",
            "strawberries", "strawberry",
            "raspberries", "raspberry",
            # Cocoa and chocolate
            "dark chocolate", "milk chocolate", "white chocolate",
            "cocoa powder", "cocoa butter", "cocoa", "cacao",
            "chocolate",
            # Yeast extracts
            "yeast extract", "autolyzed yeast", "autolyzed yeast extract",
            "marmite", "vegemite", "nutritional yeast",
            "brewer's yeast", "brewers yeast",
            # Histamine-releasing nuts
            "peanuts", "peanut", "walnuts", "walnut",
            "cashew", "cashews",
            # Alcohol
            "wine", "beer", "spirits", "cider", "mead",
            "alcohol", "ethanol",
            # Preservatives (histamine liberators)
            "sodium benzoate", "potassium benzoate",
            "sodium nitrite", "sodium nitrate",
            "sulphur dioxide", "sulfur dioxide", "sulphites", "sulfites",
        ],
    },

    "low_cholesterol": {
        "label": "Low Cholesterol",
        "emoji": "❤️",
        "keywords": [
            # Egg yolk — highest dietary cholesterol source
            "egg yolk powder", "dried egg yolk", "egg yolk", "egg yolks",
            "whole egg powder", "whole egg", "eggs", "egg",
            # Organ meats — extremely high cholesterol
            "foie gras", "chicken liver", "beef liver", "lamb liver", "pig liver",
            "liver pâté", "liver paté", "liver pate", "liver",
            "kidney", "heart", "brain", "sweetbread", "offal",
            # High-cholesterol shellfish
            "shrimp", "prawns", "prawn", "crab", "lobster",
            "squid", "calamari", "cuttlefish",
            # Saturated animal fats (raise LDL)
            "butter",
            "lard", "pig fat",
            "beef tallow", "tallow",
            "suet", "beef suet",
            "dripping", "schmaltz", "animal fat",
            "ghee",
            # Full-fat dairy
            "double cream", "heavy cream", "whipping cream", "clotted cream",
            "soured cream", "sour cream",
            "full cream milk", "full fat milk", "whole milk",
            "cream",
            "parmesan", "parmigiano", "cream cheese", "brie", "camembert",
            "cheddar", "gruyère", "gruyere", "processed cheese",
            # Processed / fatty meats
            "sausage", "salami", "pepperoni", "chorizo",
            "hot dog", "frankfurter", "bacon",
            # Tropical saturated fats
            "coconut oil", "palm oil", "palm kernel oil", "palm fat",
            # Trans fats
            "partially hydrogenated", "hydrogenated vegetable oil",
            "interesterified fat",
        ],
    },

    "diabetic": {
        "label": "Diabetic",
        "emoji": "🩸",
        "keywords": [
            # High-glycaemic sweeteners
            "high fructose corn syrup", "glucose-fructose syrup",
            "glucose syrup", "corn syrup", "golden syrup",
            "maple syrup", "agave syrup", "agave", "treacle", "molasses",
            "invert sugar syrup", "invert sugar",
            "coconut sugar", "cane sugar", "beet sugar",
            "brown sugar", "demerara sugar", "muscovado sugar",
            "caster sugar", "icing sugar", "white sugar",
            "granulated sugar", "sugar",
            "dextrose", "sucrose", "glucose", "fructose", "maltose",
            "honey",
            # Rapidly-digested starches
            "maltodextrin", "dextrin",
            "modified starch", "modified food starch",
            "tapioca starch", "potato starch", "corn starch", "wheat starch",
            "tapioca", "arrowroot",
            # Refined flours (high GI)
            "white flour", "refined flour", "wheat flour",
            "plain flour", "all-purpose flour", "self-raising flour",
            "breadcrumbs",
            # High-GI grains
            "white rice", "rice flour", "corn flour", "oats",
            # Fruit sugars
            "fruit juice concentrate", "apple juice concentrate",
            "grape juice concentrate", "fruit concentrate", "fruit juice",
            "raisins", "sultanas", "currants", "dates", "dried fruit",
        ],
    },

    "anti_inflammatory": {
        "label": "Anti-Inflammatory",
        "emoji": "🔥",
        "keywords": [
            # Trans and hydrogenated fats (most pro-inflammatory)
            "partially hydrogenated", "hydrogenated vegetable oil",
            "hydrogenated oil", "interesterified fat",
            # Pro-inflammatory omega-6 seed oils
            "soybean oil", "corn oil", "sunflower oil",
            "safflower oil", "cottonseed oil", "grapeseed oil",
            "rice bran oil",
            # Refined carbohydrates
            "high fructose corn syrup", "glucose-fructose syrup",
            "glucose syrup", "corn syrup",
            "maltodextrin",
            "white flour", "refined flour", "wheat flour",
            "cane sugar", "white sugar", "brown sugar", "sugar",
            "dextrose", "sucrose", "glucose", "fructose",
            # Processed meats
            "salami", "pepperoni", "chorizo", "hot dog",
            "frankfurter", "sausage", "bacon",
            "sodium nitrite", "sodium nitrate",
            # Artificial additives (trigger inflammatory response)
            "artificial colour", "artificial color",
            "artificial flavour", "artificial flavor",
            "sodium benzoate", "potassium benzoate",
            "BHA", "BHT", "TBHQ",
            "tartrazine", "allura red", "sunset yellow",
            "carrageenan",
            # Flavour enhancers
            "monosodium glutamate", "MSG",
            "yeast extract", "autolyzed yeast extract",
            "hydrolyzed vegetable protein",
            # Refined sugar
            "honey",
            "maple syrup", "agave",
        ],
    },

    "sibo": {
        "label": "SIBO",
        "emoji": "🧫",
        "keywords": [
            # Prebiotic / fermentable fibers that feed SIBO bacteria
            "inulin", "chicory root", "chicory root extract", "chicory inulin",
            "fructooligosaccharides", "fructo-oligosaccharides",
            "galactooligosaccharides", "galacto-oligosaccharides",
            "lactulose",
            "guar gum", "guar",
            "psyllium husk", "psyllium",
            "pectin", "apple pectin",
            "resistant starch",
            "insoluble fiber", "insoluble fibre",
            # Fructose (ferments in small intestine)
            "honey", "agave", "high fructose corn syrup",
            "fructose", "apple juice concentrate", "pear juice concentrate",
            "apple puree", "pear puree",
            # Fructans — major SIBO triggers
            "garlic", "garlic powder", "garlic extract", "garlic oil",
            "onion", "onion powder", "onion extract", "onion flakes",
            "shallot", "shallots", "leek",
            "wheat", "rye", "barley",
            # Lactose (undigested lactose feeds bacteria)
            "lactose", "milk", "yogurt", "yoghurt",
            "cream cheese", "ricotta", "cottage cheese",
            "milk powder", "condensed milk",
            # Sugar alcohols (fermented to gas)
            "sorbitol", "mannitol", "xylitol", "maltitol",
            "isomalt", "lactitol", "erythritol",
            # Legumes (GOS)
            "beans", "lentils", "chickpeas", "soybeans", "edamame",
            "split peas",
            # Cruciferous vegetables (fermentable)
            "broccoli", "cauliflower", "cabbage", "brussels sprouts",
        ],
    },

    "crohns": {
        "label": "Crohn's Disease",
        "emoji": "🩹",
        "keywords": [
            # High-insoluble-fiber foods that irritate inflamed bowel
            "wheat bran", "oat bran", "rice bran", "bran",
            "whole grain", "wholegrain", "whole wheat",
            "seeds",
            "flaxseed", "linseed", "flax seeds",
            "sunflower seeds", "sunflower seed",
            "pumpkin seeds", "pumpkin seed",
            "sesame seeds", "sesame seed", "sesame",
            "poppy seeds", "poppy seed",
            # Nuts (can pass through intestine irritating walls)
            "almonds", "almond", "walnuts", "walnut",
            "cashew", "cashews", "peanuts", "peanut",
            "macadamia", "pistachio", "mixed nuts", "tree nuts",
            # Legumes (gas, fermentation, irritation)
            "beans", "kidney beans", "black beans", "lentils",
            "chickpeas", "soybeans", "peas", "split peas",
            "broad beans", "baked beans",
            # Spicy / irritating ingredients
            "chili pepper", "chilli pepper", "chili powder", "chilli powder",
            "cayenne pepper", "cayenne",
            "hot pepper", "jalapeño", "jalapeno", "habanero",
            "black pepper",
            # Sugar alcohols (ferment, cause gas)
            "sorbitol", "mannitol", "xylitol", "maltitol",
            "isomalt", "lactitol",
            # Dairy (Crohn's often causes secondary lactose intolerance)
            "lactose", "milk", "cream",
            "yogurt", "yoghurt",
            # Alcohol (irritates gut lining)
            "alcohol", "ethanol",
            "wine", "beer", "spirits", "cider",
            # Caffeine (stimulates gut motility)
            "caffeine",
            # Corn and popcorn (hard to digest)
            "corn", "maize", "sweetcorn", "popcorn",
            # High-fat fried / processed
            "partially hydrogenated", "hydrogenated vegetable oil",
            "lard", "tallow", "suet",
            # Artificial sweeteners (can trigger symptoms)
            "artificial sweetener", "sucralose", "aspartame",
        ],
    },
}

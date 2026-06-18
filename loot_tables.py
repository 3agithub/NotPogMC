MINE = {
        "overworld": [
            ("Cobblestone", 256, 1024), ("Coal", 0, 60), ("Iron Ingot", 0, 16),
            ("Copper Ingot", 0, 32), ("Gold Ingot", 0, 8), ("Redstone Dust", 0, 24),
            ("Lapis Lazuli", 0, 12), ("Diamond", 0, 4), ("Emerald", 0, 2)
        ],
        "nether": [
            ("Netherrack", 384, 1296), ("Nether Quartz", 0, 192), ("Gold Nugget", 0, 320),
            ("Glowstone Dust", 0, 192), ("Ancient Debris", 0, 2)
        ],
        "end": [
            ("End Stone", 192, 768)
        ]
    }

CHOP = {
    "overworld": {
        "biomes": {
            "forest": {"weight": 30, "trees": ["oak", "birch"]},
            "taiga": {"weight": 20, "trees": ["spruce"]},
            "birch forest": {"weight": 10, "trees": ["birch"]},
            "dark forest": {"weight": 10, "trees": ["dark_oak"]},
            "jungle": {"weight": 3, "trees": ["jungle"]},
            "savanna": {"weight": 2, "trees": ["acacia"]},
            "mangrove swamp": {"weight": 7, "trees": ["mangrove"]},
            "cherry grove": {"weight": 10, "trees": ["cherry"]},
            "pale garden": {"weight": 8, "trees": ["pale_oak"]}
        },
        "tree_data": {
            "oak": {"drops": [("Oak Log", 12, 28), ("Oak Sapling", 1, 3), ("Apple", 0, 2), ("Stick", 1, 4)]},
            "spruce": {"drops": [("Spruce Log", 16, 54), ("Spruce Sapling", 2, 5), ("Stick", 1, 5)]},
            "birch": {"drops": [("Birch Log", 10, 16), ("Birch Sapling", 1, 2), ("Stick", 1, 3)]},
            "dark_oak": {"drops": [("Dark Oak Log", 24, 48), ("Dark Oak Sapling", 2, 4), ("Apple", 0, 3), ("Stick", 2, 6)]},
            "jungle": {"drops": [("Jungle Log", 15, 64), ("Jungle Sapling", 1, 3), ("Vines", 0, 4), ("Cocoa Beans", 0, 3)]},
            "acacia": {"drops": [("Acacia Log", 8, 14), ("Acacia Sapling", 1, 2), ("Stick", 1, 3)]},
            "cherry": {"drops": [("Cherry Log", 12, 24), ("Cherry Sapling", 1, 3), ("Pink Petals", 1, 4), ("Stick", 1, 3)]},
            "pale_oak": {"drops": [("Pale Oak Log", 15, 36), ("Pale Oak Sapling", 1, 3), ("Pale Hanging Moss", 1, 4), ("Creaking Heart", 0, 1)]},
            "mangrove": {"drops": [("Mangrove Log", 12, 32), ("Mangrove Propagule", 1, 3), ("Mangrove Roots", 4, 12), ("Muddy Mangrove Roots", 2, 6)]}
        }
    },
    "nether": {
        "biomes": {
            "crimson forest": {"weight": 50, "trees": ["crimson"]},
            "warped forest": {"weight": 50, "trees": ["warped"]}
        },
        "tree_data": {
            "crimson": {"drops": [("Crimson Stem", 14, 32), ("Crimson Fungi", 1, 2), ("Shroomlight", 0, 2), ("Weeping Vines", 0, 3)]},
            "warped": {"drops": [("Warped Stem", 14, 32), ("Warped Fungi", 1, 2), ("Shroomlight", 0, 2), ("Twisting Vines", 0, 3)]}
        }
    },
    "end": {
        "biomes": {
            "end highlands": {"weight": 100, "trees": ["chorus_plant"]}
        },
        "tree_data": {
            "chorus_plant": {"drops": [("Chorus Fruit", 10, 24), ("Chorus Flower", 1, 3)]}
        }
    }
}
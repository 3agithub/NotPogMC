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

ADVENTURE = {
    "overworld": {
        "biomes": {
            "desert": {"weight": 40, "allowed_structures": ["desert pyramid", "none"]},
            "jungle": {"weight": 30, "allowed_structures": ["jungle pyramid", "none"]},
            "ocean": {"weight": 30, "allowed_structures": ["shipwreck", "none"]}
        },
        "structures": {
            "desert pyramid": {"weight": 70, "chests": (4, 4), "use_pools": True},
            "jungle pyramid": {"weight": 60, "chests": (2, 2), "use_pools": True},
            "shipwreck": {"weight": 80, "use_pools": True, "unique_chests": True},
            "none": {"weight": 30, "chests": (0, 0), "use_pools": False} 
        },
        "loot_pools": {
            "desert_pyramid_pools": [
                {
                    "min_rolls": 2, "max_rolls": 4,
                    "items": [
                        (None, 15, 1, 1),
                        ("Bone", 25, 4, 6),
                        ("Rotten Flesh", 25, 3, 7),
                        ("Spider Eye", 25, 1, 3),
                        ("Leather", 20, 1, 5),
                        ("Enchanted Book", 20, 1, 1),
                        ("Golden Apple", 20, 1, 1),
                        ("Gold Ingot", 15, 2, 7),
                        ("Iron Ingot", 15, 1, 5),
                        ("Emerald", 15, 1, 3),
                        ("Copper Horse Armor", 15, 1, 1),
                        ("Iron Horse Armor", 15, 1, 1),
                        ("Golden Horse Armor", 10, 1, 1),
                        ("Diamond", 5, 1, 3),
                        ("Diamond Horse Armor", 5, 1, 1),
                        ("Enchanted Golden Apple", 2, 1, 1)
                    ]
                },
                {
                    "min_rolls": 4, "max_rolls": 4,
                    "items": [
                        ("Bone", 10, 1, 8),
                        ("Rotten Flesh", 10, 1, 8),
                        ("Gunpowder", 10, 1, 8),
                        ("Sand", 10, 1, 8),
                        ("String", 10, 1, 8)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 6, 1, 1),
                        ("Dune Armor Trim Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "jungle_pyramid_pools": [
                {
                    "min_rolls": 2, "max_rolls": 6,
                    "items": [
                        ("Bone", 20, 4, 6),
                        ("Rotten Flesh", 16, 3, 7),
                        ("Gold Ingot", 15, 2, 7),
                        ("Bamboo", 15, 1, 3),
                        ("Iron Ingot", 10, 1, 5),
                        ("Leather", 3, 1, 5),
                        ("Diamond", 3, 1, 3),
                        ("Emerald", 2, 1, 3),
                        ("Copper Horse Armor", 1, 1, 1),
                        ("Enchanted Book", 1, 1, 1),
                        ("Iron Horse Armor", 1, 1, 1),
                        ("Golden Horse Armor", 1, 1, 1),
                        ("Diamond Horse Armor", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 2, 1, 1),
                        ("Wild Armor Trim Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "shipwreck_supply_pools": [
                {
                    "min_rolls": 3, "max_rolls": 10,
                    "items": [
                        ("Suspicious Stew", 10, 1, 1),
                        ("Paper", 8, 1, 12),
                        ("Wheat", 7, 8, 21),
                        ("Carrot", 7, 4, 8),
                        ("Poisonous Potato", 7, 2, 6),
                        ("Potato", 7, 2, 6),
                        ("Moss Block", 7, 1, 4),
                        ("Coal", 6, 2, 8),
                        ("Rotten Flesh", 5, 5, 24),
                        ("Gunpowder", 3, 1, 5),
                        ("Enchanted Leather Cap", 3, 1, 1),
                        ("Enchanted Leather Tunic", 3, 1, 1),
                        ("Enchanted Leather Pants", 3, 1, 1),
                        ("Enchanted Leather Boots", 3, 1, 1),
                        ("Bamboo", 2, 1, 3),
                        ("Pumpkin", 2, 1, 3),
                        ("TNT", 1, 1, 2)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        ("Coast Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        ("Copper Nautilus Armor", 20, 1, 1),
                        ("Iron Nautilus Armor", 10, 1, 1),
                        ("Golden Nautilus Armor", 5, 1, 1),
                        ("Diamond Nautilus Armor", 2, 1, 1)
                    ]
                }
            ],
            "shipwreck_treasure_pools": [
                {
                    "min_rolls": 3, "max_rolls": 6,
                    "items": [
                        ("Iron Ingot", 90, 1, 5),
                        ("Emerald", 40, 1, 5),
                        ("Gold Ingot", 10, 1, 5),
                        ("Bottle o' Enchanting", 5, 1, 1),
                        ("Diamond", 5, 1, 1)
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 5,
                    "items": [
                        ("Iron Nugget", 50, 1, 10),
                        ("Lapis Lazuli", 20, 1, 10),
                        ("Gold Nugget", 10, 1, 10)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        ("Coast Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        ("Copper Nautilus Armor", 20, 1, 1),
                        ("Iron Nautilus Armor", 10, 1, 1),
                        ("Golden Nautilus Armor", 5, 1, 1),
                        ("Diamond Nautilus Armor", 2, 1, 1)
                    ]
                }
            ],
            "shipwreck_map_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        ("Buried Treasure Map", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 3,
                    "items": [
                        ("Paper", 20, 1, 10),
                        ("Feather", 10, 1, 5),
                        ("Book", 5, 1, 5),
                        ("Clock", 1, 1, 1),
                        ("Compass", 1, 1, 1),
                        ("Empty Map", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        ("Coast Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        ("Copper Nautilus Armor", 20, 1, 1),
                        ("Iron Nautilus Armor", 10, 1, 1),
                        ("Golden Nautilus Armor", 5, 1, 1),
                        ("Diamond Nautilus Armor", 2, 1, 1)
                    ]
                }
            ]
        }
    },
    "nether": {
        "biomes": {
            "nether wastes": {"weight": 50, "allowed_structures": ["nether fortress", "bastion remnant with a bridge", "bastion remnant with hoglin stables", "bastion remnant with housing units", "bastion remnant with a treasure unit", "none"]},
            "crimson forest": {"weight": 50, "allowed_structures": ["nether fortress", "bastion remnant with a bridge", "bastion remnant with hoglin stables", "bastion remnant with housing units", "bastion remnant with a treasure unit", "none"]},
            "warped forest": {"weight": 50, "allowed_structures": ["nether fortress", "bastion remnant with a bridge", "bastion remnant with hoglin stables", "bastion remnant with housing units", "bastion remnant with a treasure unit", "none"]},
            "soul sand valley": {"weight": 30, "allowed_structures": ["nether fortress", "bastion remnant with a bridge", "bastion remnant with hoglin stables", "bastion remnant with housing units", "bastion remnant with a treasure unit", "none"]},
            "basalt deltas": {"weight": 30, "allowed_structures": ["nether fortress", "none"]}
        },
        "structures": {
            "nether fortress": {"weight": 50, "chests": (2, 6), "use_pools": True},
            "bastion remnant with a bridge": {"weight": 25, "chests": (5, 18), "use_pools": True, "generic_ratio": 3, "specific_ratio": 1},
            "bastion remnant with hoglin stables": {"weight": 25, "chests": (4, 12), "use_pools": True, "generic_ratio": 4, "specific_ratio": 1},
            "bastion remnant with housing units": {"weight": 25, "chests": (7, 16), "use_pools": True, "generic_ratio": 1, "specific_ratio": 0},
            "bastion remnant with a treasure unit": {"weight": 25, "chests": (8, 25), "use_pools": True, "generic_ratio": 9, "specific_ratio": 1},
            "none": {"weight": 20, "chests": (0, 0), "use_pools": False}
        },

        "loot_pools": {
            "bastion_generic_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        ("Golden Carrot", 12, 6, 17),
                        ("Ancient Debris", 12, 1, 1),
                        ("Spectral Arrow", 10, 10, 22),
                        ("Enchanted Book", 10, 1, 1),
                        ("Snout Banner Pattern", 9, 1, 1),
                        ("Golden Apple", 9, 1, 1),
                        ("Damaged Enchanted Crossbow", 6, 1, 1),
                        ("Diamond Shovel", 6, 1, 1),
                        ("Enchanted Diamond Pickaxe", 6, 1, 1),
                        ("Music Disc (Pigstep)", 5, 1, 1),
                        ("Netherite Scrap", 4, 1, 1)
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 2,
                    "items": [
                        ("Iron Ingot", 2, 1, 6),
                        ("Gold Ingot", 2, 1, 6),
                        ("Crying Obsidian", 2, 1, 5),
                        ("Block of Iron", 2, 1, 1),
                        ("Damaged Enchanted Iron Sword", 2, 1, 1),
                        ("Block of Gold", 2, 1, 1),
                        ("Crossbow", 1, 1, 1),
                        ("Golden Sword", 1, 1, 1),
                        ("Enchanted Golden Axe", 1, 1, 1),
                        ("Golden Helmet", 1, 1, 1),
                        ("Golden Chestplate", 1, 1, 1),
                        ("Golden Leggings", 1, 1, 1),
                        ("Golden Boots", 1, 1, 1),
                        ("Enchanted Golden Boots with Soul Speed", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        ("Arrow", 2, 5, 17),
                        ("Magma Cream", 2, 2, 6),
                        ("Gilded Blackstone", 2, 1, 5),
                        ("Iron Chain", 1, 2, 10),
                        ("Obsidian", 1, 4, 6),
                        ("String", 1, 4, 6),
                        ("Iron Nugget", 1, 2, 8),
                        ("Gold Nugget", 1, 2, 8),
                        ("Bone Block", 1, 3, 6),
                        ("Cooked Porkchop", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        ("Snout Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        ("Netherite Upgrade Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_a_bridge_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        ("Lodestone", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 2,
                    "items": [
                        ("Spectral Arrow", 1, 10, 28),
                        ("Gilded Blackstone", 1, 8, 12),
                        ("Iron Ingot", 1, 4, 9),
                        ("Gold Ingot", 1, 4, 9),
                        ("Crying Obsidian", 1, 3, 8),
                        ("Damaged Enchanted Crossbow", 1, 1, 1),
                        ("Block of Gold", 1, 1, 1),
                        ("Golden Sword", 1, 1, 1),
                        ("Enchanted Golden Axe", 1, 1, 1),
                        ("Enchanted Golden Helmet", 1, 1, 1),
                        ("Enchanted Golden Chestplate", 1, 1, 1),
                        ("Enchanted Golden Leggings", 1, 1, 1),
                        ("Enchanted Golden Boots", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 4,
                    "items": [
                        ("Arrow", 1, 5, 17),
                        ("Iron Nugget", 1, 2, 6),
                        ("Gold Nugget", 1, 2, 6),
                        ("String", 1, 1, 6),
                        ("Leather", 1, 1, 3)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        ("Snout Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        ("Netherite Upgrade Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_hoglin_stables_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        ("Block of Gold", 16, 2, 4),
                        ("Damaged Enchanted Diamond Shovel", 15, 1, 1),
                        ("Ancient Debris", 12, 1, 1),
                        ("Saddle", 12, 1, 1),
                        ("Enchanted Diamond Pickaxe", 12, 1, 1),
                        ("Golden Carrot", 10, 8, 17),
                        ("Golden Apple", 10, 1, 1),
                        ("Netherite Scrap", 8, 1, 1),
                        ("Ancient Debris", 5, 2, 2)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        ("Arrow", 1, 5, 17),
                        ("String", 1, 3, 8),
                        ("Gold Nugget", 1, 2, 8),
                        ("Crimson Fungus", 1, 2, 7),
                        ("Crimson Nylium", 1, 2, 7),
                        ("Crimson Roots", 1, 2, 7),
                        ("Glowstone", 1, 3, 6),
                        ("Soul Sand", 1, 2, 7),
                        ("Cooked Porkchop", 1, 2, 5),
                        ("Gilded Blackstone", 1, 2, 5),
                        ("Raw Porkchop", 1, 2, 5),
                        ("Crying Obsidian", 1, 1, 5),
                        ("Leather", 1, 1, 3),
                        ("Enchanted Golden Axe", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        ("Snout Armor Trim Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        ("Netherite Upgrade Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_a_treasure_unit_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        ("Netherite Upgrade Smithing Template", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 3,
                    "items": [
                        ("Netherite Ingot", 15, 1, 1),
                        ("Ancient Debris", 10, 1, 1),
                        ("Netherite Scrap", 8, 1, 1),
                        ("Damaged Enchanted Diamond Spear", 6, 1, 1),
                        ("Damaged Enchanted Diamond Sword", 6, 1, 1),
                        ("Diamond Spear", 6, 1, 1),
                        ("Diamond Sword", 6, 1, 1),
                        ("Damaged Enchanted Diamond Helmet", 6, 1, 1),
                        ("Damaged Enchanted Diamond Chestplate", 6, 1, 1),
                        ("Damaged Enchanted Diamond Leggings", 6, 1, 1),
                        ("Damaged Enchanted Diamond Boots", 6, 1, 1),
                        ("Diamond", 5, 2, 6),
                        ("Diamond Helmet", 5, 1, 1),
                        ("Diamond Chestplate", 5, 1, 1),
                        ("Diamond Leggings", 5, 1, 1),
                        ("Diamond Boots", 5, 1, 1),
                        ("Ancient Debris", 4, 2, 2),
                        ("Enchanted Golden Apple", 2, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        ("Spectral Arrow", 1, 12, 25),
                        ("Nether Quartz", 1, 8, 23),
                        ("Gilded Blackstone", 1, 5, 15),
                        ("Iron Ingot", 1, 3, 9),
                        ("Gold Ingot", 1, 3, 9),
                        ("Magma Cream", 1, 3, 8),
                        ("Crying Obsidian", 1, 3, 5),
                        ("Block of Iron", 1, 2, 5),
                        ("Block of Gold", 1, 2, 5)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        ("Snout Armor Trim Smithing Template", 1, 1, 1)
                    ]
                }
            ],
            "nether_fortress_pools": [
                {
                    "min_rolls": 2, "max_rolls": 4,
                    "items": [
                        ("Gold Ingot", 15, 1, 3),
                        ("Saddle", 10, 1, 1),
                        ("Golden Horse Armor", 8, 1, 1),
                        ("Nether Wart", 5, 3, 7),
                        ("Iron Ingot", 5, 1, 5),
                        ("Diamond", 5, 1, 3),
                        ("Copper Horse Armor", 5, 1, 1),
                        ("Flint and Steel", 5, 1, 1),
                        ("Iron Horse Armor", 5, 1, 1),
                        ("Golden Sword", 5, 1, 1),
                        ("Golden Chestplate", 5, 1, 1),
                        ("Diamond Horse Armor", 3, 1, 1),
                        ("Obsidian", 2, 2, 4)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 14, 1, 1),
                        ("Rib Armor Trim Smithing Template", 1, 1, 1)
                    ]
                }
            ]
        }
    },
    "end": {
        "biomes": {
            "end highlands": {"weight": 100, "allowed_structures": ["end city", "none"]}
        },
        "structures": {
            "end city": {"weight": 80, "chests": (2, 10), "use_pools": True},
            "none": {"weight": 20, "chests": (0, 0), "use_pools": False}
        },
        "loot_pools": {
            "end_city_pools": [
                {
                    "min_rolls": 2, "max_rolls": 6,
                    "items": [
                        ("Gold Ingot", 15, 2, 7),
                        ("Iron Ingot", 10, 4, 8),
                        ("Beetroot Seeds", 5, 1, 10),
                        ("Diamond", 5, 2, 7),
                        ("Saddle", 3, 1, 1),
                        ("Enchanted Iron Pickaxe", 3, 1, 1),
                        ("Enchanted Iron Shovel", 3, 1, 1),
                        ("Enchanted Iron Sword", 3, 1, 1),
                        ("Enchanted Iron Helmet", 3, 1, 1),
                        ("Enchanted Iron Chestplate", 3, 1, 1),
                        ("Enchanted Iron Leggings", 3, 1, 1),
                        ("Enchanted Iron Boots", 3, 1, 1),
                        ("Enchanted Diamond Pickaxe", 3, 1, 1),
                        ("Enchanted Diamond Shovel", 3, 1, 1),
                        ("Enchanted Diamond Spear", 3, 1, 1),
                        ("Enchanted Diamond Sword", 3, 1, 1),
                        ("Enchanted Diamond Helmet", 3, 1, 1),
                        ("Enchanted Diamond Chestplate", 3, 1, 1),
                        ("Enchanted Diamond Leggings", 3, 1, 1),
                        ("Enchanted Diamond Boots", 3, 1, 1),
                        ("Emerald", 2, 2, 6),
                        ("Copper Horse Armor", 1, 1, 1),
                        ("Iron Horse Armor", 1, 1, 1),
                        ("Golden Horse Armor", 1, 1, 1),
                        ("Diamond Horse Armor", 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 14, 1, 1),
                        ("Spire Armor Trim Smithing Template", 1, 1, 1)
                    ]
                }
            ]
        }
    }
}
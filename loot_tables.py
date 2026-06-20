MINE = {
        "overworld": [
            (1101, 128, 512), (17201, 0, 60), (17401, 0, 16),
            (17402, 0, 32), (17403, 0, 8), (10901, 0, 24),
            (17203, 0, 12), (17204, 0, 4), (17202, 0, 2)
        ],
        "nether": [
            (2601, 192, 576), (17301, 0, 96), (17502, 0, 128),
            (18602, 0, 32), (5803, 0, 2)
        ],
        "end": [
            (2901, 64, 384)
        ]
    }

CHOP = {
    "overworld": {
        "biomes": {
            "forest": {"weight": 30, "trees": ["oak", "birch"]},
            "taiga": {"weight": 20, "trees": ["spruce"]},
            "birch forest": {"weight": 10, "trees": ["birch"]},
            "dark forest": {"weight": 10, "trees": ["dark_oak"]},
            "jungle": {"weight": 6, "trees": ["jungle", "oak"]},
            "savanna": {"weight": 15, "trees": ["acacia"]},
            "mangrove swamp": {"weight": 7, "trees": ["mangrove"]},
            "cherry grove": {"weight": 10, "trees": ["cherry"]},
            "pale garden": {"weight": 3, "trees": ["pale_oak"]}
        },
        "tree_data": {
            "oak": {"drops": [(101, 12, 28), (6501, 1, 3), (15701, 0, 2), (17601, 1, 4)]},
            "spruce": {"drops": [(201, 16, 54), (6502, 2, 5), (17601, 1, 5)]},
            "birch": {"drops": [(301, 10, 16), (6503, 1, 2), (17601, 1, 3)]},
            "dark_oak": {"drops": [(601, 24, 48), (6506, 2, 4), (15701, 0, 3), (17601, 2, 6)]},
            "jungle": {"drops": [(401, 15, 64), (6504, 1, 3), (6904, 0, 4), (7403, 0, 3)]},
            "acacia": {"drops": [(501, 8, 14), (6506, 1, 2), (17601, 1, 3)]},
            "cherry": {"drops": [(19301, 12, 24), (6510, 1, 3), (6819, 1, 4), (17601, 1, 3)]},
            "pale_oak": {"drops": [(20001, 15, 36), (6511, 1, 3), (20103, 1, 4), (20104, 0, 1)]},
            "mangrove": {"drops": [(701, 12, 32), (6507, 1, 3), (6208, 4, 12), (6209, 2, 6)]}
        }
    },
    "nether": {
        "biomes": {
            "crimson forest": {"weight": 50, "trees": ["crimson"]},
            "warped forest": {"weight": 50, "trees": ["warped"]}
        },
        "tree_data": {
            "crimson": {"drops": [(801, 14, 32), (6601, 1, 2), (6405, 2, 5), (7004, 1, 7)]},
            "warped": {"drops": [(901, 14, 32), (6602, 1, 2), (6405, 2, 5), (7005, 1, 7)]}
        }
    },
    "end": {
        "biomes": {
            "end highlands": {"weight": 100, "trees": ["chorus_plant"]}
        },
        "tree_data": {
            "chorus_plant": {"drops": [(15705, 10, 24), (7102, 1, 3)]}
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
                        (17701, 25, 4, 6),
                        (16501, 25, 3, 7),
                        (16502, 25, 1, 3),
                        (17703, 20, 1, 5),
                        #("Enchanted Book", 20, 1, 1),
                        (15702, 20, 1, 1),
                        (17208, 15, 2, 7),
                        (17206, 15, 1, 5),
                        (17202, 15, 1, 3),
                        (15206, 15, 1, 1),
                        (15202, 15, 1, 1),
                        (15203, 10, 1, 1),
                        (17204, 5, 1, 3),
                        (15204, 5, 1, 1),
                        (15703, 2, 1, 1)
                    ]
                },
                {
                    "min_rolls": 4, "max_rolls": 4,
                    "items": [
                        (17701, 10, 1, 8),
                        (16501, 10, 1, 8),
                        (18603, 10, 1, 8),
                        (5101, 10, 1, 8),
                        (11502, 10, 1, 8)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 6, 1, 1),
                        (19503, 1, 1, 1)
                    ]
                }
            ],
            "jungle_pyramid_pools": [
                {
                    "min_rolls": 2, "max_rolls": 6,
                    "items": [
                        (17701, 20, 4, 6),
                        (16501, 16, 3, 7),
                        (17208, 15, 2, 7),
                        (6901, 15, 1, 3),
                        (17206, 10, 1, 5),
                        (17703, 3, 1, 5),
                        (17204, 3, 1, 3),
                        (17202, 2, 1, 3),
                        (15206, 1, 1, 1),
                        #("Enchanted Book", 1, 1, 1),
                        (15202, 1, 1, 1),
                        (15203, 1, 1, 1),
                        (15204, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 2, 1, 1),
                        (19513, 1, 1, 1)
                    ]
                }
            ],
            "shipwreck_supply_pools": [
                {
                    "min_rolls": 3, "max_rolls": 10,
                    "items": [
                        #("Suspicious Stew", 10, 1, 1),
                        (18401, 8, 1, 12),
                        (17603, 7, 8, 21),
                        (15801, 7, 4, 8),
                        (15805, 7, 2, 6),
                        (15803, 7, 2, 6),
                        (5301, 7, 1, 4),
                        (17201, 6, 2, 8),
                        (16501, 5, 5, 24),
                        (18603, 3, 1, 5),
                        (14501, 3, 1, 1), # enchanted
                        (14502, 3, 1, 1), # enchanted
                        (14503, 3, 1, 1), # enchanted
                        (14504, 3, 1, 1), # enchanted
                        (6901, 2, 1, 3),
                        (7405, 2, 1, 3),
                        (11401, 1, 1, 2)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        (19502, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        (15208, 20, 1, 1),
                        (15209, 10, 1, 1),
                        (15210, 5, 1, 1),
                        (15211, 2, 1, 1)
                    ]
                }
            ],
            "shipwreck_treasure_pools": [
                {
                    "min_rolls": 3, "max_rolls": 6,
                    "items": [
                        (17206, 90, 1, 5),
                        (17202, 40, 1, 5),
                        (17208, 10, 1, 5),
                        (18801, 5, 1, 1),
                        (17204, 5, 1, 1)
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 5,
                    "items": [
                        (17501, 50, 1, 10),
                        (17203, 20, 1, 10),
                        (17502, 10, 1, 10)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        (19502, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        (15208, 20, 1, 1),
                        (15209, 10, 1, 1),
                        (15210, 5, 1, 1),
                        (15211, 2, 1, 1)
                    ]
                }
            ],
            "shipwreck_map_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (13302, 1, 1, 1) # buried treasure map
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 3,
                    "items": [
                        (18401, 20, 1, 10),
                        (17702, 10, 1, 5),
                        (18402, 5, 1, 5),
                        (13201, 1, 1, 1),
                        (13101, 1, 1, 1),
                        (13302, 1, 1, 1) # empty
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 5, 1, 1),
                        (19502, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 148, 1, 1),
                        (15208, 20, 1, 1),
                        (15209, 10, 1, 1),
                        (15210, 5, 1, 1),
                        (15211, 2, 1, 1)
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
                        (15802, 12, 6, 17),
                        (5803, 12, 1, 1),
                        (15602, 10, 10, 22),
                        #("Enchanted Book", 10, 1, 1),
                        (18706, 9, 1, 1),
                        (15702, 9, 1, 1),
                        (15502, 6, 1, 1), # damaged / enchanted
                        (12001, 6, 1, 1),
                        (12002, 6, 1, 1), # enchanted
                        (14101, 5, 1, 1),
                        (17404, 4, 1, 1)
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 2,
                    "items": [
                        (17206, 2, 1, 6),
                        (17208, 2, 1, 6),
                        (5402, 2, 1, 5),
                        (3102, 2, 1, 1),
                        (14203, 2, 1, 1), # damaged / enchanted
                        (3103, 2, 1, 1),
                        (15502, 1, 1, 1),
                        (14204, 1, 1, 1),
                        (11903, 1, 1, 1), # enchanted
                        (14801, 1, 1, 1),
                        (14802, 1, 1, 1),
                        (14803, 1, 1, 1),
                        (14804, 1, 1, 1),
                        (14804, 1, 1, 1) # enchanted w/ soul speed
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        (15601, 2, 5, 17),
                        (18610, 2, 2, 6),
                        (2818, 2, 1, 5),
                        (3205, 1, 2, 10),
                        (5401, 1, 4, 6),
                        (11502, 1, 4, 6),
                        (17501, 1, 2, 8),
                        (17502, 1, 2, 8),
                        (5603, 1, 3, 6),
                        (16002, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        (19508, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        (19501, 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_a_bridge_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (9501, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 2,
                    "items": [
                        (15602, 1, 10, 28),
                        (2818, 1, 8, 12),
                        (17206, 1, 4, 9),
                        (17208, 1, 4, 9),
                        (5402, 1, 3, 8),
                        (15502, 1, 1, 1), # damaged / encahnted
                        (3103, 1, 1, 1),
                        (14204, 1, 1, 1),
                        (11903, 1, 1, 1), # enchanted
                        (14801, 1, 1, 1), # enchanted
                        (14802, 1, 1, 1), # enchanted
                        (14803, 1, 1, 1), # enchanted
                        (14804, 1, 1, 1) # enchanted
                    ]
                },
                {
                    "min_rolls": 2, "max_rolls": 4,
                    "items": [
                        (15601, 1, 5, 17),
                        (17501, 1, 2, 6),
                        (17502, 1, 2, 6),
                        (11502, 1, 1, 6),
                        (17703, 1, 1, 3)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        (19508, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        (19501, 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_hoglin_stables_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (3103, 16, 2, 4),
                        (12001, 15, 1, 1), # damaged / enchanted
                        (5803, 12, 1, 1),
                        (13503, 12, 1, 1),
                        (12002, 12, 1, 1), # enchanted
                        (15802, 10, 8, 17),
                        (15702, 10, 1, 1),
                        (17404, 8, 1, 1),
                        (5803, 5, 2, 2)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        (15601, 1, 5, 17),
                        (11502, 1, 3, 8),
                        (17502, 1, 2, 8),
                        (6601, 1, 2, 7),
                        (5501, 1, 2, 7),
                        (7001, 1, 2, 7),
                        (6404, 1, 3, 6),
                        (5601, 1, 2, 7),
                        (16002, 1, 2, 5),
                        (2818, 1, 2, 5),
                        (15902, 1, 2, 5),
                        (5402, 1, 1, 5),
                        (17703, 1, 1, 3),
                        (11903, 1, 1, 1) # enchanted
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        (19508, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 9, 1, 1),
                        (19501, 1, 1, 1)
                    ]
                }
            ],
            "bastion_remnant_with_a_treasure_unit_pools": [
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (19501, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 3,
                    "items": [
                        (17302, 15, 1, 1),
                        (5803, 10, 1, 1),
                        (17404, 8, 1, 1),
                        (20906, 6, 1, 1), # damaged / enchanted
                        (14205, 6, 1, 1), # damaged / enchanted
                        (20906, 6, 1, 1),
                        (14205, 6, 1, 1),
                        (14901, 6, 1, 1), # damaged / enchanted
                        (14902, 6, 1, 1), # damaged / enchanted
                        (14903, 6, 1, 1), # damaged / enchanted
                        (14904, 6, 1, 1), # damaged / enchanted
                        (17204, 5, 2, 6),
                        (14901, 5, 1, 1),
                        (14902, 5, 1, 1),
                        (14903, 5, 1, 1),
                        (14904, 5, 1, 1),
                        (5803, 4, 2, 2),
                        (15703, 2, 1, 1)
                    ]
                },
                {
                    "min_rolls": 3, "max_rolls": 4,
                    "items": [
                        (15602, 1, 12, 25),
                        (17301, 1, 8, 23),
                        (2818, 1, 5, 15),
                        (17206, 1, 3, 9),
                        (17208, 1, 3, 9),
                        (18610, 1, 3, 8),
                        (5402, 1, 3, 5),
                        (3102, 1, 2, 5),
                        (3103, 1, 2, 5)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 11, 1, 1),
                        (19508, 1, 1, 1)
                    ]
                }
            ],
            "nether_fortress_pools": [
                {
                    "min_rolls": 2, "max_rolls": 4,
                    "items": [
                        (17208, 15, 1, 3),
                        (13503, 10, 1, 1),
                        (15203, 8, 1, 1),
                        (7413, 5, 3, 7),
                        (17206, 5, 1, 5),
                        (17204, 5, 1, 3),
                        (15206, 5, 1, 1),
                        (12401, 5, 1, 1),
                        (15202, 5, 1, 1),
                        (14204, 5, 1, 1),
                        (14802, 5, 1, 1),
                        (15204, 3, 1, 1),
                        (5401, 2, 2, 4)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 14, 1, 1),
                        (19505, 1, 1, 1)
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
                        (17208, 15, 2, 7),
                        (17206, 10, 4, 8),
                        (7410, 5, 1, 10),
                        (17204, 5, 2, 7),
                        (13503, 3, 1, 1),
                        (11802, 3, 1, 1), # enchanted
                        (11801, 3, 1, 1), # enchanted
                        (14203, 3, 1, 1), # enchanted
                        (14701, 3, 1, 1), # enchanted
                        (14702, 3, 1, 1), # enchanted
                        (14703, 3, 1, 1), # enchanted
                        (14704, 3, 1, 1), # enchanted
                        (12002, 3, 1, 1), # enchanted
                        (12001, 3, 1, 1), # enchanted
                        (20906, 3, 1, 1), # enchanted
                        (14205, 3, 1, 1), # enchanted
                        (14901, 3, 1, 1), # enchanted
                        (14902, 3, 1, 1), # enchanted
                        (14903, 3, 1, 1), # enchanted
                        (14904, 3, 1, 1), # enchanted
                        (17202, 2, 2, 6),
                        (15206, 1, 1, 1),
                        (15202, 1, 1, 1),
                        (15203, 1, 1, 1),
                        (15204, 1, 1, 1)
                    ]
                },
                {
                    "min_rolls": 1, "max_rolls": 1,
                    "items": [
                        (None, 14, 1, 1),
                        (19509, 1, 1, 1)
                    ]
                }
            ]
        }
    }
}
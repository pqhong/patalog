import argparse
import copy
import json


CATALOG_FILENAME = 'catalog.json'

def perform():
    with open(CATALOG_FILENAME, 'r') as f:
        catalog = json.load(f)

    update_catalog = copy.deepcopy(catalog)
    version = update_catalog['version']

    if version < 6:
        update_catalog = perform_1_4_0(update_catalog)

    if version < 7:
        update_catalog = perform_1_5_0(update_catalog)

    with open(CATALOG_FILENAME, 'w') as f:
        json.dump(update_catalog, f, separators=(',', ':'))

def perform_1_4_0(update_catalog):
    update_catalog = copy.deepcopy(update_catalog)
    cat = update_catalog['catalog']

    items_1_4_0 = [
        (
            'lunas bed',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrTapBedS.png'
                    }
                },
                'get': 'Luna\nAll Year'
            }
        ),
        (
            'rodeo style springy ride on',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrSpringriderRodeo.png'
                    }
                },
                'get': 'Nook Shopping Seasonal\nCowboy Festival'
            }
        ),
        (
            'fireworks show wall',
            {
                'type': 'misc',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/RoomSpWallFireworks00.png'
                    }
                },
                'get': 'Nintendo\nUpdate 1.4.0'
            }
        ),
        (
            'moon rug',
            {
                'type': 'misc',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/RugRoundMoonM00.png'
                    }
                },
                'get': 'Nook Shopping Seasonal\nMoon-Viewing Day'
            }
        ),
        (
            'hikoboshi outfit',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceKimonoLWeavermen0.png'
                    }
                },
                'get': 'Nook Shopping Seasonal\nCowherd & Weaver Girl Day'
            }
        ),
        (
            'orihime outfit',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceKimonoLWeaverwomen0.png'
                    }
                },
                'get': 'Nook Shopping Seasonal\nCowherd & Weaver Girl Day'
            }
        ),
        (
            'bulb bopper',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFBallband0.png'
                    }
                },
                'get': 'Isabelle\nFireworks Display'
            }
        ),
        (
            'flower bopper',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFFlowerband0.png'
                    }
                },
                'get': 'Isabelle\nFireworks Display'
            }
        ),
        (
            'heart bopper',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHeartband0.png'
                    }
                },
                'get': 'Isabelle\nFireworks Display'
            }
        ),
        (
            'king tut mask',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceKingtut0.png'
                    }
                },
                'get': 'Crafting\nAll Year'
            }
        ),
        (
            'star bopper',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFStarband0.png'
                    }
                },
                'get': 'Isabelle\nFireworks Display'
            }
        ),
        (
            'grape harvest basket',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHarvest0.png'
                    }
                },
                'get': 'Nook Shopping Seasonal\nGrape Harvest Festival'
            }
        ),
        (
            'king tut mask ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'Digging\nPicking up gold nuggets knocked out of rocks'
            }
        )
    ]

    for item in items_1_4_0:
        cat[item[0]] = item[1]

    # Fix some previous item data
    cat['bamboo grass']['get'] = 'Nook Shopping Seasonal\nTanabata'
    cat['handmade cape']['get'] = 'Nook Shopping Seasonal\nInternational Children\'s Day'
    cat['handmade crown']['get'] = 'Nook Shopping Seasonal\nInternational Children\'s Day'
    cat['summer solstice crown']['get'] = 'Nook Shopping Seasonal\nSummer Solstice Festival'
    cat['thank you dad mug']['get'] = 'Nook Shopping Seasonal\nFather\'s Day'
    cat['thank you mom mug']['get'] = 'Nook Shopping Seasonal\nMother\'s Day'
    cat['winter solstice sweater']['get'] = 'Nook Shopping Seasonal\nWinter Solstice Festival'

    update_catalog['catalog'] = cat
    update_catalog['version'] = 6
    return update_catalog


def perform_1_5_0(update_catalog):
    update_catalog = copy.deepcopy(update_catalog)
    cat = update_catalog['catalog']

    items_1_5_0 = [
        (
            'spooky arch',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnArch_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnArch_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnArch_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnArch_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky carriage',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnCarriage_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnCarriage_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnCarriage_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnCarriage_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Jack\nHalloween Season'
            }
        ),
        (
            'spooky chair',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnChairS_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnChairS_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnChairS_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnChairS_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky lantern',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLantern_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLantern_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLantern_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLantern_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky lantern set',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLanternset_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLanternset_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLanternset_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnLanternset_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky scarecrow',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnScarecrow_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnScarecrow_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnScarecrow_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnScarecrow_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky standing lamp',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnStand_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnStand_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnStand_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnStand_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky table',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTableL_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTableL_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTableL_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTableL_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky tower',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTower_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTower_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTower_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTower_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky candy set',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnSweets_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnSweets_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnSweets_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnSweets_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky table setting',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTablesetting_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTablesetting_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTablesetting_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnTablesetting_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; Nook\'s Cranny\nHalloween Season'
            }
        ),
        (
            'spooky garland',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnDecorationWall_Remake_0_0.png'
                    },
                    '1': {
                        'variation': 'Yellow',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnDecorationWall_Remake_1_0.png'
                    },
                    '2': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnDecorationWall_Remake_2_0.png'
                    },
                    '3': {
                        'variation': 'Monochrome',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnDecorationWall_Remake_3_0.png'
                    }
                },
                'get': 'Crafting; All villagers\nHalloween Season'
            }
        ),
        (
            'flashy animal costume',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceOverallLHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'mages dress',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceBalloonLHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'magic academy robe',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceRobeLHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'raggedy outfit',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceSalopetteLHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'flashy pointy ear animal hat',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweentriangle5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'flashy round ear animal hat',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloweenround5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'impish horns',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapOrnamentFHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'mages striped hat',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapHatHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'magic academy hood',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloweenhood5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'horizontal striped tights',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/SocksTexHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'flashy animal boots',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesLowcutHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'mages boots',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/ShoesHighcutHalloween5.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'impish wings',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'Orange',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween0.png'
                    },
                    '1': {
                        'variation': 'Purple',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween1.png'
                    },
                    '2': {
                        'variation': 'White',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween2.png'
                    },
                    '3': {
                        'variation': 'Green',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween3.png'
                    },
                    '4': {
                        'variation': 'Red',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween4.png'
                    },
                    '5': {
                        'variation': 'Black',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/BagBackpackHalloween5.png'
                    }
                },
                'get': 'Kicks\nAll Year'
            }
        ),
        (
            'ring con',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrRingcon.png'
                    }
                },
                'get': 'Nintendo; Nook Shopping Daily Selection'
            }
        ),
        (
            'jacks portrait',
            {
                'type': 'furniture',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/FtrHwnPortraitWall.png'
                    }
                },
                'get': 'Jack\nReceived in the mail'
            }
        ),
        (
            'jacks robe',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceAlongLHalloween0.png'
                    }
                },
                'get': 'Jack\nAll Year'
            }
        ),
        (
            'jacks face',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/CapFullfaceHalloween0.png'
                    }
                },
                'get': 'Jack\nAll Year'
            }
        ),
        (
            'animal nose',
            {
                'type': 'fashion',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/AccessoryMouthHalloween0.png'
                    }
                },
                'get': 'Able Sisters\nAll Year'
            }
        ),
        (
            'spooky wall',
            {
                'type': 'misc',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/RoomTexWallHalloween00.png'
                    }
                },
                'get': 'Villagers\nHalloween Season'
            }
        ),
        (
            'spooky flooring',
            {
                'type': 'misc',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/RoomTexFloorHalloween00.png'
                    }
                },
                'get': 'Villagers\nHalloween Season'
            }
        ),
        (
            'spooky rug',
            {
                'type': 'misc',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': 'https://acnhcdn.com/latest/FtrIcon/RugSquareHalloweenL00.png'
                    }
                },
                'get': 'Villagers\nHalloween Season'
            }
        ),
        (
            'spooky arch ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky candy set ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky carriage ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers; Jack\nHalloween Season'
            }
        ),
        (
            'spooky chair ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky fence ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky garland ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky lantern ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky lantern set ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky scarecrow ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky standing lamp ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky table ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky table setting ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky tower ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers\nHalloween Season'
            }
        ),
        (
            'spooky wand ',
            {
                'type': 'diy',
                'have': False,
                'vars': {
                    '0': {
                        'variation': 'N/A',
                        'have': False,
                        'img': ''
                    }
                },
                'get': 'All villagers; Jack\nHalloween Season'
            }
        )
    ]

    for item in items_1_5_0:
        cat[item[0]] = item[1]

    update_catalog['catalog'] = cat
    update_catalog['version'] = 7
    return update_catalog

def main():
    perform()

if __name__ == '__main__':
    main()

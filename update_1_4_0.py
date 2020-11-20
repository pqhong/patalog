def perform(update_catalog):
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

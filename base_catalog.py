"""
Builds the base catalog using the ACNH Spreadsheet API
  https://acnh.tnrd.net/index.html
  https://tinyurl.com/acnh-sheet
"""

import json
import requests


CATALOG_FILENAME = 'catalog.json'
FURNITURE_CATEGORIES = [
    'Art',
    'Housewares',
    'Miscellaneous',
    'WallMounted'
]
FASHION_CATEGORIES = [
    'Accessories',
    'Bags',
    'Bottoms',
    'DressUp',
    'Headwear',
    'Shoes',
    'Socks',
    'Tops',
    'Umbrellas'
]
MISC_CATEGORIES = [
    'Floors',
    'Music',
    'Rugs',
    'Wallpapers'
]
DIY_CATEGORY = 'Recipes'
FISH_CATEGORY = 'Fish'
BUG_CATEGORY = 'Insects'
BASE_URL = 'https://acnh.tnrd.net/api/v3/'


def get_items(type, categories):
    ret = dict()
    for category in categories:
        print('Getting category: {0}'.format(category))
        api_url = BASE_URL + category
        res = requests.get(api_url)
        items = res.json()
        for item in items:
            item_name = item['name'].lower()
            if item_name in ['writing chair', 'writing desk', 'writing poster']:
                item_name = item_name.replace('writing', 'study')
            replacements = [
                ('.', ''),
                ('-', ' '),
                ('\'', ''),
                ('\u00e9', 'e'),
                ('\u00e1', 'a'),
                ('\u00e0', 'a'),
                ('\u2190', '<'),
                ('\u2192', '>')
            ]
            for replacement in replacements:
                item_name = item_name.replace(replacement[0], replacement[1])
            if category == 'Recipes':
                item_name += ' '
            
            if category == 'Art':
                variation = 'Real' if item['genuine'] else 'Fake'
                vid = '0' if item['genuine'] else '1'
            elif category in ['Umbrellas', 'Floors', 'Music', 'Rugs', 'Wallpapers', 'Recipes']:
                variation = 'N/A'
                vid = '0'
            elif category in ['Fish', 'Insects']:
                variation = 'Caught'
                vid = '0'
            else:
                variation = item['variation']
                vid = item['variantID'][0] if 'variantID' in item and item['variantID'] else item['filename'][-1]
            if variation == 'NA':
                variation = 'N/A'

            if category == 'Recipes':
                img = ''
            elif category == 'Music':
                img = 'https://acnhcdn.com/latest/Audio/{0}.png'.format(item['filename'])
            elif category in FASHION_CATEGORIES:
                img = item['storageImage']
            elif category in ['Fish', 'Insects']:
                img = item['iconImage']
            else:
                img = item['image']

            if category in ['Fish', 'Insects']:
                source = item['whereHow']
            else:
                source = ', '.join(item['source'])
            if source == 'Wedding Season':
                source = 'Cyrus'
                season = 'Wedding Season'
            elif source == 'International Museum Day':
                source = 'Blathers'
                season = 'International Museum Day'
            elif source == 'Bunny Day':
                source = 'Zipper'
                season = 'Bunny Day'
            elif source == 'Bug-Off':
                source = 'Flick'
                season = 'Bug-Off'
            elif source == 'Fishing Tourney':
                source = 'C.J.'
                season = 'Fishing Tourney'

            if category in ['Fish', 'Insects']:
                time = []
                nh = 'NH: '
                sh = 'SH: '

                for h in ['nh', 'sh']:
                    avail = []
                    for m in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                        t = item[h + m]
                        if t != 'NA':
                            if not time:
                                for slot in t:
                                    slot.replace('\u00A0', ' ')
                                    time.append(slot)
                            avail.append(m)
                    if h == 'nh':
                        nh += ', '.join(avail)
                    else:
                        sh += ', '.join(avail)

                season = '\n'.join([nh, sh, ', '.join(time)])
            elif 'seasonalAvailability' in item.keys():
                season = item['seasonalAvailability']
            elif item_name in ['retro fan', 'surfboard']:
                season = 'Summer'
            elif item_name in ['round space heater', 'celebratory candles']:
                season = 'Winter'
            elif item['sourceNotes']:
                seasons = [
                    'Wedding Season',
                    'Bunny Day',
                    'Fall',
                    'Maple Leaf Season',
                    'Spring',
                    'Festive Season',
                    'Cherry-Blossom Season',
                    'Mushroom Season',
                    'Nature Day',
                    'Winter',
                    'Summer'
                ]
                for s in seasons:
                    if s in item['sourceNotes']:
                        season = s
            else:
                season = 'All Year'

            get = source + '\n' + season

            var_obj = {
                'variation': variation,
                'have': False,
                'img': img
            }

            if item_name not in ret.keys():
                ret[item_name] = {
                    'type': type,
                    'have': False,
                    'vars': {
                        vid: var_obj
                    },
                    'get': get
                }
            else:
                ret[item_name]['vars'][vid] = var_obj
            
            if category in ['Fish', 'Insects']:
                ret[item_name]['vars']['1'] = {
                    'variation': 'Donated',
                    'have': False,
                    'img': var_obj['img']
                }
    return ret

def update_1_3_0(cat):
    # Missing items
    catalog['wedding dress'] = {
        'type': 'fashion',
        'have': False,
        'vars': {
            '0': {
                'variation': 'N/A',
                'have': False,
                'img': 'https://acnhcdn.com/latest/FtrIcon/TopsTexOnepieceDressNWedding.png'
            }
        },
        'get': 'Cyrus\nWedding Season'
    }

    # 1.3.0 items
    furniture_1_3_0 = [
        ('bamboo grass', 'https://acnhcdn.com/latest/FtrIcon/FtrTanabata.png', 'Crafting\nAll Year'),
        ('mermaid bed', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidBedS.png', 'Crafting\nAll Year'),
        ('mermaid chair', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidChairS.png', 'Crafting\nAll Year'),
        ('mermaid closet', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidClosetLR.png', 'Crafting\nAll Year'),
        ('mermaid dresser', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidChest.png', 'Crafting\nAll Year'),
        ('mermaid lamp', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidLamp.png', 'Crafting\nAll Year'),
        ('mermaid screen', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidScreen.png', 'Crafting\nAll Year'),
        ('mermaid shelf', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidShelf.png', 'Crafting\nAll Year'),
        ('mermaid sofa', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidChairL.png', 'Crafting\nAll Year'),
        ('mermaid table', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidTableM.png', 'Crafting\nAll Year'),
        ('mermaid vanity', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidDresser.png', 'Crafting\nAll Year'),
        ('pirate barrel', 'https://acnhcdn.com/latest/FtrIcon/FtrPirateBarrelSkull.png', 'Gullivarrr\nAll Year'),
        ('pirate ship cannon', 'https://acnhcdn.com/latest/FtrIcon/FtrPirateCannon.png', 'Gullivarrr\nAll Year'),
        ('pirate ship helm', 'https://acnhcdn.com/latest/FtrIcon/FtrPirateWheel.png', 'Gullivarrr\nAll Year'),
        ('pirate treasure chest', 'https://acnhcdn.com/latest/FtrIcon/FtrPirateTreasurechest.png', 'Gullivarrr\nAll Year'),
        ('sideways pirate barrel', 'https://acnhcdn.com/latest/FtrIcon/FtrPirateBarrelSkullSide.png', 'Gullivarrr\nAll Year'),
        ('mermaid wall clock', 'https://acnhcdn.com/latest/FtrIcon/FtrMermaidclockWall.png', 'Crafting\nAll Year')
    ]
    misc_1_3_0 = [
        ('mermaid wall', 'https://acnhcdn.com/latest/FtrIcon/RoomSpWallMermaid00.png', 'Crafting\nAll Year'),
        ('pirate wall', 'https://acnhcdn.com/latest/FtrIcon/RoomSpWallPirates00.png', 'Gullivarrr\nAll Year'),
        ('mermaid flooring', 'https://acnhcdn.com/latest/FtrIcon/RoomSpFloorMermaid00.png', 'Crafting\nAll Year'),
        ('pirate flooring', 'https://acnhcdn.com/latest/FtrIcon/RoomTexFloorPirates00.png', 'Gullivarrr\nAll Year'),
        ('mermaid rug', 'https://acnhcdn.com/latest/FtrIcon/RugOtherMermaidM00.png', 'Crafting\nAll Year'),
        ('pirate rug', 'https://acnhcdn.com/latest/FtrIcon/RugRectPiratesM00.png', 'Gullivarrr\nAll Year')
    ]
    diy_1_3_0 = [
        ('mermaid bed', '', 'Pascal\nAll Year'),
        ('mermaid chair', '', 'Pascal\nAll Year'),
        ('mermaid closet', '', 'Pascal\nAll Year'),
        ('mermaid dresser', '', 'Pascal\nAll Year'),
        ('mermaid flooring', '', 'Pascal\nAll Year'),
        ('mermaid lamp', '', 'Pascal\nAll Year'),
        ('mermaid rug', '', 'Pascal\nAll Year'),
        ('mermaid screen', '', 'Pascal\nAll Year'),
        ('mermaid shelf', '', 'Pascal\nAll Year'),
        ('mermaid sofa', '', 'Pascal\nAll Year'),
        ('mermaid table', '', 'Pascal\nAll Year'),
        ('mermaid vanity', '', 'Pascal\nAll Year'),
        ('mermaid wall', '', 'Pascal\nAll Year'),
        ('mermaid wall clock', '', 'Pascal\nAll Year')
    ]
    for fu in furniture_1_3_0:
        catalog[fu[0]] = {
            'type': 'furniture',
            'have': False,
            'vars': {
                '0': {
                    'variation': 'N/A',
                    'have': False,
                    'img': fu[1]
                }
            },
            'get': fu[2]
        }
    for m in misc_1_3_0:
        catalog[m[0]] = {
            'type': 'misc',
            'have': False,
            'vars': {
                '0': {
                    'variation': 'N/A',
                    'have': False,
                    'img': m[1]
                }
            },
            'get': m[2]
        }
    for d in diy_1_3_0:
        dname = d[0] + ' '
        catalog[dname] = {
            'type': 'diy',
            'have': False,
            'vars': {
                '0': {
                    'variation': 'N/A',
                    'have': False,
                    'img': d[1]
                }
            },
            'get': d[2]
        }

    fashion_1_3_0 = [
        ('sea captains coat', ['Red', 'Blue', 'Black'], 'Gullivarrr\nAll Year', 'TopsTexTopCoatLPirate'),
        ('pirate pants', ['N/A'], 'Gullivarrr\nAll Year', 'BottomsTexPantsNormalPirates'),
        ('mermaid fishy dress', ['Pink', 'Light blue'], 'Pascal\nAll Year', 'TopsTexOnepieceAlongNMermaiddress'),
        ('mermaid princess dress', ['Pink', 'Light blue'], 'Pascal\nAll Year', 'TopsTexOnepieceDressNMermaid'),
        ('pirate dress', ['Red', 'Blue', 'Black'], 'Gullivarrr\nAll Year', 'TopsTexOnepieceBalloonHPirate'),
        ('pirate outfit', ['Red', 'Blue', 'Black'], 'Gullivarrr\nAll Year', 'TopsTexOnepieceOverallHPirates'),
        ('pirate treasure robe', ['N/A'], 'Gullivarrr\nAll Year', 'TopsTexOnepieceAlongLPirates'),
        ('mermaid tiara', ['N/A'], 'Pascal\nAll Year', 'CapOrnamentCMermaid'),
        ('pirate bandanna', ['Red', 'Blue', 'Black'], 'Gullivarrr\nAll Year', 'CapHatPiratesbandana'),
        ('pirate treasure crown', ['N/A'], 'Gullivarrr\nAll Year', 'CapOrnamentCPirate'),
        ('pirates hat', ['N/A'], 'Gullivarrr\nAll Year', 'CapHatPirate'),
        ('nook inc snorkel', ['N/A'], 'Nook Miles Shop\nAll Year', 'AccessoryGlassmouthNook'),
        ('pirate beard', ['N/A'], 'Gullivarrr\nAll Year', 'AccessoryMouthPirates'),
        ('pirate eye patch', ['N/A'], 'Gullivarrr\nAll Year', 'AccessoryGlassPiratespatch'),
        ('snorkel mask', ['Blue', 'Orange', 'Red', 'Pink', 'Green', 'Black'], 'Nintendo, Able Sisters\nSummer', 'AccessoryGlassmouthDiver'),
        ('mermaid shoes', ['Pink', 'Light blue'], 'Pascal\nAll Year', 'ShoesLowcutMermaid'),
        ('pirate boots', ['N/A'], 'Gullivarrr\nAll Year', 'ShoesKneePirates'),
        ('horizontal striped wet suit', ['Red', 'Blue', 'Yellow', 'Black'], 'Nook\'s Cranny\nSummer', 'TopsTexMarinesuitNormalNGreco'),
        ('leaf print wet suit', ['Light blue', 'Purple', 'Yellow', 'Green'], 'Nook Shopping Catalog\nSummer', 'TopsTexMarinesuitNormalLRashguard'),
        ('nook inc wet suit', ['N/A'], 'Nook Miles Shop\nSummer', 'TopsTexMarinesuitNormalLNook0')
    ]
    for fa in fashion_1_3_0:
        catalog[fa[0]] = {
            'type': 'fashion',
            'have': False,
            'vars': {},
            'get': fa[2]
        }
        for i in range(len(fa[1])):
            catalog[fa[0]]['vars'][str(i)] = {
                'variation': fa[1][i],
                'have': False,
                'img': 'https://acnhcdn.com/latest/FtrIcon/' + fa[3] + str(i) + '.png'
            }

    sea_1_3_0 = [
        ('abalone', 'https://acnhcdn.com/latest/MenuIcon/Awabi.png', 'Dive\n'),
        ('acorn barnacle', 'https://acnhcdn.com/latest/MenuIcon/Fujitsubo.png', 'Dive\n'),
        ('chambered nautilus', 'https://acnhcdn.com/latest/MenuIcon/Oumugai.png', 'Dive\n'),
        ('dungeness crab', 'https://acnhcdn.com/latest/MenuIcon/DungenessCrab.png', 'Dive\n'),
        ('firefly squid', 'https://acnhcdn.com/latest/MenuIcon/Hotaruika.png', 'Dive\n'),
        ('flatworm', 'https://acnhcdn.com/latest/MenuIcon/Hiramushi.png', 'Dive\n'),
        ('gazami crab', 'https://acnhcdn.com/latest/MenuIcon/Gazami.png', 'Dive\n'),
        ('giant isopod', 'https://acnhcdn.com/latest/MenuIcon/Daiougusokumushi.png', 'Dive\n'),
        ('gigas giant clam', 'https://acnhcdn.com/latest/MenuIcon/Shakogai.png', 'Dive\n'),
        ('horseshoe crab', 'https://acnhcdn.com/latest/MenuIcon/Kabutogani.png', 'Dive\n'),
        ('lobster', 'https://acnhcdn.com/latest/MenuIcon/Fish54.png', 'Dive\n'),
        ('mantis shrimp', 'https://acnhcdn.com/latest/MenuIcon/Shako.png', 'Dive\n'),
        ('moon jellyfish', 'https://acnhcdn.com/latest/MenuIcon/Mizukurage.png', 'Dive\n'),
        ('mussel', 'https://acnhcdn.com/latest/MenuIcon/Muhrugai.png', 'Dive\n'),
        ('octopus', 'https://acnhcdn.com/latest/MenuIcon/Tako.png', 'Dive\n'),
        ('oyster', 'https://acnhcdn.com/latest/MenuIcon/Kaki.png', 'Dive\n'),
        ('pearl oyster', 'https://acnhcdn.com/latest/MenuIcon/Akoyagai.png', 'Dive\n'),
        ('red king crab', 'https://acnhcdn.com/latest/MenuIcon/Tarabagani.png', 'Dive\n'),
        ('scallop', 'https://acnhcdn.com/latest/MenuIcon/Hotate.png', 'Dive\n'),
        ('sea anemone', 'https://acnhcdn.com/latest/MenuIcon/Isogintyaku.png', 'Dive\n'),
        ('sea cucumber', 'https://acnhcdn.com/latest/MenuIcon/Namako.png', 'Dive\n'),
        ('sea grapes', 'https://acnhcdn.com/latest/MenuIcon/Umibudou.png', 'Dive\n'),
        ('sea pig', 'https://acnhcdn.com/latest/MenuIcon/Senjunamako.png', 'Dive\n'),
        ('sea pineapple', 'https://acnhcdn.com/latest/MenuIcon/Hoya.png', 'Dive\n'),
        ('sea slug', 'https://acnhcdn.com/latest/MenuIcon/Umiushi.png', 'Dive\n'),
        ('sea star', 'https://acnhcdn.com/latest/MenuIcon/Hitode.png', 'Dive\n'),
        ('sea urchin', 'https://acnhcdn.com/latest/MenuIcon/Uni.png', 'Dive\n'),
        ('seaweed', 'https://acnhcdn.com/latest/MenuIcon/Wakame.png', 'Dive\n'),
        ('slate pencil urchin', 'https://acnhcdn.com/latest/MenuIcon/Paipuuni.png', 'Dive\n'),
        ('snow crab', 'https://acnhcdn.com/latest/MenuIcon/Zuwaigani.png', 'Dive\n'),
        ('spider crab', 'https://acnhcdn.com/latest/MenuIcon/Takaashigani.png', 'Dive\n'),
        ('spiny lobster', 'https://acnhcdn.com/latest/MenuIcon/Iseebi.png', 'Dive\n'),
        ('spotted garden eel', 'https://acnhcdn.com/latest/MenuIcon/Chinanago.png', 'Dive\n'),
        ('sweet shrimp', 'https://acnhcdn.com/latest/MenuIcon/Amaebi.png', 'Dive\n'),
        ('tiger prawn', 'https://acnhcdn.com/latest/MenuIcon/Kurumaebi.png', 'Dive\n'),
        ('turban shell', 'https://acnhcdn.com/latest/MenuIcon/Sazae.png', 'Dive\n'),
        ('umbrella octopus', 'https://acnhcdn.com/latest/MenuIcon/Mendako.png', 'Dive\n'),
        ('vampire squid', 'https://acnhcdn.com/latest/MenuIcon/Koumoridako.png', 'Dive\n'),
        ('venus flower basket', 'https://acnhcdn.com/latest/MenuIcon/Kairoudouketsu.png', 'Dive\n'),
        ('whelk', 'https://acnhcdn.com/latest/MenuIcon/Baigai.png', 'Dive\n')
    ]
    for s in sea_1_3_0:
        cat[s[0]] = {
            'type': 'sea',
            'have': False,
            'vars': {
                '0': {
                    'variation': 'Caught',
                    'have': False,
                    'img': s[1]
                },
                '1': {
                    'variation': 'Donated',
                    'have': False,
                    'img': s[1]
                }
            },
            'get': s[2]
        }
    
    return cat

furniture = get_items('furniture', FURNITURE_CATEGORIES)
fashion = get_items('fashion', FASHION_CATEGORIES)
misc = get_items('misc', MISC_CATEGORIES)
diy = get_items('diy', [DIY_CATEGORY])
fish = get_items('fish', [FISH_CATEGORY])
bugs = get_items('bugs', [BUG_CATEGORY])

catalog = dict(**furniture, **fashion, **misc, **diy, **fish, **bugs)

catalog = update_1_3_0(cat=catalog)

content = {
    'version': 2,
    'catalog': catalog
}

with open(CATALOG_FILENAME, 'w') as f:
    json.dump(content, f, separators=(',', ':'))

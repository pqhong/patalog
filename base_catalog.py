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
BASE_URL = 'https://acnh.tnrd.net/api/v3/'


def get_items(type, categories):
    ret = dict()
    for category in categories:
        print('Getting category: {0}'.format(category))
        api_url = BASE_URL + category
        res = requests.get(api_url)
        items = res.json()
        for item in items:
            item_name = item['name'].lower().replace('.', '')
            if category == 'Recipes':
                item_name += ' '
            if category == 'Art':
                variation = 'Real' if item['genuine'] else 'Fake'
            elif category in ['Umbrellas', 'Floors', 'Music', 'Rugs', 'Wallpapers', 'Recipes']:
                variation = 'N/A'
            else:
                variation = item['variation']
            if variation == 'NA':
                variation = 'N/A'
            if item_name not in ret.keys():
                ret[item_name] = {
                    'type': type,
                    'have': False,
                    'vars': {variation: False}
                }
            else:
                ret[item_name]['vars'][variation] = False
    return ret

furniture = get_items('furniture', FURNITURE_CATEGORIES)
fashion = get_items('fashion', FASHION_CATEGORIES)
misc = get_items('misc', MISC_CATEGORIES)
diy = get_items('diy', [DIY_CATEGORY])

catalog = dict(**furniture, **fashion, **misc, **diy)

with open(CATALOG_FILENAME, 'w') as f:
    json.dump(catalog, f, separators=(',', ':'))

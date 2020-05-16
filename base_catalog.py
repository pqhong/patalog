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
    'Floor',
    'Music',
    'Rugs',
    'Wallpaper'
]
BASE_URL = 'https://acnh.tnrd.net/api/v1/'


def get_items(type, categories):
    ret = dict()
    for category in categories:
        print('Getting category: {0}'.format(category))
        api_url = BASE_URL + category
        res = requests.get(api_url)
        items = res.json()
        for item in items:
            item_name = item['name']
            if category == 'Art':
                variation = 'Real' if item['isGenuine'] else 'Fake'
            elif category in ['Umbrellas', 'Floor', 'Music', 'Rugs', 'Wallpaper']:
                variation = 'N/A'
            else:
                variation = item['variation']
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

catalog = dict(**furniture, **fashion, **misc)

with open(CATALOG_FILENAME, 'w') as f:
    json.dump(catalog, f, separators=(',', ':'))

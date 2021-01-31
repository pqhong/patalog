import argparse
import copy
import json

import update_1_4_0
import update_1_5_0
import update_1_6_0
import update_1_7_0


CATALOG_FILENAME = 'src/catalog.json'

def perform():
    with open(CATALOG_FILENAME, 'r') as f:
        catalog = json.load(f)

    update_catalog = copy.deepcopy(catalog)
    version = update_catalog['version']

    if version < 6:
        cat = copy.deepcopy(update_catalog)
        update_catalog = update_1_4_0.perform(cat)

    if version < 7:
        cat = copy.deepcopy(update_catalog)
        update_catalog = update_1_5_0.perform(cat)

    if version < 8:
        cat = copy.deepcopy(update_catalog)
        update_catalog = update_1_6_0.perform(cat)

    if version < 9:
        cat = copy.deepcopy(update_catalog)
        update_catalog = update_1_7_0.perform(cat)

    with open(CATALOG_FILENAME, 'w') as f:
        json.dump(update_catalog, f, separators=(',', ':'))


def main():
    perform()

if __name__ == '__main__':
    main()

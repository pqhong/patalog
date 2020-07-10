import argparse
import copy
import json


CATALOG_FILENAME = 'catalog.json'

def perform(filename, updates=[]):
    with open(CATALOG_FILENAME, 'r') as f:
        catalog = json.load(f)

    with open(filename, 'r') as f:
        cat = json.load(f)
    
    if '1' in updates:
        catalog['catalog'] = perform1(old_catalog=cat, new_catalog=catalog['catalog'])

    with open(filename, 'w') as f:
        json.dump(catalog, f, separators=(',', ':'))

def perform1(old_catalog, new_catalog):
    for item_name in old_catalog.keys():
        new_catalog[item_name]['have'] = old_catalog[item_name]['have']
        for var in old_catalog[item_name]['vars'].keys():
            for vid in new_catalog[item_name]['vars'].keys():
                if new_catalog[item_name]['vars'][vid]['variation'] == var:
                    new_catalog[item_name]['vars'][vid]['have'] = old_catalog[item_name]['vars'][var]
    return new_catalog

def perform2(old_catalog):
    return old_catalog

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, dest='filename', required=True, help='catalog file to be updated')
    parser.add_argument('-1', action='store_true', dest='update1', required=False, help='perform update 1')
    return parser.parse_args()

def main():
    args = parse_args()
    updates = []
    if args.update1:
        updates.append('1')
    perform(filename=args.filename, updates=updates)

if __name__ == '__main__':
    main()

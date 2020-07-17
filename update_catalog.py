import argparse
import copy
import json


CATALOG_FILENAME = 'catalog.json'

def perform(filename, updates=[]):
    with open(CATALOG_FILENAME, 'r') as f:
        catalog = json.load(f)

    with open(filename, 'r') as f:
        cat = json.load(f)

    new_catalog = catalog
    
    if '1' in updates:
        new_catalog['catalog'] = perform1(old_catalog=cat, new_catalog=new_catalog['catalog'])
    
    if '2' in updates:
        new_catalog['catalog'] = perform2(old_catalog=new_catalog['catalog'], new_catalog=catalog['catalog'])

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

def perform2(old_catalog, new_catalog):
    for vid in old_catalog['frying pan']['vars']:
        if old_catalog['frying pan']['vars'][vid]['variation'] == 'Veggie saut\u00e9':
            old_catalog['frying pan']['vars'][vid]['variation'] = 'Veggie saute'
    for vid in old_catalog['exit sign']['vars']:
        if old_catalog['exit sign']['vars'][vid]['variation'] == '\u2190 \u2192':
            old_catalog['exit sign']['vars'][vid]['variation'] = '< >'
        if old_catalog['exit sign']['vars'][vid]['variation'] == '\u2190':
            old_catalog['exit sign']['vars'][vid]['variation'] = '<'
        if old_catalog['exit sign']['vars'][vid]['variation'] == '\u2192':
            old_catalog['exit sign']['vars'][vid]['variation'] = '>'
    return perform1(old_catalog=old_catalog, new_catalog=new_catalog)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, dest='filename', required=True, help='catalog file to be updated')
    parser.add_argument('-1', action='store_true', dest='update1', required=False, help='perform update 1')
    parser.add_argument('-2', action='store_true', dest='update2', required=False, help='perform update 2')
    return parser.parse_args()

def main():
    args = parse_args()
    updates = []
    if args.update1:
        updates.append('1')
    if args.update2:
        updates.append('2')
    perform(filename=args.filename, updates=updates)

if __name__ == '__main__':
    main()

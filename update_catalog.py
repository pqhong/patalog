import argparse
import copy
import json


CATALOG_FILENAME = 'catalog.json'

def perform(filename):
    with open(CATALOG_FILENAME, 'r') as f:
        catalog = json.load(f)

    with open(filename, 'r') as f:
        cat = json.load(f)
    
    for item_name in cat.keys():
        catalog[item_name]['have'] = cat[item_name]['have']
        for var in cat[item_name]['vars'].keys():
            for vid in catalog[item_name]['vars'].keys():
                if catalog[item_name]['vars'][vid]['variation'] == var:
                    catalog[item_name]['vars'][vid]['have'] = cat[item_name]['vars'][var]

    with open(CATALOG_FILENAME, 'w') as f:
        json.dump(catalog, f, separators=(',', ':'))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='filename', required=True, help='catalog file to be updated')
    return parser.parse_args()

def main():
    args = parse_args()
    perform(filename=args.filename)

if __name__ == '__main__':
    main()

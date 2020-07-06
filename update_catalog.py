import json


CATALOG_FILENAME = 'catalog.json'

with open(CATALOG_FILENAME, 'r') as f:
    catalog = json.load(f)

new_catalog = dict()
for item_name in catalog.keys():
    if item_name in ['writing chair', 'writing desk', 'writing poster']:  # Not sure when this happened, might be 1.3.0
        new_name = item_name.replace('writing', 'study')
    else:
        new_name = item_name.replace('.', '').replace('-', ' ').replace('\'', '')
    new_catalog[new_name] = catalog[item_name]

# Missing items
new_catalog['wedding dress'] = {
    'type': 'fashion',
    'have': False,
    'vars': {
        'N/A': False
    }
}

# 1.3.0 items
new_furniture = [
    'bamboo grass',
    'mermaid bed',
    'mermaid chair',
    'mermaid closet',
    'mermaid dresser',
    'mermaid lamp',
    'mermaid screen',
    'mermaid shelf',
    'mermaid sofa',
    'mermaid table',
    'mermaid vanity',
    'pirate barrel',
    'pirate ship cannon',
    'pirate ship helm',
    'pirate treasure chest',
    'sideways pirate barrel',
    'mermaid wall clock'
]
new_misc = [
    'mermaid wall',
    'pirate wall',
    'mermaid flooring',
    'pirate flooring',
    'mermaid rug',
    'pirate rug'
]
new_diy = [
    'mermaid bed',
    'mermaid chair',
    'mermaid closet',
    'mermaid dresser',
    'mermaid flooring',
    'mermaid lamp',
    'mermaid rug',
    'mermaid screen',
    'mermaid shelf',
    'mermaid sofa',
    'mermaid table',
    'mermaid vanity',
    'mermaid wall',
    'mermaid wall clock'
]
for furniture in new_furniture:
    new_catalog[furniture] = {
        'type': 'furniture',
        'have': False,
        'vars': {
            'N/A': False
        }
    }
for misc in new_misc:
    new_catalog[misc] = {
        'type': 'misc',
        'have': False,
        'vars': {
            'N/A': False
        }
    }
for diy in new_diy:
    new_catalog[diy] = {
        'type': 'diy',
        'have': False,
        'vars': {
            'N/A': False
        }
    }

new_fashion = [
    ('sea captains coat', ['Black', 'Red', 'Blue']),
    ('pirate pants', ['N/A']),
    ('mermaid fishy dress', ['Pink', 'Light blue']),
    ('mermaid princess dress', ['Pink', 'Light blue']),
    ('pirate dress', ['Black', 'Red', 'Blue']),
    ('pirate outfit', ['Black', 'Red', 'Blue']),
    ('pirate treasure robe', ['N/A']),
    ('mermaid tiara', ['N/A']),
    ('pirate bandanna', ['Black', 'Red', 'Blue']),
    ('pirate treasure crown', ['N/A']),
    ('pirates hat', ['N/A']),
    ('nook inc snorkel', ['N/A']),
    ('pirate beard', ['N/A']),
    ('pirate eye patch', ['N/A']),
    ('snorkel mask', ['Black', 'Red', 'Pink', 'Orange', 'Green', 'Blue']),
    ('mermaid shoes', ['Pink', 'Light blue']),
    ('pirate boots', ['N/A']),
    ('horizontal striped wet suit', ['Black', 'Red', 'Yellow', 'Blue']),
    ('leaf print wet suit', ['Yellow', 'Green', 'Light blue', 'Purple']),
    ('nook inc wet suit', ['N/A'])
]
for fashion in new_fashion:
    new_catalog[fashion[0]] = {
        'type': 'fashion',
        'have': False,
        'vars': {}
    }
    for variation in fashion[1]:
        new_catalog[fashion[0]]['vars'][variation] = False

with open(CATALOG_FILENAME, 'w') as f:
    json.dump(new_catalog, f, separators=(',', ':'))

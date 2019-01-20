BASIC_ATTRS = ('rank', 'name')
SHARES = ('jobbing_pirate', 'cabin_person', 'pirate', 'officer', 'fleet_officer', 'senior_officer', 'captain')
RANKS = ['Captain', 'Senior Officer', 'Fleet Officer', 'Officer', 'Pirate', 'Cabin Person', 'Jobbing Pirate']

ULTIMATE_MAPPINGS = {
    'piracy': {
        'swordfighting': 0,
        'bilging': 2,
        'sailing': 3,
        'rigging': 31,
        'navigating': 4,
        'battle_navigation': 29,
        'gunning': 5,
        'carpentry': 6,
        'rumble': 27,
        'treasure_haul': 30,
        'patching': 32,
    },
    'crafting': {
        'distilling': 14,
        'alchemistry': 18,
        'shipwrightery': 16,
        'blacksmithing': 15,
        'foraging': 12,
        'weaving': 13,
    },
    'carousing': {
        'drinking': 1,
        'spades': 21,
        'hearts': 24,
        'treasure_drop': 25,
        'poker': 26
    }
}

def clean_stat(data):
    stats = data.split('  ')
    left_side = stats[0].split('/')
    experience = left_side[0]
    standing = {'ocean_wide': left_side[1]}
    if len(stats) == 2:
        right_side = stats[1].replace('(archipelago:\xa0', '').replace(')', '')
        standing['archipelago'] = right_side
    else:
        standing['archipelago'] = left_side[1]

    return experience, standing

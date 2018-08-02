from yoweb.helpers import clean_stat, BASIC_ATTRS


class Affiliations(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data
        self.crew = Crew(self._data, self.name)
        self.flag = Flag(self._data, self.name)
        self.navy = Navy(self._data, self.name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Carousing(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data[1]
        skills = ('drinking', 'spades', 'hearts', 'treasure_drop', 'poker')
        for skill, order in zip(skills, range(0, len(skills))):
            setattr(self, skill, Statistics(self._data[order], self.name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Crafting(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data[1]
        skills = ('distilling', 'alchemistry', 'shipwrighting', 'blacksmithing', 'foraging', 'weaving')

        for skill, order in zip(skills, range(0, len(skills))):
            setattr(self, skill, Statistics(self._data[order], self.name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Crew(object):
    default = 'Independent Pirate'

    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data
        if self._data[0] == self.default:
            for basic in BASIC_ATTRS:
                setattr(self, basic, self.default)
        else:
            for basic, order in zip(BASIC_ATTRS, range(0, len(self._data[0].split(' of the crew ')))):
                setattr(self, basic, self._data[order].split(' of the crew '))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Familiars(object):
    default = 'None'

    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data



class Flag(object):
    default = 'Independent Pirate'

    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data
        if self._data[0] == self.default:
            for basic in BASIC_ATTRS:
                setattr(self, basic, self.default)
        else:
            for basic, order in zip(BASIC_ATTRS, range(0, len(self._data[0].split(' of the flag ')))):
                setattr(self, basic, self._data[order].split(' of the flag '))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Navy(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data[2].split(' in the ')
        for basic, order in zip(BASIC_ATTRS, range(0, len(self._data))):
            setattr(self, basic, self._data[order])
        self.archipelago = self._data[2]

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Piracy(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data[1]
        skills = ('sailing', 'rigging', 'carpentry', 'patching', 'bilging', 'gunnery', 'treasure_haul',
                  'duty_navigation', 'battle_navigation', 'swordfighting', 'rumble')
        for skill, order in zip(skills, range(0, len(skills))):
            setattr(self, skill, Statistics(self._data[order], self.name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Reputations(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data
        reputations = ('conqueror', 'explorer', 'patron', 'magnate')
        for reputation, order in zip(reputations, range(0, len(reputations))):
            setattr(self, reputation, self._data[order])

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Skills(object):
    def __init__(self, data, pirate):
        self.name = pirate
        self._data = data
        self.piracy = Piracy(self._data[9], self.name)
        self.carousing = Carousing(self._data[10], self.name)
        self.crafting = Crafting(self._data[11], self.name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Statistics(object):
    def __init__(self, data, pirate):
        self.name = pirate
        experience, standing = clean_stat(data)
        self.experience = experience
        self.ocean_wide = standing['ocean_wide']
        self.archipelago = standing['archipelago']

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)

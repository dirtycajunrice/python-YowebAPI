from yoweb.helpers import clean_stat, BASIC_ATTRS


class Affiliations(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        self.crew = Crew(self._data, self._name)
        self.flag = Flag(self._data, self._name)
        self.navy = Navy(self._data, self._name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Carousing(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        skills = ('drinking', 'spades', 'hearts', 'treasure_drop', 'poker')
        for skill, order in zip(skills,  self._data.index.values):
            setattr(self, skill, Statistics(self._data[order], self._name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Crafting(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        skills = ('distilling', 'alchemistry', 'shipwrighting', 'blacksmithing', 'foraging', 'weaving')

        for skill, order in zip(skills,  self._data.index.values):
            setattr(self, skill, Statistics(self._data[order], self._name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Crew(object):
    _default = 'Independent Pirate'

    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        if self._data[0] == self._default:
            for basic in BASIC_ATTRS:
                setattr(self, basic, self._default)
        else:
            for basic, order in zip(BASIC_ATTRS, range(0, len(self._data[0].split(' of the crew ')))):
                setattr(self, basic, self._data[0].split(' of the crew ')[order])

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Familiars(object):

    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        self.list = None
        if self._data is not None:
            self.list = self._data.split('  Hearties  ')[0].split('Familiars  ')[1].split('  ')

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Flag(object):
    _default = 'Independent Pirate'

    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        if self._data[1] == self._default:
            for basic in BASIC_ATTRS:
                setattr(self, basic, self._default)
        elif len(self._data) < 3:
            for basic in BASIC_ATTRS:
                setattr(self, basic, None)
        else:
            for basic, order in zip(BASIC_ATTRS, range(0, len(self._data[1].split(' of the flag ')))):
                setattr(self, basic, self._data[1].split(' of the flag ')[order])

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Hearties(object):

    def __init__(self, data, pirate, oceanobj):
        self._name = pirate
        self._data = data
        self.list = None
        if self._data is not None:
            hearty_list = self._data.split('Hearties  ')[1].split(', ')
            self.list = [oceanobj.getpirate(h) for h in hearty_list]

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Navy(object):
    _default = 'Independent Pirate'

    def __init__(self, data, pirate):
        self._name = pirate
        if data[0] == self._default or len(data) < 3:
            self._data = data[1].split(' in the ')
        else:
            self._data = data[2].split(' in the ')
        for order, basic in enumerate(BASIC_ATTRS):
            setattr(self, basic, self._data[order])
        self.archipelago = self._data[2]

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Piracy(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        skills = ('sailing', 'rigging', 'carpentry', 'patching', 'bilging', 'gunnery', 'treasure_haul',
                  'duty_navigation', 'battle_navigation', 'swordfighting', 'rumble')
        for skill, order in zip(skills, self._data.index.values):
            setattr(self, skill, Statistics(self._data[order], self._name))

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Reputations(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        reputations = ('conqueror', 'explorer', 'patron', 'magnate')
        for order, reputation in enumerate(reputations):
            setattr(self, reputation, self._data[order])

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Skills(object):
    def __init__(self, data, pirate):
        self._name = pirate
        self._data = data
        self.piracy = Piracy(self._data[0][1][-31:-20], self._name)
        self.carousing = Carousing(self._data[0][1][-16:-11], self._name)
        self.crafting = Crafting(self._data[0][1][-7:-1], self._name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)


class Statistics(object):
    def __init__(self, data, pirate):
        self._name = pirate
        experience, standing = clean_stat(data)
        self.experience = experience
        self.ocean_wide = standing['ocean_wide']
        self.archipelago = standing['archipelago']

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self._name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)

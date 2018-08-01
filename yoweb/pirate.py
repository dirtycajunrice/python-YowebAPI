class Affiliations(object):
    def __init__(self, data):
        self._data = data
        self.crew = Crew(self._data)
        self.flag = Flag(self._data)
        self.navy = Navy(self._data)
    def __repr__(self):
        complete = {
            'crew': self.crew,
            'flag': self.flag,
            'navy': self.navy
        }
        return repr(complete)

class Reputations(object):
    def __init__(self, data):
        self._data = data
        self.conqueror = self._data[0]
        self.explorer = self._data[1]
        self.patron = self._data[2]
        self.magnate = self._data[3]
    def __repr__(self):
        complete = {
            'conqueror': self.conqueror,
            'explorer': self.explorer,
            'patron': self.patron,
            'magnate': self.magnate
        }
        return repr(complete)

class Crew(object):
    default = 'Independent Pirate'
    def __init__(self, data):
        self._data = data
        if self._data[0] == self.default:
            self.rank = self.default
            self.name = self.default
        else:
            self.rank = self._data[0].split(' of the crew ')[0]
            self.name = self._data[0].split(' of the crew ')[1]
    def __repr__(self):
        complete = {
            'rank': self.rank,
            'name': self.name
        }
        return repr(complete)

class Flag(object):
    default = 'Independent Pirate'
    def __init__(self, data):
        self._data = data
        if self._data[0] == self.default:
            self.rank = self.default
            self.name = self.default
        else:
            self.rank = self._data[1].split(' of the flag ')[0]
            self.name = self._data[1].split(' of the flag ')[1]
    def __repr__(self):
        complete = {
            'rank': self.rank,
            'name': self.name
        }
        return repr(complete)

class Navy(object):
    def __init__(self, data):
        self._data = data[2].split(' in the ')
        self.rank = self._data[0]
        self.name = self._data[1]
        self.archipelago = self._data[2]
    def __repr__(self):
        complete = {
            'rank': self.rank,
            'name': self.name,
            'archipelago': self.archipelago
        }
        return repr(complete)
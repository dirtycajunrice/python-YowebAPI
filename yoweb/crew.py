from datetime import datetime

from yoweb.helpers import SHARES


class BootyShares(object):
    def __init__(self, data, sharetype, name):
        self._name = name
        self._data = data
        self.type = sharetype
        for order, share in enumerate(SHARES):
            share_amount = str(self._data[order]).replace('\xa0', ' ')
            setattr(self, share, share_amount)

    def __repr__(self):
        name = self.__class__.__name__
        crewid = self._name
        return "<{name}:{crewid}>".format(name=name, crewid=crewid)


class ActiveMates(object):
    def __init__(self, data, name):
        self._name = name
        self._data = data

        for count, rank in enumerate(self._data[0]):
            if rank == 'Jobbing Pirate:':
                self.jobbing_pirate = self._data[1][count]
            elif rank == 'Cabin Person:':
                self.cabin_person = self._data[1][count]
            elif rank == 'Pirate:':
                self.pirate = self._data[1][count]
            elif rank == 'Officer:':
                self.officer = self._data[1][count]
            elif rank == 'Fleet Officer:':
                self.fleet_officer = self._data[1][count]
            elif rank == 'Senior Officer:':
                self.senior_officer = self._data[1][count]
            elif rank == 'Captain:':
                self.captain = self._data[1][count]

    def __repr__(self):
        name = self.__class__.__name__
        crewid = self._name
        return "<{name}:{crewid}>".format(name=name, crewid=crewid)

class Affiliations(object):
    def __init__(self, data, name):
        self._name = name
        self._data = data
        self.flag = None
        self.public_statement = None

        if 'flag' in self._data:
            self.flag = self._data.split('  of the flag  ')[0]
        if 'Public Statement' in self._data:
            self.public_statement = self._data.split('  Public Statement  ')[1]
        founded_date_str = self._data.split(' Founded in the year ')[1].split('  ')[0].split(' ')
        self.founded = datetime.strptime(founded_date_str, "%Y on %B %d").date()
        fame_data = self._data.split(founded_date_str)[1].split('  ')[1].split(' of ')
        self.crew_rank = fame_data[0]
        self.fame = fame_data[1]

    def __repr__(self):
        name = self.__class__.__name__
        crewid = self._name
        return "<{name}:{crewid}>".format(name=name, crewid=crewid)

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

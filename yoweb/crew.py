from datetime import datetime
import numpy as np
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


class CrewAffiliations(object):
    def __init__(self, data, name):
        self._name = name
        self._data = data
        self.flag = None
        self.public_statement = None

        if 'flag' in self._data:
            self.flag = self._data.split('  of the flag  ')[1].split('  Founded')[0]
        if 'Public Statement' in self._data:
            self.public_statement = self._data.split('  Public Statement  ')[1]
        founded_date_str = self._data.split(' Founded in the year ')[1].split('  ')[0]
        self.founded = datetime.strptime(founded_date_str, "%Y on %B %d").date()
        fame_data = self._data.split(founded_date_str)[1].split('  ')[1].split(' of ')
        self.rank = fame_data[0]
        self.fame = fame_data[1]

    def __repr__(self):
        name = self.__class__.__name__
        crewid = self._name
        return "<{name}:{crewid}>".format(name=name, crewid=crewid)


class CrewMembers(object):
    def __init__(self, data, name, oceanobj):
        self._name = name
        self._data = data
        self._oceanobj = oceanobj
        self._data.drop(self._data.columns[3], axis=1, inplace=True)
        member_dfs = np.split(self._data, self._data[self._data.isnull().all(1)].index)

        for member_df in member_dfs:
            member_df.dropna(how='all', inplace=True)
            if member_df.empty:
                continue
            title = str(member_df[1][member_df.index.values[1]]).lower().replace(' ', '_')
            member_df.drop(member_df.index[:2], inplace=True)
            members = [self._oceanobj.getpirate(column) for index, row in
                       member_df.iterrows() for column in row if str(column) != 'nan']
            setattr(self, title, members)

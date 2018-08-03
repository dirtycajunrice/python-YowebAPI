import pandas
from yoweb.pirate import Affiliations, Reputations, Skills, Hearties, Familiars
from yoweb.crew import BootyShares, ActiveMates, CrewAffiliations, CrewMembers

class Ocean(object):
    """ Base class for all Yoweb objects
        Parameters:
            ocean (:str:`yoweb.base.Ocean`): Ocean this client is connected to
    """
    key = None

    def __init__(self, ocean):
        self._initpath = 'http://ocean.puzzlepirates.com/yoweb/'
        self._ocean = self.ocean(ocean)

    def ocean(self, ocean):
        self._initpath = self._initpath.replace('ocean', ocean)
        if ocean is None:
            self._notimplemented()
        return ocean

    def getpirate(self, name):
        pirate = Pirate(name, self._initpath, self)
        return pirate

    def getcrew(self, crewid):
        crew = Crew(crewid, self._initpath, self)
        return crew

    def _notimplemented(self):
        raise NotImplementedError('Abstract method not implemented.')

    def __repr__(self):
        name = self.__class__.__name__
        ocean = self._ocean
        return "<{name}:{ocean}>".format(name=name, ocean=ocean)


class Pirate(object):
    """ Pirate class object to manipulate pirate page data
        Parameters:
            name (:str:`yoweb.base.Pirate`): Pirates in-game name
            initpath (:str:`yoweb.base.Ocean`): base path to yoweb
    """
    def __init__(self, name, initpath, oceanobj):
        self.name = name
        self._initpath = initpath
        self._path = initpath + 'pirate.wm?classic=$classic&target={pirate}'.format(pirate=self.name)
        self._data = None
        self._oceanobj = oceanobj

    def __getattr__(self, item):
        if not self._data:
            self._loaddata(self._path)
        return self.__getattribute__(item)

    def _loaddata(self, path):
        data = pandas.read_html(path)
        self._data = data
        familiars_data, hearties_data = None, None
        affiliation_data = self._data[0][2][0].split('  ')
        reputation_data = self._data[3][1]

        for row in self._data[0][0][1:]:
            if 'Hearties' in str(row):
                hearties_data = str(row)
            if 'Familiars' in str(row):
                familiars_data = str(row)

        self.affiliations = Affiliations(affiliation_data, self.name)
        self.reputations = Reputations(reputation_data, self.name)
        self.skills = Skills(self._data, self.name)
        self.hearties = Hearties(hearties_data, self.name, self._oceanobj)
        self.familiars = Familiars(familiars_data, self.name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)

class Crew(object):
    def __init__(self, crewid, initpath, oceanobj):
        self.crewid = crewid
        self._initpath = initpath
        self._oceanobj = oceanobj
        self._path = initpath + 'crew/info.wm?crewid={crewid}&classic=false'.format(crewid=self.crewid)
        self._data = None

    def __getattr__(self, item):
        if not self._data:
            self._loaddata(self._path)
        return self.__getattribute__(item)

    def _loaddata(self, path):
        data = pandas.read_html(path)
        self._data = data

        crew_affiliation_data = self._data[0][0][0]
        reputation_data = self._data[4][1]
        bootyshare_data = self._data[5][1]
        activemate_data = self._data[6]
        third_frame = self._data[3][2][12]
        bootyshare_type = third_frame.split('shares: ')[1].split('  ')[0]
        member_data = self._data[8]

        if 'flag' in crew_affiliation_data:
            self.name = crew_affiliation_data.split('  of the flag  ')[0]
        else:
            self.name = crew_affiliation_data.split('  Founded')[0]

        self.politics = third_frame.split('  Booty')[0].split(': ')[1]
        self.ship_restocking = third_frame.split('  Ship restocking:\xa0')[1].split('  Active')[0].replace('\xa0','')

        self.affiliations = CrewAffiliations(crew_affiliation_data, self.name)
        self.reputations = Reputations(reputation_data, self.name)
        self.booty_shares = BootyShares(bootyshare_data, bootyshare_type, self.name)
        self.active_mates = ActiveMates(activemate_data, self.name)
        self.members = CrewMembers(member_data, self.name, self._oceanobj)

    def __repr__(self):
        name = self.__class__.__name__
        crewid = self.crewid
        return "<{name}:{crewid}>".format(name=name, crewid=crewid)
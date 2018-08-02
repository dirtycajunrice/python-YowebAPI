import attr
import pandas
from yoweb.pirate import Affiliations, Reputations, Skills


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
        pirate = Pirate(name, self._initpath)
        return pirate

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
    # Classes/attrs left to implement
    # Center Column
    pictures = None
    trophies = None
    # Left Column
    buildings = None
    familiars = None
    hearties = None

    def __init__(self, name, initpath):
        self.name = name
        self._initpath = initpath
        self._path = initpath + 'pirate.wm?classic=$classic&target={pirate}'.format(pirate=self.name)
        self._data = self._loaddata(self._path)
        self._setdata()

    def _loaddata(self, path):
        data = pandas.read_html(path)
        return data

    def _setdata(self):
        affiliation_data = self._data[0][2][0].split('  ')
        reputation_data = self._data[3][1]
        self.affiliations = Affiliations(affiliation_data, self.name)
        self.reputations = Reputations(reputation_data, self.name)
        self.skills = Skills(self._data, self.name)

    def __repr__(self):
        name = self.__class__.__name__
        pirate = self.name
        return "<{name}:{pirate}>".format(name=name, pirate=pirate)



class TaxRates(object):
    def __init__(self, name, path, data):
        self._name = name
        self._path = path
        self._data = data
        labor_data = self._data[2]
        commodity_data = self._data[1]

        self.labor = LaborTax(self._name, labor_data)
        self.commodity = CommodityTax(self._name, commodity_data)

    def __repr__(self):
        name = self.__class__.__name__
        ocean = self._name
        return "<{ocean}:{name}>".format(name=name, ocean=ocean)


class LaborTax(object):
    def __init__(self, name, data):
        self._name = name
        self._data = data

        for row in self._data[1:].iterrows():
            labor_type = str(row[1][0]).lower().replace(' ', '_')
            amount = float(row[1][1])
            setattr(self, labor_type, amount)

    def __repr__(self):
        name = self.__class__.__name__
        ocean = self._name
        return "<{ocean}:{name}>".format(name=name, ocean=ocean)


class CommodityTax(object):
    def __init__(self, name, data):
        self._name = name
        self._data = data

        for row in self._data[1:].iterrows():
            commodity_type = str(row[1][0]).lower().replace(' ', '_')
            amount = float(row[1][1])
            setattr(self, commodity_type, amount)

    def __repr__(self):
        name = self.__class__.__name__
        ocean = self._name
        return "<{ocean}:{name}>".format(name=name, ocean=ocean)

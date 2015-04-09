__author__ = 'Yih-Yoon Lee'
#

class Bicycle(object):
    def __init__(self, bikeDetail):
        self.bikeDetail = {'Madone': 150, 'Lexa': 400, 'Silque': 1000, 'FX': 1500, 'CrossRip': 4500, 'Tandem': 8000}

    def weight(self, bikeWeight):
        self.bikeWeight = bikeWeight


class Shop(object):
    def name(self, shopName):
        self.shopName = shopName

    def inventory(self, bikeList):
        self.bikeList = bikeList

    def sale(self, totalSale):
        self.totalsale = totalSale

    def profit(self, totalProfit):
        self.totalProfit = totalProfit


class Customer(object):
    def name(self, customerName):
        self.customerName = customerName

    def fund(self, availMoney):
        self.availMoney = availMoney

    def buyBike(self, buy):
        self.buy = buy


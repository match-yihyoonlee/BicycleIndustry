__author__ = 'Yih-Yoon Lee'
#

class Bicycle(object):
    def __init__(self, bikeDetail, bikeWeight):
        self.bikeDetail = {
            'Madone': [150, 100],
            'Lexa': [400, 90],
            'Silque': [1000, 80],
            'FX': [1500, 75],
            'CrossRip': [4500, 60],
            'Tandem': [8000, 55]
        }
        self.bikeWeight = {'Madone'}


class Shop(object):
    def name(self, shopName):
        self.shopName = shopName

    def inventory(self, bikeList):
        self.bikeList = bikeList

    def sale(self, totalSale):
        self.totalSale = totalSale

    def profit(self, totalProfit):
        self.totalProfit = totalProfit


class Customer(object):
    def name(self, customerName):
        self.customerName = customerName

    def fund(self, availMoney):
        self.availMoney = availMoney

    def buyBike(self, buy):
        self.buy = buy



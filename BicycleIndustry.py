__author__ = 'Yih-Yoon Lee'
#

class Bicycle(object):
    def __init__(self, bikeDetail, bikeWeight):
        self.bikeDetail = {
            'Madone': [150, 100],
            'Lexa': [400, 90],
            'Silque': [1000, 80],
            'FX': [1500, 70],
            'CrossRip': [4500, 65],
            'Tandem': [8000, 55]
        }


class Shop(object):
    def name(self, shopName):
        self.shopName = shopName

    def inventory(self, bikeList):
        self.bikeList = bikeList

    def sale(self, totalSale):
        self.totalSale = totalSale

    def profit(self, totalProfit):
        self.totalProfit = totalProfit


class Customer:
    def __init__(self, customerName, availMoney, buy='Y'):
        self.customerName = customerName
        self.availMoney = availMoney
        self.buy = buy


FriscoBikeMart = Shop()
FriscoBikeMart.shopName = 'Fisco Bike\'s Mart'
FriscoBikeMart.inventory = {'Madone': 5, 'Lexa': 3, 'Silque': 5, 'FX': 2, 'CrossRip': 1, 'Tandem': 1}

Lee = Customer('Yih-Yoon Lee', 200, 'Y')
Chia = Customer('Chia-Hwa Chang', 500, 'Y')
Joseph = Customer('Joseph Tan', 1000, 'Y')






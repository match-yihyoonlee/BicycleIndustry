__author__ = 'Yih-Yoon Lee'
# 'Madone': [150, 100],
# 'Lexa': [400, 90],
#            'Silque': [1000, 80],
#           'FX': [1500, 70],
#           'CrossRip': [4500, 65],
#           'Tandem': [8000, 55]

class Bicycle(object):
    def modelName_(self, modelName):
        self.modelName = modelName

    def weight(self, weight):
        self.weight = weight

    def bikeCost(self, bikeCost):
        self.bikeCost = bikeCost


class Shop(object):
    def name(self, shopName):
        self.shopName = shopName

    def inventory(self, bikeList):
        self.bikeList = bikeList

    def sale(self, saleMargin):
        self.saleMargin = saleMargin

    def profit(self, totalProfit):
        self.totalProfit = totalProfit


class Customer(object):
    def customerName(self, customerName):
        self.customerName = customerName
    def availMoney(self, availMoney):
        self.availMoney = availMoney
    def bikeOwn(self, bikeOwn):
        self.bikeOwn = bikeOwn


def main():
    FriscoBikeMart = Shop()
    FriscoBikeMart.shopName = 'Fisco Bike\'s Mart'
    FriscoBikeMart.inventory = {'Madone': 5, 'Lexa': 3, 'Silque': 5, 'FX': 2, 'CrossRip': 1, 'Tandem': 1}
    FriscoBikeMart.saleMargin = .2

    Lee = Customer()
    Chia = Customer()
    Joseph = Customer()


if __name__ == "__main__":
    main()



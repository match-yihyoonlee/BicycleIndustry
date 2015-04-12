"""
'Madone': [150, 100],
'Lexa': [400, 90],
'Silque': [1000, 80],
'FX': [1500, 70],
'CrossRip': [4500, 65],
'Tandem': [8000, 55]
"""

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

    affordableBikeList = {}

    # Create an instance of bike shop - Frisco's Bike Mart
    FriscoBikeMart = Shop()
    FriscoBikeMart.shopName = 'Fisco Bike\'s Mart'
    FriscoBikeMart.inventory = {'Madone': 5, 'Lexa': 3, 'Silque': 5, 'FX': 2, 'CrossRip': 1, 'Tandem': 1}
    FriscoBikeMart.saleMargin = .2

    # Create 3 customers
    Lee = Customer()
    Lee.customerName = 'Yih-Yoon Lee'
    Lee.availMoney = 200
    Lee.bikeOwn = ''

    Chia = Customer()
    Chia.customerName = 'Chang Chia'
    Chia.availMoney = 500
    Chia.bikeOwn = ''

    Joseph = Customer()
    Joseph.customerName = 'Joseph Tan'
    Joseph.availMoney = 1000
    Joseph.bikeOwn = ''

    customers = [Lee, Chia, Joseph]

    # Create 6 Bicycles
    Madone = Bicycle()
    Madone.modelName = 'Madone'
    Madone.bikeCost = 150
    Madone.weight = 100

    Lexa = Bicycle()
    Lexa.modelName = 'Lexa'
    Lexa.bikeCost = 400
    Lexa.weight = 90

    Silque = Bicycle()
    Silque.modelName = 'Silque'
    Silque.bikeCost = 1000
    Silque.weight = 80

    FX = Bicycle()
    FX.modelName = 'FX'
    FX.bikeCost = 1500
    FX.weight = 70

    CrossRip = Bicycle()
    CrossRip.modelName = 'CrossRip'
    CrossRip.bikeCost = 4500
    CrossRip.weight = 65

    Tandem = Bicycle()
    Tandem.modelName = 'Tandem'
    Tandem.bikeCost = 8000
    Tandem.weight = 55

    bicycles = [Madone, Lexa, Silque, FX, CrossRip, Tandem]

    print '{:<10} {:>10}'.format('Bicycle Model', 'Available')
    for bike, available in FriscoBikeMart.inventory.items():
        print '{:<10} {:>10}'.format(bike, available)

    for customer in customers:
        affordableBikeList[customer.customerName] = []
        for affordableBike in bicycles:
            if affordableBike.bikeCost <= customer.availMoney:
                affordableBikeList[customer.customerName].append(affordableBike)
    print '%s' % affordableBikeList
    #"Here is the list of bicycles for customer {}".format(affordableBikeList)  


if __name__ == "__main__":
    main()



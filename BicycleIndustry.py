__author__ = 'yih-yoonlee'


class Bicycle():
    def model(self, bikeName):
        self.bikeName = bikeName

    def weight(self, bikeWeight):
        self.bikeWeight = bikeWeight

    def cost(self, bikeCost):
        self.bikeCost = bikeCost


class Shop():
    pass


class Customer():
    def name(self, customerName):
        self.customerName = customerName

    def fund(self, availMoney):
        self.availMoney = availMoney

    def buyBike(self, buy):
        self.buy = buy


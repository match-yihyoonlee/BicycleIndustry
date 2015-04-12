affordableBikeList = {}

class Bicycle(object):
    def __init__(self,modelName,weight,bikeCost):
        self.modelName = modelName
        self.weight = weight
        self.bikeCost = bikeCost

class Shop(object):
    def __init__(self,shopName,saleMargin):
        self.shopName = shopName
        self.inventory = []
        self.totalProfit = 0
        self.saleMargin = saleMargin

    def retail_bike_price(self,bicycle):
        retailPrice = (bicycle.bikeCost * self.saleMargin) + bicycle.bikeCost
        return retailPrice
    
    def display_inventory(self):
        print '{:<10} {:>10}'.format('Bicycle Model', 'Available In Stock')
        for bike, available in self.inventory.items():
            print '{:<10} {:>10}'.format(bike, available)
        print '\n'

class Customer(object):
    def __init__(self,customerName,availMoney):
        self.customerName = customerName
        self.availMoney = availMoney
        self.bikeOwn = []

    def display_bikes(self, shop, bicycles):
        print 'Bicycle models that {} can afford are: '.format(self.customerName)
        for bicycle in bicycles:
            if shop.retail_bike_price(bicycle) < self.availMoney:
                print bicycle.modelName
        print '\n'

def main():
    # Create an instance of bike shop - Frisco's Bike Mart
    
    FriscoBikeMart = Shop('Fisco Bike\'s Mart',.2)
    FriscoBikeMart.inventory = {'Madone': 5, 'Lexa': 3, 'Silque': 5, 'FX': 2, 'CrossRip': 1, 'Tandem': 1}

    # Create 3 customers
    Lee = Customer('Yih-Yoon Lee',200)
    Chia = Customer('Chang Chia', 500)
    Joseph = Customer('Joseph Tan',10000)

    customers = [Lee, Chia, Joseph]

    Madone = Bicycle('Madone',100,150)
    Lexa = Bicycle('Lexa',90,400)
    Silque = Bicycle('Silque',80,1000)
    FX = Bicycle('FX',70,1500)
    CrossRip = Bicycle('CrossRip',65,4500)
    Tandem = Bicycle('Tandem',55,8000)

    bicycles = [Madone, Lexa, Silque, FX, CrossRip, Tandem]

    #print '{:<10} {:>10}'.format('Bicycle Model', 'Available In Stock')
    #for bike, available in FriscoBikeMart.inventory.items():
     #   print '{:<10} {:>10}'.format(bike, available)

    FriscoBikeMart.display_inventory()

    for customer in customers:
       customer.display_bikes(FriscoBikeMart,bicycles)

if __name__ == "__main__":
    main()

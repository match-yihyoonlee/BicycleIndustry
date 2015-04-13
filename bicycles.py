class Bicycle(object):
    def __init__(self,model_name,weight,cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)

class Shop(object):
    def __init__(self,shopName,saleMargin):
        self.shopName = shopName
        self.inventory = []
        self.totalProfit = 0
        self.saleMargin = saleMargin

    def retail_bike_price(self,bicycle):
        retailPrice = (bicycle.cost_to_produce * self.saleMargin) + bicycle.cost_to_produce
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
                print bicycle.model_name
        print '\n'
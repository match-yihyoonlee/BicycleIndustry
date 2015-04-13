class Bicycle(object):
    def __init__(self,model_name,weight,cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)

class Shop(object):
    def __init__(self,shop_name,sale_margin):
        self.shop_name = shop_name
        self.inventory = []
        self.total_profit = 0
        self.sale_margin = sale_margin

    def retail_bike_price(self,bicycle):
        retail_price = (bicycle.cost_to_produce * self.sale_margin) + bicycle.cost_to_produce
        return retail_price

    def display_inventory(self):
        print '{:<10} {:>10}'.format('Bicycle Model', 'Available In Stock')
        for bike, available in self.inventory.items():
            print '{:<10} {:>10}'.format(bike, available)
        print '\n'

class Customer(object):
    def __init__(self,customer_name,availMoney):
        self.customer_name = customer_name
        self.availMoney = availMoney
        self.bikeOwn = []

    def display_bikes(self, shop, bicycles):
        print 'Bicycle models that {} can afford are: '.format(self.customer_name)
        for bicycle in bicycles:
            if shop.retail_bike_price(bicycle) < self.availMoney:
                print bicycle.model_name
        print '\n'

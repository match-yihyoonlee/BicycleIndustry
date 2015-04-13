import random
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
        self.inventory = {}
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
    def __init__(self,customer_name,avail_money):
        self.customer_name = customer_name
        self.avail_money = avail_money
        self.bike_own = []

    def display_bikes(self, shop, bicycles):
        print 'Bicycle models that {} can afford are: '.format(self.customer_name)
        for bicycle in bicycles:
            if shop.retail_bike_price(bicycle) < self.avail_money:
                print bicycle.model_name
        print '\n'

    def buy_bike(self,customer_name,bicycles, shop):
        affordablebikelist = []
        for bicycle in bicycles:
            if shop.retail_bike_price(bicycle) < self.avail_money:
                affordablebikelist.append(bicycle)
        final_bike = random.choice(affordablebikelist)
        money_left = self.avail_money - shop.retail_bike_price(final_bike)
        shop.total_profit += shop.retail_bike_price(final_bike)
        shop.inventory[final_bike.model_name] -= 1

        print '{0} bought {1} for {2}. Customer has {3} available fund.'.format(self.customer_name,final_bike.model_name,shop.retail_bike_price(final_bike),money_left)

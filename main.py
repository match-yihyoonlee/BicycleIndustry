from bicycles import Bicycle, Shop, Customer

def main():
    # Create an instance of bike shop - Frisco's Bike Mart

    FriscoBikeMart = Shop('Fisco Bike\'s Mart',.2)
    FriscoBikeMart.inventory = {'Madone': 5, 'Lexa': 3, 'Silque': 5, 'FX': 2, 'CrossRip': 1, 'Tandem': 1}

    # Create 3 customers
    lee = Customer('Yih-Yoon Lee',200)
    chia = Customer('Chang Chia', 500)
    joseph = Customer('Joseph Tan',10000)

    customers = [lee, chia, joseph]

    madone = Bicycle('Madone', 150, 150)
    lexa = Bicycle('Lexa',90,400)
    silque = Bicycle('Silque',80,1000)
    fx = Bicycle('FX',70,1500)
    crossrip = Bicycle('CrossRip',65,4500)
    tandem = Bicycle('Tandem',55,8000)

    bicycles = [madone, lexa, silque, fx, crossrip, tandem]


    FriscoBikeMart.display_inventory()

    for customer in customers:
       customer.display_bikes(FriscoBikeMart,bicycles)

    for customer in customers:
        customer.buy_bike(customer, bicycles, FriscoBikeMart)

    print '\n{0}\'s Updated Inventory:'.format(FriscoBikeMart.shop_name)
    print '*' * 40

    FriscoBikeMart.display_inventory()

    print '\n{0}\'s total profit: {1}'.format(FriscoBikeMart.shop_name, FriscoBikeMart.total_profit)

if __name__ == "__main__":
    main()

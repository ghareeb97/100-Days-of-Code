from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
m = Menu()
coffeemaker = CoffeeMaker()
piggy_bank = MoneyMachine()

is_on = True

while is_on:
    drinks = m.get_items()
    order_request = input(f" What would you like ? ({drinks}): ")
    if order_request == "report":
        coffeemaker.report()
        piggy_bank.report()
    elif order_request == "off":
        is_on = False
    else:
        drink = m.find_drink(order_request)
        enough_resources = coffeemaker.is_resource_sufficient(drink)
        if enough_resources and piggy_bank.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
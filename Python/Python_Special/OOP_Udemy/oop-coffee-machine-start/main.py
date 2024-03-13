from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
ro get access the other classes, for every class should initiate an object of those classes
"""


# first elements initiated
menu_item = Menu()
coffee_maker = CoffeeMaker()
money_machin = MoneyMachine()


is_on = True
while is_on:
    options = menu_item.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machin.report()
        coffee_maker.report()
    else:
        drink = menu_item.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machin.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

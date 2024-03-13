from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




menu_items = Menu()
coffee_maker = CoffeeMaker()
money_machin = MoneyMachine()

menu_items.get_items()
coffee_maker.report()

# Print report
is_active = True
while is_active:
    water = coffee_maker.resources["water"]
    milk = coffee_maker.resources["milk"]
    coffee = coffee_maker.resources["coffee"]

    if water <  300:
        coffee_maker.report()
    elif milk < 200:
        coffee_maker.report()
    elif coffee < 100:
        coffee_maker.report()
    else:
        money_machin.report()
    break


check_resources = True
while check_resources:
    choice = coffee_maker.resources
    if choice["water"] < 300 :
        coffee_maker.report()
    elif choice["milk"] < 200:
        coffee_maker.report()
    elif choice["coffee"] < 100:
        coffee_maker.report()
    else:
        coffee_maker.make_coffee(order=input("what do u like: "))













# Process coins
is_active = True
while is_active:
    money = money_machin.process_coins()

    print(f"you inserted: {money} $")


    if money < money_machin.money_received:
        money_machin.make_payment(cost=money_machin.money_received)
    else:
        break

#is_active = False















# transaction payment
# money_recived = True
# while money_recived:
#     x = money_machin.make_payment(cost=5)
#     money_machin.process_coins()






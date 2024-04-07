from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


"""
ro get access the other classes, for every class should initiate an object of those classes

"""






x = MoneyMachine.CURRENCY
print(f"Money:{x}")


menu_item = Menu()
menu_item.get_items()

#menu_item.find_drink(order_name=Menu.__name__)



# first elements ready
cafee_maker = CoffeeMaker()
cafee_maker.report()




money_machin= MoneyMachine()
money_machin.report()




#is_enough = CoffeeMaker()
#is_enough.is_resource_sufficient(drink=CoffeeMaker.make_coffee())



is_on = True
while is_on:
	options = menu_item.get_items()
	choice = input(f"What would you like? ({options}) ")
	if choice == "off":
		is_on = False
	elif choice == "report":
		money_machin.report()
		cafee_maker.report()
	else:
		drink = menu_item.find_drink(choice)
		is_sufficient = True
		while is_sufficient:
			if cafee_maker.resources["water"] < 300 :
				cafee_maker.is_resource_sufficient(drink)
				
			elif cafee_maker.resources["milk"] < 200 :
				cafee_maker.is_resource_sufficient(drink)
				
			elif cafee_maker.resources["coffee"] < 100:
				cafee_maker.is_resource_sufficient(drink)
				
			elif cafee_maker.resources["water"] >= 300 \
					and cafee_maker.resources["milk"] >= 200 \
					and cafee_maker.resources["coffee"] >= 100:
				cafee_maker.make_coffee(drink)
				
				break
				
				
				















	
	
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker1= CoffeeMaker()
menu1= Menu()
money_machine1 = MoneyMachine()
should_continue=True
while should_continue:
    order = input(f"what would you like? {menu1.get_items()}: ")
    if order=="report":
        coffee_maker1.report()
        money_machine1.report()
    elif order=="off":
        should_continue=False
    else:
        drink=menu1.find_drink(order)
        if coffee_maker1.is_resource_sufficient(drink):
            if money_machine1.make_payment(drink.cost):
                coffee_maker1.make_coffee(drink)
        
            
        
        

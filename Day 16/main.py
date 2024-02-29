from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

coffe_maker.report()
money_machine.report()

machine_on = True

while machine_on:
    drinks = menu.get_items()

    choice = input(f"What would you like? ({drinks}): ")
    if choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)





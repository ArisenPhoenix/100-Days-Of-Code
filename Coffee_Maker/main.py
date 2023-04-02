from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True
while is_on:
    options = menu.display_menu()
    choice = input(f'What would you like?  \n')
    if (type(choice) is not None):
        if choice == 'off':
            # Turns the coffee machine off i.e. the program
            is_on = False
        elif choice == 'report':
            coffee_maker.report()
            money.report()
        elif choice == "fill":
            coffee_maker.fill_resources()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):

                if money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)




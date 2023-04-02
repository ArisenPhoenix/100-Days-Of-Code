from money_machine import MoneyMachine
CURRENCY = MoneyMachine.CURRENCY
class MenuItem:
    
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        try:
            order = int(order)
        except ValueError:
           order = str(order)
            
        for num, item in enumerate(self.menu):
            if type(order) == type("2"):
                if item.name == order:
                    print(f"Ok that will be {CURRENCY} {item.cost}")
                    return item
            elif type(order) == type(2):
                if num == order - 1:
                    print(f"Ok that will be {CURRENCY} {item.cost}")
                    return item
        print("Sorry that item is not available.")
        
    def get_longest_word_length(self):
        """For More Nicely Formatting the Menu"""
        longest = 0
        for item in self.menu:
            if len(item.name) > longest:
                longest = len(item.name)
        return longest
    
    def get_spaces(self, word, longest):
        spaces = longest - len(word)
        chars_between = ["- " for space in range(spaces)]
        chars_between = "".join(chars_between)
        return chars_between
    
        
    def display_menu(self):
        longest = self.get_longest_word_length()
        for num, item in enumerate(self.menu):
            spaces = self.get_spaces(item.name, longest)
            print(f"{num + 1}: {item.name} {spaces}{CURRENCY}{item.cost} ")
        return

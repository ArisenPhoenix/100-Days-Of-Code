class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    def __init__(self):
        self.profit = 0
        self.money_received = 0
    
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.currency}{self.profit}")
    
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
    
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
    
    def get_currency(self):
        return self.CURRENCY

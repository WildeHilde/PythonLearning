"""Create a banking system for practise"""

class Account:
    """The account of each of the bank's clients"""

    def __init__(self, name, initialBalance=0):
        self.name = name
        self.balance = initialBalance

    def info(self):
        """Print the account details"""
        print("The owner's name is {0} and the balance is {1}".format(self.name, self.balance))

    def transfer(self, amount):
        """"Adds the specified amount, returns an error is balance is below X"""

        new_bal = balance + amount
        if new_bal < 0:
            print("Account balance would be below 0. Action stopped!")
        else:
            balance = new_bal
            print("Transfer successful!")
    

        
acc1 = Account("Peter", 200)
acc1.info()

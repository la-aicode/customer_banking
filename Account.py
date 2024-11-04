class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance=0.0, interest=0.0):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    def get_balance(self):
        """Returns the current balance of the account"""
        return self.balance

    def set_interest(self, interest):
        """Sets the interest rate for the account"""
        self.interest = interest

    def get_interest(self):
        """Returns the current interest rate of the account"""
        return self.interest

    def deposit(self, amount):
        """Adds a specified amount to the account balance"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts a specified amount from the account balance, if sufficient funds are available"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def apply_interest(self):
        """Applies the current interest rate to the account balance"""
        if self.interest > 0:
            interest_amount = self.balance * (self.interest / 100)
            self.balance += interest_amount
            print(f"Interest of {interest_amount} applied. New balance: {self.balance}")
        else:
            print("Interest rate must be positive to apply interest.")

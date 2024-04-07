"""
Exercise 3: Create a BankAccount Class
Create a BankAccount class with attributes account_holder, balance, and account_type (e.g., savings or checking).
Implement methods to deposit and withdraw money, and a method to display the account balance.
"""

class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ${self.balance}")

# Example usage:
account1 = BankAccount(account_holder="John Doe", balance=1000, account_type="Savings")
account1.display_balance()

account1.deposit(500)
account1.withdraw(200)

account2 = BankAccount(account_holder="Alice Smith", balance=2000, account_type="Checking")
account2.display_balance()

account2.deposit(1000)
account2.withdraw(250)
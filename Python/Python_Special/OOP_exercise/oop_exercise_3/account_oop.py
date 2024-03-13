"""
Exercise 3: Create a BankAccount Class
Create a BankAccount class with attributes account_holder, balance, and account_type (e.g., savings or checking).
Implement methods to deposit and withdraw money, and a method to display the account balance.
"""

class BankAccount:
    def __init__(self, account_holder,  balance):

        self.account_holder = account_holder
        self.balance = balance
        #self.account_type = account_type
        
        
    def deposit1(self, deposit):
        if deposit > 0 :
            self.balance += deposit
            print(f"Deposit of: {deposit} succesfull.Now Balance: {self.balance}")


    def withdrow2(self, withdraw):
        #user_withrow = input(f"how much u want to Withdraw")
        if withdraw > 0 and withdraw <= self.balance:
            self.balance -= withdraw
            print(f"withdrawal of: {withdraw} succesfull.Now Balance is: {self.balance}")


    def display_balance(self):
        print(f"Account Holder : {self.account_holder}\nCurrent Balance: {self.balance}")


    def account_check(self , account_type):
        gold = "Golden Card"
        credit = "Master Card"
        if account_type == "G".lower():
            print(f"type acount: {gold}")
        elif account_type == "M".lower():
            print(f"type Account: {credit}")
        else:
            print(f"Unknown Account")


data = BankAccount("Ali", balance=300)
data.display_balance()
data.account_check("m")
data.withdrow2(22)
data.deposit1(50)






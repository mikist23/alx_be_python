class BankAccount:
    
    def __init__(self,account_balance):
        self.account_balance = account_balance
        self.account_balance = 0

    def deposit(self,amount):
        deposit = self.account_balance + amount
        return deposit


    def withdraw(self,amount):
        withdraw = self.account_balance - amount
        return withdraw

    def display_balance(self):
        balance = self.account_balance
        return balance


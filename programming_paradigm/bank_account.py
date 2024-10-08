class BankAccount:
    
    def __init__(self,account_balance=0):
        self.account_balance = account_balance
        

    def deposit(self,amount):
        self.account_balance += amount
        return self.account_balance


    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        balance = float(self.account_balance)
        print(f"Current Balance: ${balance:.2f}")
        return balance


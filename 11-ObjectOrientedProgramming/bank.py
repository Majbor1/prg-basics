import math

class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0
    
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += self.deposit_amount
    
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= self.withdraw_amount
        else:
            print("Insufficient funds on the account")

    def show_status(self):
        print(f"Bank Account No: {self.number}")
        print(f"Balance PLN: {self.balance}")
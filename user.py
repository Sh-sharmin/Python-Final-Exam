import random
from account import Account
class User:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account = Account(account_type)
        self.account_number = name+str(random.randint(1,100))
        print("Account created successfully")
        print(f"Account number: {self.account_number}")
        
    def deposit(self,amount):
        self.account.deposit(amount)
    def withdraw(self,amount):
        self.account.withdraw(amount)
    def check_balance(self):
        print(f"Balance: {self.account.balance}")
    def transaction_history(self):
        for i in self.account.transaction:
            print(i)
    def transfer(self,other_account_num,amount,bank):
        self.account.transfer(other_account_num,amount,bank)
    def take_loan(self,amount,bank):
        self.account.take_loan(amount,bank)
    
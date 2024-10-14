class Account:
    def __init__(self,account_type):
        self.account_type = account_type
        self.balance=0
        self.loan_amount=0
        self.transaction=[]
        self.loan_count=0
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction.append(f"Deposited: {amount}")
            print(f"Deposited {amount}")
            print(f"New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Withdrawal amount exceeded!")
        elif self.balance==0:
            print("Not sufficient balance!")
        else:
            self.balance-=amount
            self.transaction.append(f"Withdraw: {amount}")
            print(f"Withdrew: {amount}")
            print(f"New balance: {self.balance}")

    def take_loan(self,amount,bank):
        if bank.loan==True:
            if self.loan_count<2:
                self.loan_count+=1
                self.loan_amount+=amount
                print("Loan Approved!!")
                self.transaction.append(f"Loan: {amount}")
                self.deposit(amount)
            else:
                print("Loan limit exceeded.")
        else:
            print("Loan feature is off")

    def transfer(self,other_account_num,amount,bank):
        if self.balance >=amount:
            if bank.check_account_exists(other_account_num):
                self.withdraw(amount)
                bank.get_account(other_account_num).deposit(amount)
                self.transaction.append(f"Transfer: {amount}")
                print(f"Transferred successfully")
            else:
                print("Account does not exist!")
        else:
            print("Not sufficient balance!")
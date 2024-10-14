from user import User
class Admin:
    def __init__(self,name,phone,email) -> None:
        self.name=name
        self.phone=phone
        self.email=email

    def create_account(self,name,email,address,account_type,bank):
        new_user = User(name,email,address,account_type)
        bank.add_user(new_user)
    def view_user(self,bank):
        bank.view_user()
    def delele_account(self,account_num,bank):
        bank.delete_account(account_num)
    def total_bal(self,bank):
        total_balance = bank.get_balance()
        print(f"Total Balance of the bank: {total_balance}")
    def total_loan(self,bank):
        total_loan_amount=bank.get_loan_amount()
        print(f"Total loan amount of the bank: {total_loan_amount}")
    def loan_feature(self,flag,bank):
        bank.loan=flag
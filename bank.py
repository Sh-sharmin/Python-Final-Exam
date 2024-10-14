class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.users = []
        self.total_balance = 0
        self.loan_amount = 0
        self.loan=True

    def add_user(self,user):
        self.users.append(user)
    def view_user(self):
        print("User List: ")
        print("Name\tEmail\tAddress")
        for i in self.users:
            print(i.name,i.email,i.address)

    def delete_account(self,account_num):
        f=True
        for user in self.users:
            if user.account_number==account_num:
                f=False
                self.users.remove(user)
                print(f"{account_num} deleted")
                break
        if f:
            print(f"{account_num} doesn't exist")
    def get_balance(self):
        self.total_balance=0
        for i in self.users:
            self.total_balance+=i.account.balance
        return self.total_balance
    def get_loan_amount(self):
        self.loan_amount=0
        for i in self.users:
            self.loan_amount+=i.account.loan_amount
        return self.loan_amount
    def check_account_exists(self,account_num):
        for user in self.users:
            if user.account_number==account_num:
                return True
        return False
    def get_user(self,account_num):
        for user in self.users:
            if user.account_number==account_num:
                return user
        return None
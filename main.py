from bank import Bank
from admin import Admin
from user import User
bank = Bank("AB Bank")

def user_menu(user):
    while True:
        print(f"Welcome {user.name}!")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check balanace")
        print("4. View transaction history")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            amount=int(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice ==2:
            amount=int(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice==3:
            user.check_balance()
        elif choice==4:
            user.transaction_history()
        elif choice==5:
            amount = int(input("Enter loan amount: "))
            user.take_loan(amount,bank)
        elif choice==6:
            num = input("Enter Account Number to transfer money: ")
            amount=int(input("Enter amount to transfer: "))
            user.transfer(num,amount,bank)
        elif choice==7:
            break
        else:
            print("Invalid!")

def admin_menu():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone number: ")
    email = input("Enter Your Email: ")
    admin = Admin(name,phone,email)

    while True:
        print(f"Welcome {name}!")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. View Users")
        print("4. Check total bank balance")
        print("5. check total loan amount")
        print("6. Loan feature on/off")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            user_name = input("Enter name: ")
            email = input("Enter email: ")
            address= input("Enter address: ")
            account_type = input("Enter account type(savings/current): ")
            admin.create_account(user_name,email,address,account_type,bank)
        elif choice==2:
            account_number = input("Enter account number to delete: ")
            admin.delele_account(account_number,bank)
        elif choice==3:
            admin.view_user(bank)
        elif choice==4:
            admin.total_bal(bank)
        elif choice==5:
            admin.total_loan(bank)
        elif choice==6:
            flag = input("Enter on/off: ")
            if flag=='on':
                admin.loan_feature(True,bank)
            elif flag=='off':
                admin.loan_feature(False,bank)
            else:
                print("Invalid!")
        elif choice==7:
            break
        else:
            print("Invalid!")



while True:
    print("Welcome!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        account_number = input("Enter your account number: ")
        user= bank.get_user(account_number)
        if user:
            user_menu(user)
        else:
            print("Account does not exist!")    
    elif choice ==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid!")
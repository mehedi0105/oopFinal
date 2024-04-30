from user import Bank, Accaunt, User
from admin import Admin
# bank_name = input("Enter Bank Name : ")
# bank_adress = input("Enter Bank Address : ")
bank_name = "Grammen"
bank_address = "Badarganj,Rangpur"
bank = Bank(bank_name, bank_address)
print()


def user_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    accaunt_type = input("Enter Your Accaunt Type : ")
    # bank = Bank(bank_name, bank_adress)
    user = User(bank, name, email, address, accaunt_type)
    print()

    while True:
        print(f"Welcome {name}")
        print("1.Deposit Amount")
        print("2.Withdraw Amount")
        print("3.Check Available Balance")
        print("4.Check Transaction History")
        print("5.Loan Amount")
        print("6.Transfer Amaunt")
        print("7.Exit")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            amount = int(input("Enter Your Deposit Amaunt : "))
            user.deposit_amount(amount=amount)
            print()
        elif choice == 2:
            amount = int(input("Enter Your Withdraw Amaunt : "))
            user.withdraw_amount(amount=amount)
            print()
        elif choice == 3:
            user.check_available_balance()
            print()
        elif choice == 4:
            user.check_transaction_history()
            print()
        elif choice == 5:
            amount = int(input("Enter Your Loan Amaunt : "))
            user.loan_amount(amount=amount)
            print()
        elif choice == 6:
            trans = input("Enter Your Transfer Accaunt : ")
            amount = int(input("Enter Your Transfer Amaunt : "))
            user.transfer_amaunt(accaunt_no=name+email,
                                 amount=amount, tranfer_accaunt_no=trans)
            print()
        elif choice == 7:
            break
        else:
            print("Inavalid Input")
            print()


def admin_menu():

    admin = Admin(bank)
    while True:
        print("1. Create Account")
        print("2. Delete Accaunt")
        print("3. See User List")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Off loan feature")
        print("7. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            # bank, name, email, address, accaunt_type
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            admin.create_account(name=name,
                                 email=email, address=address)
            print()
        elif choice == 2:
            accaunt_no = input("Enter Delete accaunt_no : ")
            accaunt_type = input("Enter Your Accaunt Type : ")
            admin.delete_accaunt(accaunt_no=accaunt_no,
                                 accaunt_type=accaunt_type)
            print()
        elif choice == 3:
            admin.user_list()
            print()
        elif choice == 4:
            admin.total_available_balance()
            print()
        elif choice == 5:
            admin.total_loan_amount()
            print()
        elif choice == 6:
            admin.off__loan_feature(bool=False)
            print()
        elif choice == 7:
            break
        else:
            print("Inavalid Input")
            print()


while True:
    print("Welcome!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")

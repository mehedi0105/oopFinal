
class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.Savings_accaunts = []
        self.Curent_accaunts = []
        self.admin_accaunts = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_fature = True


class Accaunt:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.accaunt_no = name+email
        self.transaction_history = {}
        self.takeloan = 0

    def deposit_amount(self, amount):
        self.balance += amount
        self.transaction_history["deposit_amount"] = amount
        # print(self.balance)

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history["withdraw_amount"] = amount
            # print(self.balance)
        else:
            print("\tWithdrawal amount exceeded")


class User:
    def __init__(self, bank, name, email, address, accaunt_type) -> None:
        self.bank = bank
        self.accaunt = Accaunt(name, email, address)
        if accaunt_type.lower() == "savings":
            bank.Savings_accaunts.append(self.accaunt)

        elif accaunt_type.lower() == "cuurent":
            bank.Curent_accaunts.append(self.accaunt)

        else:
            print(f"\tAccaunt Type is Not Valid")

    def deposit_amount(self, amount):
        self.accaunt.deposit_amount(amount)
        self.bank.total_balance += amount

    def withdraw_amount(self, amount):
        self.accaunt.withdraw_amount(amount)
        self.bank.total_balance -= amount

    def check_available_balance(self):
        print(f"\tYour Accautnt current balance is: {self.accaunt.balance}")

    def check_transaction_history(self):
        print(f"\tYour Accautnt transaction history is: {
              self.accaunt.transaction_history}")

    def loan_amount(self, amount):
        if self.bank.loan_fature == True:
            if self.accaunt.takeloan < 2:
                self.accaunt.takeloan += 1
                self.bank.total_loan += amount
            else:
                print(f"\tsorry you already two time taken loan")

    def transfer_amaunt(self, accaunt_no, amount, tranfer_accaunt_no):
        for account in self.bank.Savings_accaunts + self.bank.Curent_accaunts:
            if account.accaunt_no == tranfer_accaunt_no:
                account.balance += amount
                account.transaction_history["add_balance"] = amount
                for account in self.bank.Savings_accaunts + self.bank.Curent_accaunts:
                    if account.accaunt_no == accaunt_no:
                        account.balance -= amount
                        account.transaction_history["transfer_balance"] = amount
                        return
        print("Tranfer Accaunt No Not Found")

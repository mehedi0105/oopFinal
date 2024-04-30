from user import Bank, Accaunt, User


class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank

    def create_account(self, name, email, address, ):
        self.accaunt = Accaunt(name, email, address)
        self.bank.admin_accaunts.append(self.accaunt)

    def delete_accaunt(self, accaunt_no, ):
        if self.accaunt.accaunt_type.lower() == "savings":
            for account in self.bank.Savings_accaunts:
                if account.accaunt_no == accaunt_no:
                    self.bank.Savings_accaunts.remove(account)

        elif self.accaunt.accaunt_type.lower() == "Cuurent":
            for account in self.bank.Curent_accaunts:
                if account.accaunt_no == accaunt_no:
                    self.bank.Curent_accaunts.remove(account)

        else:
            print(f"Accaunt type is not Valid")

    def user_list(self):
        # print(f"user name\temail\tbalance\taccaunt no")
        for account in self.bank.Savings_accaunts + self.bank.Curent_accaunts:
            print([account.name, account.email,
                  account.balance, account.accaunt_no])

    def total_available_balance(self):
        total_balance = sum(
            account.balance for account in self.bank.Savings_accaunts + self.bank.Curent_accaunts)
        print(f"\tTotal Available Balance is {total_balance}")

    def total_loan_amount(self):
        print(f"Total loan amount {self.bank.total_loan}")

    def off__loan_feature(self, bool):
        self.bank.loan_fature = bool

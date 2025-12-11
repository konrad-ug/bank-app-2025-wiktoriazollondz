from src.personal_account import PersonalAccount

class AccountsRegistry(PersonalAccount):
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        for acc in self.accounts:
            if acc.pesel == account.pesel:
                return False

        self.accounts.append(account)
        return True

    def search_pesel(self, pesel: str) -> None:
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None

    def return_account(self):
        return self.accounts

    def amount_of_accounts(self):
        return len(self.accounts)




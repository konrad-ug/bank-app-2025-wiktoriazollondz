from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name: str, nip: str):
        super().__init__()
        self.company_name = company_name
        self.set_nip(nip)

    def set_nip(self, nip):
        if isinstance(nip, str) and len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = "Invalid"

    def express_transfer(self, amount: float) -> None:
        fee = 5.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance -= (amount + fee)

    def take_loan(self, amount: float):
        if self.balance >= 2 * amount and -1775 in self.history:
            self.balance += amount
            return True

        return False
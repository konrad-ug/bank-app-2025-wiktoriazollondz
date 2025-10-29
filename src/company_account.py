from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name: str, nip: str):
        super().__init__()
        self.company_name = company_name
        if isinstance(nip, str) and len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = "Invalid"

    def express_transfer(self, amount: float) -> None:
        fee = 5.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance -= (amount + fee)
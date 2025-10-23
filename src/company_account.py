from src.account import Account

def CompanyAccount(Account):
    def __init__(self, name, nip):
        self.nip = nip if self.is_nip_valid(nip) else "Invalid"
        self.balance = 0.0

    def is_nip_valid(self, nip):
        if isinstance(nip, str) and len(nip) == 10:
            return True
        return False
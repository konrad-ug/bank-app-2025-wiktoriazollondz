from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        if isinstance(pesel, str) and len(pesel) == 11 and pesel.isdigit():
            self.pesel = pesel
        else:
            self.pesel = "Invalid"

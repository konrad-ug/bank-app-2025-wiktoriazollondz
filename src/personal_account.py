from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel=None, balance=0):
        super().__init__(balance)
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        self.set_pesel(pesel)

    def set_pesel(self, pesel):
        if isinstance(pesel, str) and len(pesel) == 11 and pesel.isdigit():
            self.pesel = pesel
        else:
            self.pesel = "Invalid"

    def submit_for_loan(self, amount):
        if self.last_three_positive():
            self.balance += amount
            return True

        if self.sum_of_last_five(amount):
            self.balance += amount
            return True

        return False

    def last_three_positive(self):
        if len(self.history) < 3:
            return False
        last_three = self.history[-3:]
        return all(t > 0 for t in last_three)

    def sum_of_last_five(self, amount):
        if len(self.history) < 5:
            return False
        return sum(self.history[-5:]) > amount
class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.promo_code = promo_code
        if isinstance(pesel, str) and len(pesel) == 11 and pesel.isdigit():
            self.pesel = pesel
        else:
            self.pesel = "Invalid"

        if self.promo_code and self.promo_code.startswith("PROM_") and len(self.promo_code) == 8 and self.born_after_1960():
            self.balance += 50

    def born_after_1960(self):
        if self.pesel == "Invalid":
            return False
        year = int(self.pesel[:2])
        month = int(self.pesel[2:4])
        year += 1900 if month <= 12 else 2000
        return year > 1960


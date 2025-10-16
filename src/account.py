class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.promo_code = promo_code
        if isinstance(pesel, str) and len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Invalid"
        if isinstance(promo_code, str) and promo_code.startswith("PROM_") and len(promo_code) == 8:
            self.balance += 50

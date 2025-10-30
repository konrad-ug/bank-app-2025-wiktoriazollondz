class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def incoming_transfer(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
    
    def outgoing_transfer(self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def express_transfer(self, amount: float) -> None:
        fee = 1.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance -= (amount + fee)

    def transfer(self, amount):
        fee = 3.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance += (amount + fee)
class Account:
    def __init__(self, balance=0, history=None):
        self.balance = balance
        self.history = [] if history is None else history

    def incoming_transfer(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            self.history.append(amount)
    
    def outgoing_transfer(self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(-amount)

    def express_transfer(self, amount: float) -> None:
        fee = 1.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance -= (amount + fee)
            self.history.append(-amount)
            self.history.append(-fee)
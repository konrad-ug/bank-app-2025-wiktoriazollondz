from src.personal_account import PersonalAccount
from src.account import Account

class TestTransfers:
    def test_incoming_transfer(self):
        account = Account()
        account.incoming_transfer(100.0)
        assert account.balance == 100.0

    def test_outgoing_transfer(self):
        account = Account()
        account.balance = 100.0
        account.outgoing_transfer(50.0)
        assert account.balance == 50.0

    def test_outgoing_transfer_exceeding_balance(self):
        account = Account()
        account.balance = 30.0
        account.outgoing_transfer(50.0)
        assert account.balance == 30.0

    def test_incoming_transfer_negative_amount(self):
        account = Account()
        account.incoming_transfer(-20.0)
        assert account.balance == 0.0
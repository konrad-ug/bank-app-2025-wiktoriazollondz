from src.account import Account
from src.personal_account import PersonalAccount


class TestExpressTransfer:
    def test_tranfer_history(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(100.0)
        acc.express_transfer(50.0)
        assert acc.history == [100.0, -50.0, -1.0]

    def test_tranfer_history2(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(100.0)
        acc.outgoing_transfer(50.0)
        acc.express_transfer(20.0)
        assert acc.history == [100.0, -50.0, -20.0, -1.0]
from src.account import Account
from src.company_account import CompanyAccount

class TestExpressTransfer:
    def test_express_transfer_personal_account_fee_1(self):
        acc = Account()
        acc.incoming_transfer(100.0)
        acc.express_transfer(50.0)
        # 100 - 50 - 1 = 49
        assert acc.balance == 49.0

    def test_express_transfer_personal_account_can_go_minus_fee(self):
        acc = Account()
        acc.incoming_transfer(50.0)
        acc.express_transfer(50.0)
        # 50 - 50 - 1 = -1
        assert acc.balance == -1.0

    def test_express_transfer_company_account_fee_5(self):
        acc = CompanyAccount("Tech Solutions", "1234567890")
        acc.incoming_transfer(100.0)
        acc.express_transfer(50.0)
        # 100 - 50 - 5 = 45
        assert acc.balance == 45.0

    def test_express_transfer_company_account_can_go_minus_fee(self):
        acc = CompanyAccount("Tech Solutions", "1234567890")
        acc.incoming_transfer(50.0)
        acc.express_transfer(50.0)
        # 50 - 50 - 5 = -5
        assert acc.balance == -5.0

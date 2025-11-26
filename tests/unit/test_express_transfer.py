import pytest
class TestExpressTransfer:
    @pytest.mark.parametrize("input1, input2, expected", [
        (100.0, 50.0, 49.0),
        (50.0, 50.0, -1.0),
    ])
    def test_express_transfer_personal_account_fee_1(self, acc, input1, input2, expected):
        acc.incoming_transfer(input1)
        acc.express_transfer(input2)
        assert acc.balance == expected

    @pytest.mark.parametrize("input1, input2, expected", [
        (100.0, 50.0, 45.0),
        (50.0, 50.0, -5.0),
    ])
    def test_express_transfer_company_account_fee_5(self, comp_acc, input1, input2, expected):
        comp_acc.incoming_transfer(input1)
        comp_acc.express_transfer(input2)
        assert comp_acc.balance == expected

import pytest
class TestTransfers:
    @pytest.mark.parametrize("input, expected", [
        (100.0, 100.0),
        (-20.0, 0.0)
    ])
    def test_incoming_transfer(self, acc, input, expected):
        acc.incoming_transfer(input)
        assert acc.balance == expected

    @pytest.mark.parametrize("input1, input2, expected", [
        (100.0, 50.0, 50.0),
        (30.0, 50.0, 30.0)
    ])
    def test_outgoing_transfer(self, acc, input1, input2, expected):
        acc.balance = input1
        acc.outgoing_transfer(input2)
        assert acc.balance == expected
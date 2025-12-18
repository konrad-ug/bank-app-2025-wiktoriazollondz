import pytest
@pytest.mark.usefixtures("mock_mf_ok")
class TestLoan:
    @pytest.mark.parametrize("balance, history, amount, expected_balance, expected_result", [
        (300.0, [-1775], 100.0, 400.0, True),  # oba warunki OK
        (225.0, [-1775], 300.0, 225.0, False),  # saldo za niskie
        (2000.0, [], 300.0, 2000.0, False),  # brak ZUS
        (100.0, [], 300.0, 100.0, False),  # brak ZUS + saldo za niskie
    ])
    def test_take_loan(self, comp_acc, balance, history, amount, expected_balance, expected_result):
        comp_acc.balance = balance
        comp_acc.history = history.copy()
        result = comp_acc.take_loan(amount)
        assert result == expected_result
        assert comp_acc.balance == expected_balance

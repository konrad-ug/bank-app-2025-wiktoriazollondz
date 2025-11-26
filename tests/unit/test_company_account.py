import pytest
class TestCompanyAccount:
    def test_account_creation(self, comp_acc):
        assert comp_acc.company_name == "Tech Solutions"
        assert comp_acc.nip == "1234567890"

    @pytest.mark.parametrize("input, expected", [
        ("1234567890", "1234567890"),
        ("12345", "Invalid"),
        ("12A4567890", "Invalid")
    ])
    def test_nip_validation(self, comp_acc, input, expected):
        comp_acc.set_nip(input)
        assert comp_acc.nip == expected

    def test_transfers_work_same_as_account(self, comp_acc):
        comp_acc.incoming_transfer(200.0)
        comp_acc.outgoing_transfer(100.0)
        assert comp_acc.balance == 100.0
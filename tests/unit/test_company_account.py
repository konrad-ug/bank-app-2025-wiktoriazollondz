import pytest
from src.company_account import CompanyAccount
@pytest.mark.usefixtures("mock_gov_api")
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

    def test_company_account_creation_success(self, mock_gov_api):
        account = CompanyAccount("Tech Solutions", "1234567890")
        assert account.nip == "1234567890"

    def test_company_account_invalid_nip_raises(self, mock_gov_api):
        mock_gov_api.return_value.json.return_value = {
            "result": {"subject": {"statusVat": "Nieaktywny"}}
        }

        with pytest.raises(ValueError, match="Company not registered!!"):
            CompanyAccount("Bad Company", "1234567890")

    def test_company_account_short_nip(self, mock_gov_api):
        account = CompanyAccount("Small Biz", "123")
        assert account.nip == "Invalid"

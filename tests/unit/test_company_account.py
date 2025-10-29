from src.company_account import CompanyAccount

class TestCompanyAccount:
    def test_account_creation(self):
        account = CompanyAccount("Tech Solutions", "1234567890")
        assert account.company_name == "Tech Solutions"
        assert account.nip == "1234567890"

    def test_account_creation_with_invalid_nip(self):
        account = CompanyAccount("Business Corp", "12345")
        assert account.nip == "Invalid"

    def test_account_invalid_nip_not_digits(self):
        acc = CompanyAccount("Business Corp", "12A4567890")
        assert acc.nip == "Invalid"

    def test_transfers_work_same_as_account(self):
        acc = CompanyAccount("Tech Solutions", "1234567890")
        acc.incoming_transfer(200.0)
        acc.outgoing_transfer(100.0)
        assert acc.balance == 100.0
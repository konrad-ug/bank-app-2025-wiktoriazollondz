class TestCompanyAccount:
    def test_account_creation(self):
        account = CompanyAccount("Tech Solutions", "1234567890")
        assert account.name == "Tech Solutions"
        assert account.nip == "1234567890"

    def test_account_creation_with_invalid_nip(self):
        account = CompanyAccount("Business Corp", "12345")
        assert account.nip == "12345"
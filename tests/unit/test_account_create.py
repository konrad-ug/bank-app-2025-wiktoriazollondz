from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678910")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "12345678910"

    def test_pesel_too_long_or_short(self):
        account = Account("Jan", "Kowalski", "4325436865564357658")
        account2 = Account("Joe", "Doe", "4325436")
        assert account.pesel == "Invalid"
        assert account2.pesel == "Invalid"

    def test_promo(self):
        account = Account("John", "Doe", "12345678910", "PROMO_XYZ", 50)
        assert account.promo_code == "PROMO_XYZ"
        assert account.balance == 50
        account2 = Account("John", "Doe", "12345678910", None, 0)
        assert account2.promo_code == None
        assert account2.balance == 0


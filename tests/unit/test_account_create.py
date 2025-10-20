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
        account = Account("John", "Doe", "75051412345", "PROM_XYZ", 50)
        assert account.promo_code == "PROM_XYZ"
        assert account.balance == 100
        account1 = Account("John", "Doe", "75051412345", "PROM_343")
        assert account1.balance == 50
        account2 = Account("John", "Doe", "75051412345", None)
        assert account2.promo_code == None
        assert account2.balance == 0
        account3 = Account("John", "Doe", "75051412345", "PR_343")
        assert account3.balance == 0

    def test_promo_year(self):
        account = Account("John", "Doe", "75051412345", "PROM_XYZ")
        assert account.balance == 50
        account1 = Account("John", "Doe", "50062067890", "PROM_XYZ")
        assert account1.balance == 0




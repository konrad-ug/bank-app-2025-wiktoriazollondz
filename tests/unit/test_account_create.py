from src.personal_account import PersonalAccount

class TestAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "12345678910"

    def test_pesel_too_long_or_short(self):
        account = PersonalAccount("Jan", "Kowalski", "4325436865564357658")
        account2 = PersonalAccount("Joe", "Doe", "4325436")
        assert account.pesel == "Invalid"
        assert account2.pesel == "Invalid"




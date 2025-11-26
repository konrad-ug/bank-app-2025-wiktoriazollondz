import pytest
class TestAccount:
    @pytest.mark.parametrize("input, expected", [
        ("12345678910", "12345678910"),  # prawidłowy PESEL
        ("4325436865564357658", "Invalid"),  # za długi
        ("4325436", "Invalid"),  # za krótki
        ("abcdefghijk", "Invalid"),  # niecyfry
    ])
    def test_pesel_validation(self, personal_acc, input, expected):
        personal_acc.set_pesel(input)
        assert personal_acc.pesel == expected

    def test_account_creation(self, personal_acc):
        assert personal_acc.first_name == "Jan"
        assert personal_acc.last_name == "Kowalski"
        assert personal_acc.balance == 0




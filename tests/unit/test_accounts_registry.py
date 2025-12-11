class TestAccount:
    def test_add_account(self, acc_reg, personal_acc):
        result = acc_reg.add_account(personal_acc)
        assert result is True
        assert len(acc_reg.accounts) == 1

    def test_add_account_duplicate_pesel(self, acc_reg, personal_acc):
        acc_reg.add_account(personal_acc)
        duplicate = personal_acc
        result = acc_reg.add_account(duplicate)
        assert result is False
        assert len(acc_reg.accounts) == 1

    def test_search_pesel(self, acc_reg, personal_acc):
        personal_acc.set_pesel("12345678910")
        acc_reg.add_account(personal_acc)
        result = acc_reg.search_pesel("12345678910")
        assert result is personal_acc

    def test_search_pesel_false(self, acc_reg, personal_acc):
        personal_acc.set_pesel("12345678910")
        acc_reg.add_account(personal_acc)
        assert acc_reg.search_pesel("123456789") is None

    def test_return_account_empty(self, acc_reg):
        assert acc_reg.return_account() == []

    def test_return_account(self, acc_reg, personal_acc):
        acc_reg.add_account(personal_acc)
        accounts = acc_reg.return_account()
        assert accounts[0] is personal_acc

    def test_amount_of_accounts(self, acc_reg, personal_acc):
        acc_reg.add_account(personal_acc)
        assert acc_reg.amount_of_accounts() == 1


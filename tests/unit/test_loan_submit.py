from src.personal_account import PersonalAccount

class TestLoan:
    def test_loan_true_last_three(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(100.0)
        acc.incoming_transfer(100.0)
        acc.incoming_transfer(100.0)
        assert acc.submit_for_loan(100.0) == True
        assert acc.balance == 400.0

    def test_loan_true_sum_of_five(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        for _ in range(5):
            acc.incoming_transfer(100.0)
        assert acc.submit_for_loan(100.0) == True
        assert acc.balance == 600.0

    def test_loan_false_too_few_transactions(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(100.0)
        assert acc.submit_for_loan(100.0) == False
        assert acc.balance == 100.0

    def test_loan_false_last_three_negative(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(300.0)
        acc.outgoing_transfer(100.0)
        acc.outgoing_transfer(100.0)
        assert acc.submit_for_loan(100.0) == False
        assert acc.balance == 100.0

    def test_loan_false_last_three_negative_but_five_sum_positive(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(200.0)
        acc.incoming_transfer(100.0)
        acc.incoming_transfer(100.0)
        acc.outgoing_transfer(100.0)
        acc.outgoing_transfer(100.0)
        assert acc.submit_for_loan(100.0) == True
        assert acc.balance == 300.0

    def test_loan_false_last_three_not_positive(self):
        acc = PersonalAccount("Jan", "Doe", "12345678910")
        acc.incoming_transfer(500.0)
        acc.outgoing_transfer(200.0)
        acc.outgoing_transfer(200.0)
        acc.incoming_transfer(100.0)
        acc.incoming_transfer(100.0)
        assert acc.submit_for_loan(500.0) == False
        assert acc.balance == 300.0


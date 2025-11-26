class TestLoan:
    def test_loan_true_last_three(self, personal_acc):
        personal_acc.incoming_transfer(100.0)
        personal_acc.incoming_transfer(100.0)
        personal_acc.incoming_transfer(100.0)
        assert personal_acc.submit_for_loan(100.0) == True
        assert personal_acc.balance == 400.0

    def test_loan_true_sum_of_five(self, personal_acc):
        for _ in range(5):
            personal_acc.incoming_transfer(100.0)
        assert personal_acc.submit_for_loan(100.0) == True
        assert personal_acc.balance == 600.0

    def test_loan_false_too_few_transactions(self, personal_acc):
        personal_acc.incoming_transfer(100.0)
        assert personal_acc.submit_for_loan(100.0) == False
        assert personal_acc.balance == 100.0

    def test_loan_false_last_three_negative(self, personal_acc):
        personal_acc.incoming_transfer(300.0)
        personal_acc.outgoing_transfer(100.0)
        personal_acc.outgoing_transfer(100.0)
        assert personal_acc.submit_for_loan(100.0) == False
        assert personal_acc.balance == 100.0

    def test_loan_false_last_three_negative_but_five_sum_positive(self, personal_acc):
        personal_acc.incoming_transfer(200.0)
        personal_acc.incoming_transfer(100.0)
        personal_acc.incoming_transfer(100.0)
        personal_acc.outgoing_transfer(100.0)
        personal_acc.outgoing_transfer(100.0)
        assert personal_acc.submit_for_loan(100.0) == True
        assert personal_acc.balance == 300.0

    def test_loan_false_last_three_not_positive(self, personal_acc):
        personal_acc.incoming_transfer(500.0)
        personal_acc.outgoing_transfer(200.0)
        personal_acc.outgoing_transfer(200.0)
        personal_acc.incoming_transfer(100.0)
        personal_acc.incoming_transfer(100.0)
        assert personal_acc.submit_for_loan(500.0) == False
        assert personal_acc.balance == 300.0


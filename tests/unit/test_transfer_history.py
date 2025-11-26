class TestExpressTransfer:
    def test_tranfer_history(self, personal_acc):
        personal_acc.incoming_transfer(100.0)
        personal_acc.express_transfer(50.0)
        assert personal_acc.history == [100.0, -50.0, -1.0]

    def test_tranfer_history2(self, personal_acc):
        personal_acc.incoming_transfer(100.0)
        personal_acc.outgoing_transfer(50.0)
        personal_acc.express_transfer(20.0)
        assert personal_acc.history == [100.0, -50.0, -20.0, -1.0]
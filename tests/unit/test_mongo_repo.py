from src.mongo_repository import MongoAccountsRepository

class TestMongoRepository:
    def test_save_all_clears_and_inserts(self, mocker):
        mock_collection = mocker.Mock()
        repo = MongoAccountsRepository("mock_uri", "db", "coll")
        repo.collection = mock_collection

        mock_account = mocker.Mock()
        mock_account.pesel = "123"
        mock_account.to_dict.return_value = {"pesel": "123", "saldo": 100}

        repo.save_all([mock_account])

        mock_collection.delete_many.assert_called_once_with({})

        mock_collection.update_one.assert_called_once_with(
            {"pesel": "123"},
            {"$set": {"pesel": "123", "saldo": 100}},
            upsert=True
        )

    def test_load_all_returns_data_from_db(self, mocker):
        mock_collection = mocker.Mock()
        repo = MongoAccountsRepository("mock_uri", "db", "coll")
        repo.collection = mock_collection

        mock_collection.find.return_value = [
            {"name": "Jan", "surname": "Kowalski", "pesel": "123"},
            {"name": "Anna", "surname": "Nowak", "pesel": "456"}
        ]

        result = repo.load_all()

        mock_collection.find.assert_called_once_with({})
        assert len(result) == 2
        assert result[0]["pesel"] == "123"
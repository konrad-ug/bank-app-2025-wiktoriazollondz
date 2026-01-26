from pymongo import MongoClient

class MongoAccountsRepository:
    def __init__(self, connection_string, db_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_all(self, accounts):
        self.collection.delete_many({})
        for account in accounts:
            self.collection.update_one(
                {"pesel": account.pesel},
                {"$set": account.to_dict()},
                upsert=True,
            )

    def load_all(self):
        return list(self.collection.find({}))
from flask import Flask, request, jsonify
from src.accounts_registry import AccountsRegistry
from src.personal_account import PersonalAccount
from src.mongo_repository import MongoAccountsRepository

app = Flask(__name__)
registry = AccountsRegistry()
repository = MongoAccountsRepository("mongodb://localhost:27017/", "bank_db", "accounts")

@app.route("/api/accounts/reset", methods=['POST'])
def reset_accounts():
    registry.accounts = []
    return jsonify({"message": "Registry cleared"}), 200

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])
    result = registry.add_account(account)
    if result is True:
        return jsonify({"message": "Account created"}), 201
    else:
        return jsonify({"message": "Account with this pesel already exists"}), 409

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.return_account()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel": acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.amount_of_accounts()
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    print("Get account by pesel request received")
    acc = registry.search_pesel(pesel)
    if acc is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({"name": acc.first_name, "surname": acc.last_name, "pesel": acc.pesel, "balance": acc.balance}), 200

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    print("Update account request received")
    acc = registry.search_pesel(pesel)
    if acc is None:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()
    if "name" in data:
        acc.first_name = data["name"]
    if "surname" in data:
        acc.last_name = data["surname"]
    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    print("Delete account request received")
    acc = registry.search_pesel(pesel)
    if acc is None:
        return jsonify({"error": "Account not found"}), 404

    registry.accounts.remove(acc)
    return jsonify({"message": "Account deleted"}), 200

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer_account(pesel):
    print("Transfer account request received")
    acc = registry.search_pesel(pesel)
    if acc is None:
        return jsonify({"error": "Account not found"}), 404

    body = request.get_json()
    type = body["type"]
    amount = body["amount"]

    if type == "incoming":
        acc.incoming_transfer(amount)
        return jsonify({"message": "Order accepted for processing"}), 200

    elif type == "outgoing":
        success = acc.outgoing_transfer(amount)
        if not success:
            return jsonify({"error": "Transfer not successful"}), 422
        return jsonify({"message": "Order accepted for processing"}), 200

    elif type == "express":
        success = acc.express_transfer(amount)
        if not success:
            return jsonify({"error": "Transfer not successful"}), 422
        return jsonify({"message": "Order accepted for processing"}), 200

    else:
        return jsonify({"error": "Unknown transfer type"}), 400

@app.route("/api/accounts/save", methods=['POST'])
def save_accounts():
    accounts = registry.return_account()
    repository.save_all(accounts)
    return jsonify({"message": "Successfully saved to database"}), 200

@app.route("/api/accounts/load", methods=['POST'])
def load_accounts():
    registry.accounts = []

    accounts_data = repository.load_all()
    for data in accounts_data:
        nowe_konto = PersonalAccount(
            data["first_name"],
            data["last_name"],
            data["pesel"],
            data["balance"]
        )
        registry.add_account(nowe_konto)

    return jsonify({"message": "Successfully loaded from database"}), 200

import requests

url = "http://127.0.0.1:5000/api/accounts"

class TestAccountsApi:
    def test_save_accounts_endpoint(self):
        response = requests.post(f"{url}/save")

        assert response.status_code == 200
        assert response.json()["message"] == "Successfully saved to database"

    def test_load_accounts_endpoint(self):
        response = requests.post(f"{url}/load")

        assert response.status_code == 200
        assert response.json()["message"] == "Successfully loaded from database"

    def test_full_cycle_save_and_load(self):
        save_resp = requests.post(f"{url}/save")
        assert save_resp.status_code == 200

        load_resp = requests.post(f"{url}/load")
        assert load_resp.status_code == 200
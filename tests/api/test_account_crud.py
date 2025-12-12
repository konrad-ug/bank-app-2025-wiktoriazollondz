import requests

url = "http://127.0.0.1:5000/api/accounts"

class TestAPI:
    def test_create_account(self, api_acc):
        requests.post(f"{url}/reset")
        r = requests.post(url, json=api_acc)
        assert r.status_code == 201
        assert r.json() == {"message": "Account created"}

    def test_get_all_accounts(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.get(url)
        assert r.status_code == 200
        assert r.json() == [{"balance": 0.0, "name": "Jan", "pesel": "12345678901", "surname": "Kowalski"}]

    def test_get_account_count(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.get(f"{url}/count")
        assert r.status_code == 200
        assert r.json() == {"count": 1}

    def test_get_account_by_pesel(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.get(f"{url}/12345678901")
        assert r.status_code == 200
        assert r.json() == {"balance": 0.0, "name": "Jan", "pesel": "12345678901", "surname": "Kowalski"}

    def test_get_account_by_pesel_fail(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.get(f"{url}/00000000000")
        assert r.status_code == 404
        assert r.json() == {"error": "Account not found"}

    def test_update_account(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        update = {"name": "Adam"}
        r = requests.patch(f"{url}/12345678901", json=update)
        assert r.status_code == 200
        r2 = requests.get(f"{url}/12345678901")
        assert r2.json()["name"] == "Adam"
        assert r2.json()["surname"] == "Kowalski"

    def test_delete_account(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.delete(f"{url}/12345678901")
        assert r.status_code == 200
        r2 = requests.get(f"{url}/12345678901")
        assert r2.status_code == 404

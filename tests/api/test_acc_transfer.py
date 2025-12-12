import requests

url = "http://127.0.0.1:5000/api/accounts"

class TestAPI:
    def test_unique_pesel(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r2 = requests.post(url, json=api_acc)
        assert r2.status_code == 409
        assert r2.json()["message"] == "Account with this pesel already exists"

    def test_all_fail(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "diff"})
        assert r.status_code == 400
        assert r.json() == {"error": "Unknown transfer type"}

    def test_incoming_transfer(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "incoming"})
        assert r.status_code == 200
        assert r.json() == {"message": "Order accepted for processing"}

    def test_outcoming_transfer(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        requests.post(f"{url}/12345678901/transfer", json={"amount": 200, "type": "incoming"})
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "outgoing"})
        assert r.status_code == 200
        assert r.json() == {"message": "Order accepted for processing"}

    def test_outcoming_transfer_fail(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "outgoing"})
        assert r.status_code == 422
        assert r.json() == {"error": "Transfer not successful"}

    def test_express_transfer(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        requests.post(f"{url}/12345678901/transfer", json={"amount": 200, "type": "incoming"})
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "express"})
        assert r.status_code == 200
        assert r.json() == {"message": "Order accepted for processing"}

    def test_express_transfer_fail(self, api_acc):
        requests.post(f"{url}/reset")
        requests.post(url, json=api_acc)
        r = requests.post(f"{url}/12345678901/transfer", json={"amount": 100, "type": "express"})
        assert r.status_code == 422
        assert r.json() == {"error": "Transfer not successful"}
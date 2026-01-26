import requests
import time

URL = "http://127.0.0.1:5000"
LIMIT = 0.5


def test_1_stworz_usun():
    for i in range(100):
        start = time.time()
        r_post = requests.post(f"{URL}/accounts", json={"name": "Test"}, timeout=LIMIT)
        koniec = time.time() - start

        if r_post.status_code not in [200, 201] or koniec > LIMIT:
            print("Błąd")
            return

        acc_id = r_post.json()["id"]

        start = time.time()
        r_del = requests.delete(f"{URL}/accounts/{acc_id}", timeout=LIMIT)
        koniec = time.time() - start

        if r_del.status_code not in [200, 204] or koniec > LIMIT:
            print("Błąd")
            return

    print("Test 1: Prawidłowo")


def test_2_przelewy_i_saldo():
    r_acc = requests.post(f"{URL}/accounts", json={"name": "User1", "balance": 0}, timeout=LIMIT)

    if r_acc.status_code not in [200, 201]:
        print("Błąd")
        return

    acc_id = r_acc.json()["id"]

    for i in range(100):
        start = time.time()
        r_trans = requests.post(f"{URL}/accounts/{acc_id}/transfers", json={"amount": 10}, timeout=LIMIT)
        koniec = time.time() - start

        if r_trans.status_code not in [200, 201] or koniec > LIMIT:
            print("Błąd przelewu")
            return

    r_final = requests.get(f"{URL}/accounts/{acc_id}", timeout=LIMIT)

    if r_final.status_code != 200:
        print("Błąd")
        return

    saldo = r_final.json()["balance"]

    if saldo == 1000:
        print(f"Test 2: Prawidłowo, saldo wynosi {saldo}")
    else:
        print(f"Test 2: Błąd, saldo wynosi {saldo}, a powinno być 1000")

test_1_stworz_usun()
test_2_przelewy_i_saldo()
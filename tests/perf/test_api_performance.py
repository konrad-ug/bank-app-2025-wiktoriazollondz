import requests
import time

URL = "http://localhost:3000"
LIMIT = 0.5  #0.5 sek

def test_1_stworz_usun():
    for i in range(100):
        #tworzenie
        start = time.time()
        r_post = requests.post(f"{URL}/accounts", json={"name": "Test"}, timeout=LIMIT)
        koniec = time.time() - start

        #sprawdzenie kodu i czasu
        if r_post.status_code not in [200, 201] or koniec > LIMIT:
            print("Błąd")
            return

        acc_id = r_post.json()["id"]

        #usuwanie
        start = time.time()
        r_del = requests.delete(f"{URL}/accounts/{acc_id}", timeout=LIMIT)
        koniec = time.time() - start

        if r_del.status_code not in [200, 204] or koniec > LIMIT:
            print("Błąd")
            return

    print("Test 1: Prawidłowo")


def test_2_przelewy_i_saldo():
    r_acc = requests.post(f"{URL}/accounts", json={"name": "User1", "balance": 0})
    acc_id = r_acc.json()["id"]

    for i in range(100):
        start = time.time()
        r_trans = requests.post(f"{URL}/accounts/{acc_id}/transfers", json={"amount": 10}, timeout=LIMIT)
        koniec = time.time() - start

        if r_trans.status_code not in [200, 201] or koniec > LIMIT:
            print(f"Błąd przelewu")
            return

    #sprawdzenie salda na koniec
    r_final = requests.get(f"{URL}/accounts/{acc_id}")
    saldo = r_final.json()["balance"]

    if saldo == 1000:
        print(f"Test 2: Prawidłowo, saldo wynosi {saldo}")
    else:
        print(f"Test 2: Błąd, saldo wynosi {saldo}, a powinno być 1000")


#wywołanie funkcji
test_1_stworz_usun()
test_2_przelewy_i_saldo()
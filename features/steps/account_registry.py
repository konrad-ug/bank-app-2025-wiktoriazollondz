from behave import *
import requests

URL = "http://localhost:5000"

@step('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, name, last_name, pesel):
    json_body = {
        "name": name,
        "surname": last_name,
        "pesel": pesel
    }
    response = requests.post(URL + "/api/accounts", json=json_body)
    assert response.status_code == 201, f"Błąd tworzenia konta! Status: {response.status_code}, Treść: {response.text}"

@step('Account registry is empty')
@step('Acoount registry is empty')
def clear_account_registry(context):
    response = requests.get(URL + "/api/accounts")
    accounts = response.json()
    for account in accounts:
        requests.delete(URL + f"/api/accounts/{account['pesel']}")

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/api/accounts")
    assert len(response.json()) == int(count)

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 404

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    json_body = { field: value }
    response = requests.patch(URL + f"/api/accounts/{pesel}", json=json_body)
    assert response.status_code == 200

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.json()[field] == value


@when('I transfer "{amount}" from account "{src_pesel}" to "{dst_pesel}"')
def transfer_money(context, amount, src_pesel, dst_pesel):
    amount_int = int(amount)
    if src_pesel == "000":
        payload = {"type": "incoming", "amount": amount_int}
        response = requests.post(f"{URL}/api/accounts/{dst_pesel}/transfer", json=payload)
        assert response.status_code == 200, f"Initial deposit failed: {response.text}"
    else:
        out_payload = {"type": "outgoing", "amount": amount_int}
        out_resp = requests.post(f"{URL}/api/accounts/{src_pesel}/transfer", json=out_payload)
        assert out_resp.status_code == 200, f"Outgoing transfer failed: {out_resp.text}"

        in_payload = {"type": "incoming", "amount": amount_int}
        in_resp = requests.post(f"{URL}/api/accounts/{dst_pesel}/transfer", json=in_payload)
        assert in_resp.status_code == 200, f"Incoming transfer failed: {in_resp.text}"

@then('Account with pesel "{pesel}" has balance equal to "{balance}"')
def check_balance(context, pesel, balance):
    response = requests.get(f"{URL}/api/accounts/{pesel}")
    assert response.status_code == 200
    actual_balance = response.json().get("balance")
    assert float(actual_balance) == float(balance), f"Expected {balance}, got {actual_balance}"

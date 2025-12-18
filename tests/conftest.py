import pytest
from unittest.mock import patch

from src.accounts_registry import AccountsRegistry
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from src.account import Account

@pytest.fixture
def personal_acc():
    return PersonalAccount("Jan", "Kowalski", None, 0)

@pytest.fixture
def comp_acc():
    return CompanyAccount("Tech Solutions", "1234567890")

@pytest.fixture
def acc():
    return Account()

@pytest.fixture
def acc_reg():
    return AccountsRegistry()

@pytest.fixture
def api_acc():
    return {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "12345678901"
    }

@pytest.fixture
def mock_mf_ok(mocker):
    mock = mocker.patch("src.company_account.requests.get")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {
        "result": {"subject": {"statusVat": "Czynny"}}
    }
    return mock
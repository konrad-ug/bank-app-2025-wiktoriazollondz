import pytest
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
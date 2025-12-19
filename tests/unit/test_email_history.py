import pytest
from unittest.mock import MagicMock
from src.company_account import CompanyAccount
from datetime import datetime
from src.personal_account import PersonalAccount

class TestEmailHistory:
    @pytest.fixture
    def today(self):
        return datetime.today().strftime("%Y-%m-%d")

    def test_send_history_personal_success(self, today):
        personal_acc = PersonalAccount("Jan", "Kowalski", "12345678901")
        personal_acc.history = [100, -50]
        mock_smtp = MagicMock()
        mock_smtp.send.return_value = True

        res = personal_acc.send_history_via_email("test@mail.pl", mock_smtp)

        assert res is True
        mock_smtp.send.assert_called_once_with(
            f"Account Transfer History {today}",
            "Personal account history: [100, -50]",
            "test@mail.pl"
        )

    def test_send_history_company_fail(self, mocker, today):
        mock_api = mocker.patch("src.company_account.requests.get")
        mock_api.return_value.status_code = 200
        mock_api.return_value.json.return_value = {
            "result": {"subject": {"statusVat": "Czynny"}}
        }

        account = CompanyAccount("Tech Solutions", "1234567890")
        account.history = [5000, -1000]

        mock_smtp = MagicMock()
        mock_smtp.send.return_value = False

        email = "szef@firma.pl"
        res = account.send_history_via_email(email, mock_smtp)

        assert res is False
        mock_smtp.send.assert_called_once_with(
            f"Account Transfer History {today}",
            "Company account history: [5000, -1000]",
            email
        )
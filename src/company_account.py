from src.account import Account
import os
from datetime import datetime
import requests
from smtp.smtp import SMTPClient

class CompanyAccount(Account):
    def __init__(self, company_name: str, nip: str):
        super().__init__()
        self.company_name = company_name
        self.set_nip(nip)

    def set_nip(self, nip):
        if isinstance(nip, str) and len(nip) == 10 and nip.isdigit():
            self.nip = nip
            if not self.is_company_active(nip):
                raise ValueError("Company not registered!!")
        else:
            self.nip = "Invalid"

    def express_transfer(self, amount: float) -> None:
        fee = 5.0
        if amount > 0 and (self.balance + fee) >= amount:
            self.balance -= (amount + fee)

    def take_loan(self, amount: float):
        if self.balance >= 2 * amount and -1775 in self.history:
            self.balance += amount
            return True

        return False

    def is_company_active(self, nip):
        today_date = datetime.today().strftime("%Y-%m-%d")
        base_url = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl")
        url = f"{base_url}/api/search/nip/{nip}?date={today_date}"

        try:
            response = requests.get(url)
            print(f"MF API Response: {response.status_code}, {response.text}")

            if response.status_code != 200:
                return False

            data = response.json()
            result = data.get("result", {})
            subject = result.get("subject")

            if subject and subject.get("statusVat") == "Czynny":
                return True
        except Exception as e:
            print(f"API Error: {e}")
            return False

        return False

    def send_history_via_email(self, email_address, smtp_client: SMTPClient):
        today_date = datetime.today().strftime("%Y-%m-%d")
        subject = f"Account Transfer History {today_date}"
        content = f"Company account history: {self.history}"

        return smtp_client.send(subject, content, email_address)
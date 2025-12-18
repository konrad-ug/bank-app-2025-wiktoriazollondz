from src.account import Account
import os
from datetime import datetime
import requests

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
        if os.getenv("DISABLE_MF_VALIDATION") == "true":
            return True

        today_date = datetime.today().strftime("%Y-%m-%d")
        base_url = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl")

        if len(nip) != 10:
            return True

        url = f"{base_url}/api/search/nip/{nip}?date={today_date}"
        response = requests.get(url)

        if response.status_code != 200:
            return False

        data = response.json() or {}
        subject = data.get("result", {}).get("subject")

        if not subject:
            return False

        return subject.get("statusVat") == "Czynny"

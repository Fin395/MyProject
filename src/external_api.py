import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction_info: dict) -> Any:
    if transaction_info["operationAmount"]["currency"]["code"] == "RUB":
        return transaction_info["operationAmount"]["amount"]
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": transaction_info["operationAmount"]["amount"],
            "from": transaction_info["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        if response.status_code == 200:
            transaction_amount = response.json()
            return transaction_amount["result"]
        else:
            return None

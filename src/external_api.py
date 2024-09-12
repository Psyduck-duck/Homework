import os

import requests
from dotenv import load_dotenv

load_dotenv()
apilayer_API_KEY = os.getenv("apilayer_API_KEY")


def converte_currency(base_carrency: str, end_carrency: str, amount: float) -> float:
    """Функция конвертирует валюту по актуальному курсу"""

    headers = {"apikey": apilayer_API_KEY}
    # url = "https://api.apilayer.com/exchangerates_data/convert"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={end_carrency}&from={base_carrency}&amount={amount}"
    responce = requests.get(url, headers=headers)
    if responce.status_code != 200:
        raise ValueError("Check URL")
    return responce.json()["result"]


if __name__ == "__main__":
    print(converte_currency("USD", "RUB", 10))

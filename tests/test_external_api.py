import json
import os
from unittest.mock import Mock, patch

import pytest
import requests
from dotenv import load_dotenv

from src.external_api import converte_currency

load_dotenv()
apilayer_API_KEY = os.getenv("apilayer_API_KEY")


@patch("requests.get")
def test_converte_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 30}
    headers = {"apikey": apilayer_API_KEY}
    assert converte_currency("USD", "RUB", 1) == 30
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers=headers
    )


@patch("requests.get")
def test_converte_currency_failed_request(mock_get):
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {"result": 30}
    headers = {"apikey": apilayer_API_KEY}
    with pytest.raises(ValueError):
        converte_currency("USD", "RUB", 1)

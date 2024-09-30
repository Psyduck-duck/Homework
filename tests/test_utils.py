import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.utils import get_amount_transaction, get_operations_data

# from src.external_api import converte_currency

load_dotenv()
apilayer_API_KEY = os.getenv("apilayer_API_KEY")


@patch("json.load")
def test_get_operations_data(mock_load):
    mock_load.return_value = [{1: 1}, {2: 2}]
    assert get_operations_data("operations.json") == [{1: 1}, {2: 2}]


@patch("json.load")
def test_get_operations_data_with_None(mock_load):
    mock_load.return_value = None
    assert get_operations_data("operations.json") == []


@patch("json.load")
def test_get_operations_data_with_str(mock_load):
    mock_load.return_value = "str"
    assert get_operations_data("operations.json") == []


def test_get_operations_data_invalid_path():
    assert get_operations_data("None.json") == []


def test_get_amount_transaction():
    assert get_amount_transaction("operations.json", 587085106) == 48223.05


@patch("requests.get")
def test_get_amount_transaction_with_USD(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 30}
    headers = {"apikey": apilayer_API_KEY}
    assert get_amount_transaction("operations.json", 41428829) == 30  # 8221.37 USD
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )


def test_get_amount_transaction_unvalid_id():
    with pytest.raises(KeyError):
        get_amount_transaction("operations.json", 123)


@patch("src.utils.get_operations_data")
def test_get_amount_transaction_invalid_operations_data(mock_get):
    mock_get.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    # "code": "RUB"
                },
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    with pytest.raises(KeyError):
        get_amount_transaction("operations.json", 441945886)

import os
import json

from external_api import converte_currency


def get_operations_data(filename: str) -> list:
    """Функция принимает название файла в дирректории Data и возвращает данные"""

    with open(f"data/{filename}", "r", encoding="utf-8") as file:
        try:
            operations_data = json.load(file)
        except Exception:
            return []
        if type(operations_data) != list:
            return []

    return operations_data


def get_amount_transaction(id: int) -> float:
    """Фунция принимает транзакцию и возвращает сумму транзакции в рублях"""

    operations_data = get_operations_data("operations.json")
    for operation in operations_data:
        if operation["id"] == id:
            amount = operation["operationAmount"]["amount"]
            currency_code = operation["operationAmount"]["currency"]["code"]
            if currency_code != "RUB":
                result = converte_currency(currency_code, "RUB", amount)
                return result
            return amount

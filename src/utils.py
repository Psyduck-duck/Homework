import json
import os

from src.external_api import converte_currency


def get_operations_data(filename: str) -> list:
    """Функция принимает название файла в дирректории Data и возвращает данные"""

    path_to_file = f"../data/{filename}"

    try:
        with open(f"{path_to_file}", "r", encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
            except Exception:
                return []
            if type(operations_data) != list:
                return []
    except FileNotFoundError:
        return []

    return operations_data


def get_amount_transaction(id: int) -> float:
    """Фунция принимает транзакцию и возвращает сумму транзакции в рублях"""

    operations_data = get_operations_data("operations.json")
    id_in_data = False
    for operation in operations_data:
        if operation["id"] == id:
            id_in_data = True
            amount = operation["operationAmount"]["amount"]
            currency_code = operation["operationAmount"]["currency"]["code"]
            if currency_code != "RUB":
                result = converte_currency(currency_code, "RUB", amount)
                return result
            return float(amount)
    if not id_in_data:
        raise KeyError("ID not found")


if __name__ == "__main__":
    pass

    #print(get_operations_data("operations.json"))
    print(type(get_amount_transaction(142264268)))

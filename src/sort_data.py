import re
from collections import Counter
from src.pandas_work import read_csv_file

from src.pandas_work import read_csv_file


def sort_operation_data_by_description(operations_data: list[dict], description: str) -> list[dict]:
    """Функция принимает список словарей с данными о транзакциях и фильтрует по описанию"""
    sorted_list = []
    pattern = fr"{description.lower()}"
    for operation in operations_data:
        match = re.search(pattern, str(operation.get("description")).lower())
        if match:
            sorted_list.append(operation)

    return sorted_list


def counter_operations_data(operations_data: list[dict], pattern_list: list) -> dict:
    """Функция принимает список словарей с данными о транзакциях и список искомых совпадений,
     возвращает подсчет уникальных совпадений"""
    new_list = []
    for operation in operations_data:
        for pattern in pattern_list:
            pattern = fr"{pattern.lower()}"
            match = re.search(pattern, str(operation.get("description")).lower())
            if match:
                new_list.append(operation.get("description"))

    return Counter(new_list)

import re
from collections import Counter
from collections import defaultdict

from src.pandas_work import read_csv_file


def sort_operation_data_by_description(operations_data: list[dict], description: str) -> list[dict]:
    """Функция принимает список словарей с данными о транзакциях и фильтрует по описанию"""
    #pattern = re.compile(description)
    sorted_list = []
    for operation in operations_data:
        if description.lower() in str(operation["description"]).lower():
            sorted_list.append(operation)

    return sorted_list


def counter_operations_data(operations_data: list[dict], category_list: list) -> dict:
    """Функция принимает список словарей с данными о транзакциях, возвращает подсчет транзакций"""
    op_dict = defaultdict(int)
    for operation in operations_data:
        category = str(operation["description"])
        if category in category_list:
            op_dict[category] += 1

    return op_dict


def Counter_operations_data(operation_data):
    """Функция возвращает подсчет для всех категорий в списке операций"""
    categorys_list = []
    for operation in operation_data:
        categorys_list.append(operation["description"])

    return Counter(categorys_list)

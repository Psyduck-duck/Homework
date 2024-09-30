import datetime

import pandas as pd

from src.pandas_work import read_csv_file, read_excel_file
from src.sort_data import sort_operation_data_by_description
from src.utils import get_operations_data
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date


def main():
    print(
        """Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    answer = 0
    while answer not in ["1", "2", "3"]:
        answer = input("Введите ответ: ")

    if answer == "1":
        print("Для обработки выбран JSON-файл.")
    elif answer == "2":
        print("Для обработки выбран CSV-файл.")
    elif answer == "3":
        print("Для обработки выбран XLSX-файл.")

    # operation_data = get_operations_data("operations.json")

    choices = ["EXECUTED", "CANCELED", "PENDING"]
    choice = ""
    while choice not in choices:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        choice = input("Введите ответ: ").upper()

        if choice not in choices:
            print(f"Статус операции '{choice}' недоступен.")

    print(f"Операции отфильтрованы по статусу '{choice}'")

    print("Отсортировать операции по дате? Да/Нет")
    sort_answer = ""
    sort_data = False
    sort_revers = False
    while sort_answer not in ["да", "нет"]:
        sort_answer = input("Введите ответ: ").lower()
        if sort_answer == "да":
            sort_data = True
            print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
            sort_course = ""
            while sort_course not in ["по возрастанию", "по убыванию"]:
                sort_course = input("Введите ответ: ").lower()
                if sort_course == "по убыванию":
                    sort_revers = True

    print("Программа: Выводить только рублевые тразакции? Да/Нет")
    is_currency_rub = ""
    is_currency_rub_bool = False
    while is_currency_rub not in ["да", "нет"]:
        is_currency_rub = input("Введите ответ: ").lower()
        if is_currency_rub == "да":
            is_currency_rub_bool = True

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_description = ""
    sort_by_description_words = ""
    sort_by_description_bool = False
    while sort_by_description not in ["да", "нет"]:
        sort_by_description = input("Введите ответ: ").lower()
        if sort_by_description == "да":
            sort_by_description_bool = True
            sort_by_description_words = input("Введите описание: ")

    operations_data = []

    if answer == "1":
        operations_data = get_operations_data("operations.json")

    elif answer == "2":
        operations_data = read_csv_file("data/transactions.csv")

    elif answer == "3":
        operations_data = read_excel_file("data/transactions_excel.xlsx")

    sorted_operations_data = filter_by_state(operations_data, choice)

    if sort_data:
        sorted_operations_data = sort_by_date(sorted_operations_data, sort_revers)

    if is_currency_rub_bool:
        empty_list = []
        if answer == "1":
            for operation in sorted_operations_data:
                if operation["operationAmount"]["currency"]["code"] == "RUB":
                    empty_list.append(operation)
            sorted_operations_data = empty_list

        else:
            empty_list = []
            for operation in sorted_operations_data:
                if operation.get("currency_code") == "RUB":
                    empty_list.append(operation)
            sorted_operations_data = empty_list

    if sort_by_description:
        sorted_operations_data = sort_operation_data_by_description(sorted_operations_data, sort_by_description_words)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(sorted_operations_data)}")
    if answer == "1":
        for operation in sorted_operations_data:
            print(
                f"""{get_date(operation.get("date"))} {operation.get("description")}
{mask_account_card(operation.get("from"))} -> {mask_account_card(operation.get("to"))}
Сумма: {operation.get("operationAmount").get("amount")},  Валюта: {operation.get("operationAmount").get("currency").get("code")}
    """
            )
    else:
        for operation in sorted_operations_data:
            print(
                f"""{get_date(operation.get("date"))} {operation.get("description")}
{mask_account_card(operation.get("from"))} -> {mask_account_card(operation.get("to"))}
Сумма: {operation.get("amount")}, Валюта: {operation.get("currency_code")}
    """
            )

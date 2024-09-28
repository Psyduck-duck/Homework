import os
import json
import logging

from src.external_api import converte_currency
from data.__init__ import PATH_TO_DATA_DIRECTORY

logging.basicConfig(
    level=logging.DEBUG,
    filename="../logs/utils.log",
    format="%(asctime)s %(filename)s %(name)s %(levelname)s: %(message)s",
    encoding="utf8",
    filemode="w",
)

get_operations_data_logger = logging.getLogger("get_data_loger")
get_amount_transaction_logger = logging.getLogger("get_amount_logger")


def get_operations_data(filename: str) -> list:
    """Функция принимает название файла в дирректории Data и возвращает данные"""

    get_operations_data_logger.info(f"Задается путь до {filename}")

    path_to_file = os.path.join(PATH_TO_DATA_DIRECTORY, filename)

    try:
        get_operations_data_logger.info(f"Попытка открыть {filename}")

        with open(f"{path_to_file}", "r", encoding="utf-8") as file:

            try:
                get_operations_data_logger.info(f"Попытка перевести {filename} в json формат")

                operations_data = json.load(file)

            except Exception as e:
                get_operations_data_logger.error(f"Вызов исключения {e}, возвращается пустой список")

                return []

            if type(operations_data) != list:

                get_operations_data_logger.warning("Тип данные не список, возвращаетя пустой список")

                return []

    except FileNotFoundError as e:

        get_operations_data_logger.error(f"Вызвано исключение {e}, возвращается пустой список")

        return []

    get_operations_data_logger.info("Функция завершает работу")

    return operations_data


def get_amount_transaction(filename: str, id: int) -> float:
    """Фунция принимает транзакцию и возвращает сумму транзакции в рублях"""

    get_amount_transaction_logger.info(f"Попытка получить данные из {filename}")

    operations_data = get_operations_data(filename)
    operations_data_id = (operation for operation in operations_data if operation.get("id") == id)

    try:
        operation = next(operations_data_id)
    except StopIteration:
        get_amount_transaction_logger.error("ID not found")

        raise KeyError("ID not found")

    get_amount_transaction_logger.info("Получение суммы операции и кода валюты")

    amount = operation["operationAmount"]["amount"]
    currency_code = operation["operationAmount"]["currency"]["code"]

    if currency_code != "RUB":

        get_amount_transaction_logger.info("Перевод валюты в рубли по актуальному курсу")

        try:

            result = converte_currency(currency_code, "RUB", amount)
            result = round(result, 2)

        except Exception as e:

            get_amount_transaction_logger.error(f"Вызов исключения {e}, проблемы с обработкой валюты")

        get_amount_transaction_logger.info("Возвращение результата, завершение работы функции")

        return result

    get_amount_transaction_logger.info("Возвращенеи результата, завершение работы функции")
    return float(amount)


print(get_operations_data("operations.json"))
#print(get_amount_transaction("operations.json",1))
#print(get_amount_transaction("operations.json",104807525))
#print(PATH_TO_DATA_DIRECTORY)

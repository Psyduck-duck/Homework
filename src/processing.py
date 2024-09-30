import datetime

from src.widget import get_date


def filter_by_state(operation_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению"""

    new_list = []

    for dict in operation_list:

        if "state" in dict:

            if dict["state"] == state:
                new_list.append(dict)

    return new_list


def sort_by_date(operation_list: list, reverse_: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате (date)"""

    try:
        sorted_list = sorted(
            operation_list,
            key=lambda x: datetime.datetime.strptime(get_date(x["date"]), "%d.%m.%Y"),
            reverse=reverse_,
        )
    except ValueError:
        raise ValueError("date not found")
    return sorted_list

from src.widget import get_data


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

    sorted_list = sorted(
        operation_list, key=lambda x: ".".join(reversed((get_data(x["date"]).split(".")))), reverse=reverse_
    )

    return sorted_list

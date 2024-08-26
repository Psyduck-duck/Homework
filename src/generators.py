def filter_by_currency(operation_list: list, currency: str):
    """Функция возвращает генератор сортирующий список словарей по указанной валюте"""
    return (x for x in operation_list if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(operation_list):
    """Функция возвращает генератор показывающий информацию об операциях"""
    # return (x['description'] for x in operation_list)
    for x in operation_list:
        yield x["description"]


def card_number_generator(start: int, stop: int):
    """Функция генерирует номер карты формата ХХХХ ХХХХ ХХХХ ХХХХ от num1 до num2"""
    if start < 0 or stop < 0:
        raise ValueError("Некорректные параметры")

    if start <= stop:
        for i in range(stop - start + 1):
            card_number = str("0" * (16 - len(str(start))) + str(start + i))
            card_number_mask = (
                card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:]
            )
            yield card_number_mask

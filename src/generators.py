

def filter_by_currency(operation_list: list, currency: str):
    """Функция возвращает генератор сортирующий список словарей по указанной валюте"""
    return (x for x in operation_list if x['operationAmount']['currency']['code'] == currency)


def transaction_descriptions(operation_list):
    """Функция возвращает генератор показывающий информацию об операциях"""
    return (x['description'] for x in operation_list)


def card_number_generator(num1: int, num2: int):
    """Функция генерирует номер карты формата ХХХХ ХХХХ ХХХХ ХХХХ от num1 до num2"""
    if num2 < num1:
        return "Некорректные параметры"
    if num1 <= num2:
        for i in range(num2 - num1 + 1):
            card_number = str('0' * (16 - len(str(num1))) + str(num1 + i))
            card_number_mask = card_number[:4] + ' ' + card_number[4: 8] + ' ' + card_number[8: 12] + ' ' + card_number[12:]
            yield card_number_mask

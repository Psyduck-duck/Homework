import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_data: str) -> str:
    """Принимает информация о карте или счете
    и возвращает соответсвующую маску"""

    card_data_list = card_data.split()
    new_card_data_list = []
    mask_number = ""

    for card_data_list_item in card_data_list:

        if card_data_list_item.isalpha():
            new_card_data_list.append(card_data_list_item)

        else:

            if len(str(card_data_list_item)) == 16:
                mask_number = get_mask_card_number(int(card_data_list_item))

            elif len(str(card_data_list_item)) == 20:
                mask_number = get_mask_account(int(card_data_list_item))

            else:
                raise ValueError("Некорректный номер карты или счета")

    return " ".join(new_card_data_list) + " " + mask_number


def get_date(time_data: str) -> str:
    """Принимает время формата 2024-03-11T02:26:18.671407
    и возвращает в формате 11.03.2024"""

    pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

    match = pattern.match(time_data)

    if int(match.group(3)) < 0 or int(match.group(3)) > 31:
        raise ValueError ("Incorrect date")
    if int(match.group(2)) < 1 or int(match.group(2)) > 12:
        raise ValueError("Incorrect date")
    if int(match.group(1)) < 0:
        raise ValueError("Incorrect date")
    return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"

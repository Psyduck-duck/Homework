from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_data: str) -> str:
    """Принимает информация о карте или счете
    и возвращает соответсвующую маску"""
    card_data_list = card_data.split()
    new_card_data_list = []
    mask_number = ''
    for card_data_list_item in card_data_list:
        if card_data_list_item.isalpha():
            new_card_data_list.append(card_data_list_item)
        else:
            if len(str(card_data_list_item)) == 16:
                mask_number = get_mask_card_number(card_data_list_item)
            elif len(str(card_data_list_item)) == 20:
                mask_number = get_mask_account(card_data_list_item)
    return " ".join(new_card_data_list) + ' ' + mask_number


data = ['Maestro 1596837868705199',
'Счет 64686473678894779589',
'MasterCard 7158300734726758',
'Счет 35383033474447895560',
'Visa Classic 6831982476737658',
'Visa Platinum 8990922113665229',
'Visa Gold 5999414228426353',
'Счет 73654108430135874305']

if __name__ == '__main__':
    for i in data:
        print(mask_account_card(i))

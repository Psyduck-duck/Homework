from masks import get_mask_account, get_mask_card_number


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
                mask_number = get_mask_card_number(int(card_data_list_item))
            elif len(str(card_data_list_item)) == 20:
                mask_number = get_mask_account(int(card_data_list_item))
    return " ".join(new_card_data_list) + ' ' + mask_number


def get_data(time_data: str) -> str:
    """Принимает время формата 2024-03-11T02:26:18.671407
     и возвращает в формате 11.03.2024"""
    new_time_data = time_data[8:10] + '.' + time_data[5:7] + '.' + time_data[0:4]
    return new_time_data


if __name__ == '__main__':
    data_tests = ['Maestro 1596837868705199',
                  'Счет 64686473678894779589',
                  'MasterCard 7158300734726758',
                  'Счет 35383033474447895560',
                  'Visa Classic 6831982476737658',
                  'Visa Platinum 8990922113665229',
                  'Visa Gold 5999414228426353',
                  'Счет 73654108430135874305']
    for i in data_tests:
        print(mask_account_card(i))

    print(get_data('2024-03-11T02:26:18.671407'))

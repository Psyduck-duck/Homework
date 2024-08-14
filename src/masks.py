def get_mask_card_number(num_card: int) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(str(num_card)) == 16:
        return str(num_card)[0:4] + " " + str(num_card)[4:6] + "** **** " + str(num_card)[-4:]
    else:
        return "Некорректный номер карты!"


def get_mask_account(num_account: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(str(num_account)) == 20:
        return "**" + str(num_account)[-4:]
    else:
        return "Некорректный номер счета!"


if __name__ == '__main__':
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(12345678901234567890))

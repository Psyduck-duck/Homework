def get_mask_card_number(num_card: int) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if type(num_card) != int:
        raise TypeError('Некорректный формат данных!')

    if len(str(num_card)) == 16:
        return str(num_card)[0:4] + " " + str(num_card)[4:6] + "** **** " + str(num_card)[-4:]

    else:
        raise ValueError("Некорректный номер карты!")


def get_mask_account(num_account: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if type(num_account) != int:
        raise TypeError('Некоректный формат данных!')

    if len(str(num_account)) == 20:
        return "**" + str(num_account)[-4:]

    else:
        raise ValueError("Некорректный номер счета!")

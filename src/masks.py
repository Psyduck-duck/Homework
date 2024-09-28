import logging
import os

from logs.__init__ import PATH_TO_LOGS_DIRECTORY

logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(PATH_TO_LOGS_DIRECTORY, "masks.log"),
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    encoding="utf8",
    filemode="w",
)

mask_card_logger = logging.getLogger("masks_card_loger")
mask_account_loger = logging.getLogger("masks_account_logger")


def get_mask_card_number(num_card: int) -> str:
    """принимает на вход номер карты и возвращает ее маску"""

    mask_card_logger.info(f"Попытка обработать карту с номером: {num_card}")

    if type(num_card) is not int:

        mask_card_logger.error(f"Вызов исключения 'TypeError', номер карты не целое число ")

        raise TypeError("Некорректный формат данных!")

    if len(str(num_card)) == 16:

        mask_card_logger.info("Создана маска для номера карты, функция завершает работу")

        return str(num_card)[0:4] + " " + str(num_card)[4:6] + "** **** " + str(num_card)[-4:]

    else:

        mask_card_logger.error("Вызов исключения 'ValueError', номер карты != 16 символам")

        raise ValueError("Некорректный номер карты!")


def get_mask_account(num_account: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    mask_account_loger.info(f"Попытка создать маску для номера счета {num_account}")

    if type(num_account) is not int:

        mask_account_loger.error("Вызов исключения 'TypeError', номер счета не целое число")

        raise TypeError("Некоректный формат данных!")

    if len(str(num_account)) == 20:

        mask_account_loger.info("Создана маска для номера счета, функция завершает работу")

        return "**" + str(num_account)[-4:]

    else:

        mask_account_loger.error("Вызов исключения 'ValueError', номер счета != 20 символам")

        raise ValueError("Некорректный номер счета!")

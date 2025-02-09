import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "masks.log")


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(logs_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    card_number_length = len(card_number)
    if card_number_length != 16:
        logger.error("Ошибка: неверное количество знаков")
        raise ValueError("Номер карты должен состоять из 16 цифр")
    else:
        logger.info("Происходит разбивка номера на символы")
        splited_card_number = card_number.split()
        for name_item in splited_card_number:
            if name_item.isdigit():
                logger.info("Происходит маскировка номера карты")
                masked_card = f"{name_item[0:4]} {name_item[4:6]}** **** {name_item[-4:]}"
            else:
                logger.error("Ошибка: нечисловые символы в номере карты")
                raise TypeError("В номере карты присутствуют нечисловые символы")
        return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    account_number_length = len(account_number)
    if account_number_length != 20:
        logger.error("Ошибка: неверное количество знаков")
        raise ValueError("Номер счета должен состоять из 20 цифр")
    else:
        logger.info("Происходит разбивка номера на символы")
        splited_account_number = account_number.split()

        for name_item in splited_account_number:
            if name_item.isdigit():
                logger.info("Происходит маскировка номера счета")
                masked_account = f"**{account_number[-4:]}"
            else:
                logger.error("Ошибка: нечисловые символы в номере счета")
                raise TypeError("В номере карты присутствуют нечисловые символы")
        return masked_account

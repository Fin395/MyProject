def get_mask_card_number(card_number: str) -> str:
    """Функция,которая принимает на вход номер карты и возвращает ее маску"""
    splited_card_number = card_number.split()
    for name_item in splited_card_number:
        if name_item.isdigit():
            masked_card = f"{name_item[0:4]} {name_item[4:6]}** **** {name_item[-4:]}"
            return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    splited_account_number = account_number.split()
    for name_item in splited_account_number:
        if name_item.isdigit():
            masked_account = f"**{account_number[-4:]}"
            return masked_account

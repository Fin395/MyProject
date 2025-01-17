def get_mask_card_number(card_number: str) -> str:
    """Функция,которая принимает на вход номер карты и возвращает ее маску"""
    card_number_length = len(card_number)
    if card_number_length != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    else:
        splited_card_number = card_number.split()
        for name_item in splited_card_number:
            if name_item.isdigit():
                masked_card = f"{name_item[0:4]} {name_item[4:6]}** **** {name_item[-4:]}"
            else:
                raise TypeError("В номере карты присутствуют нечисловые символы")
        return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    account_number_length = len(account_number)
    if account_number_length != 20:
        raise ValueError("Номер счета должен состоять из 20 цифр")
    else:
        splited_account_number = account_number.split()
        for name_item in splited_account_number:
            if name_item.isdigit():
                masked_account = f"**{account_number[-4:]}"
            else:
                raise TypeError("В номере карты присутствуют нечисловые символы")
        return masked_account

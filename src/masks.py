def get_mask_card_number(card_number: str) -> str:
    """Функция,которая принимает на вход номер карты и возвращает ее маску"""
    list_for_card_number = []
    new_list_for_card_number = []
    count = 0

    for number in card_number:
        list_for_card_number.append(number)

    list_for_card_number[6:12] = "******"
    for character in list_for_card_number:
        count += 1
        new_list_for_card_number.append(character)
        if count != 16:
            if count % 4 == 0:
                new_list_for_card_number.append(" ")
        else:
            break
    visible_card_number = ",".join(new_list_for_card_number).replace(",", "")
    return visible_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    list_for_account_number = []

    for number in account_number:
        list_for_account_number.append(number)

    account_number_formated = list_for_account_number[-6:]
    account_number_formated[0:2] = "**"
    visible_account_number = "".join(account_number_formated)
    return visible_account_number

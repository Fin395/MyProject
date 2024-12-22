from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(card_or_account_data: str) -> str:
    """ Функция, которая обрабатывает информацию о картах и счетах """
    splited_card_or_account_data = card_or_account_data.split()
    if "счет" in card_or_account_data.lower():
        for name_item in splited_card_or_account_data:
            if name_item.isdigit():
                masked_data = card_or_account_data.replace(name_item, get_mask_account(card_or_account_data))
    else:
        for name_item in splited_card_or_account_data:
            if name_item.isdigit():
                masked_data = card_or_account_data.replace(name_item, get_mask_card_number(card_or_account_data))
    return masked_data
            
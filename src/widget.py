from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_data: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""
    splited_card_or_account_data = card_or_account_data.split()
    number = splited_card_or_account_data[-1]
    if "счет" in card_or_account_data.lower():
        masked_data = card_or_account_data.replace(number, get_mask_account(number))
    else:
        masked_data = card_or_account_data.replace(number, get_mask_card_number(number))
    return masked_data


def get_date(date_to_fix: str) -> str:
    """Функция возвращает дату в корректном формате"""
    date_list = []
    sliced_date = date_to_fix[0:10]
    sliced_date_splited = sliced_date.split("-")
    for number in sliced_date_splited[::-1]:
        date_list.append(number)
    date_in_required_format = ".".join(date_list)
    return date_in_required_format

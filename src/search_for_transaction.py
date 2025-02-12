import re
from src.transactions import get_transactions_from_csv


def filter_by_search_string(list_of_transactions: list[dict], search_string: str) -> list[dict]:
    """ Функция ищет список транзакций по заданной строке """
    filtered_transactions = []
    pattern = re.compile(f"{search_string}")
    for banking_transaction in list_of_transactions:
        description = banking_transaction["description"]
        match = pattern.search(f'{description}')
        if match:
            filtered_transactions.append(banking_transaction)
    return filtered_transactions


#list_to_process = get_transactions_from_csv(r"C:\Users\Sergei\OneDrive\Рабочий стол\УЧЕБА\transactions.csv")
#print(filter_by_search_string(list_to_process, "Перевод со счета на счет"))
import re
from collections import Counter


def search_for_transcations_by_string(list_of_transactions: list[dict], search_string: str) -> list[dict]:
    """Функция ищет список транзакций по заданной строке"""
    filtered_transactions = []
    pattern = re.compile(f"{search_string}")
    for banking_transaction in list_of_transactions:
        description = banking_transaction["description"]
        match = pattern.search(f"{description}")
        if match:
            filtered_transactions.append(banking_transaction)
    return filtered_transactions


def count_transactions_category(list_of_transactions: list[dict], list_of_categories: list[str]) -> dict:
    """Функция генерирует количество операций по заданным категориям"""
    new_dict = {}
    all_categories = []
    for transaction in list_of_transactions:
        all_categories.append(transaction.get("description"))
    counted_categories = Counter(all_categories)
    for key, value in counted_categories.items():
        if key in list_of_categories:
            new_dict[key] = value
    return new_dict

from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict]:
    """Функция возвращает итератор для получения транзакций, где валюта операции соответствует заданной"""
    for transaction in transactions:
        filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    for transaction in transactions:
        description = transaction["description"]
        yield description

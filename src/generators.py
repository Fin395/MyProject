from typing import Any, Generator

from src.json_path import logs_path
from src.transactions import get_transactions_from_csv
from src.utils import get_transactions


def filter_by_currency_json(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """Функция возвращает итератор для получения транзакций, где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions if "operationAmount" in transaction.keys() and transaction["operationAmount"]["currency"]["code"] == currency)


def filter_by_currency_csv_or_excel(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """ Функция возвращает итератор для получения транзакций, где валюта операции соответствует заданной """
    return (transaction for transaction in transactions if "currency_code" in transaction.keys() and transaction["currency_code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Функция создает итератор, который возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator:
    """Функциия создает генератор, который сгенерировать номера карт в заданном диапазоне"""
    for number in range(start, stop):
        yield (
            f"{str(number).zfill(16)[:4]}"
            f" {str(number).zfill(16)[4:8]} "
            f"{str(number).zfill(16)[8:12]} "
            f"{str(number).zfill(16)[12:]}"
        )

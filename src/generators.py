from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """Функция возвращает итератор для получения транзакций, где валюта операции соответствует заданной"""
    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


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

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(sample_transactions: list[dict]) -> None:
    """Тестирование корректной фильтрации, если валюта - USD"""
    result = filter_by_currency(sample_transactions, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_rub(sample_transactions: list[dict]) -> None:
    """Тестирование корректной фильтрации, если валюта - RUB"""
    result = filter_by_currency(sample_transactions, "RUB")
    assert next(result) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(result) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_no_currency(sample_transactions: list[dict]) -> None:
    """Тестирование случаев, когда заданная валюта отсутствует"""
    result = list(filter_by_currency(sample_transactions, "EURO"))
    assert result == []


def test_filter_by_currency_empty(sample_transactions_empty: list) -> None:
    """Тестирование случаев, когда список транзакций отсутствует"""
    result = list(filter_by_currency(sample_transactions_empty, "USD"))
    assert result == []


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    """Тестирование корректности описания каждой транзакции"""
    result = transaction_descriptions(sample_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_empty(sample_transactions_empty: list) -> None:
    """Тестирование работы при отсутствии входных данных"""
    result = list(transaction_descriptions(sample_transactions_empty))
    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1234123412341230, 1234123412341231, "1234 1234 1234 1230"),
        (1234123412341231, 1234123412341232, "1234 1234 1234 1231"),
        (1234123412341232, 1234123412341233, "1234 1234 1234 1232"),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    """Тестирование корректности формата и крайних значений"""
    generator = card_number_generator(start, stop)
    assert next(generator) == expected

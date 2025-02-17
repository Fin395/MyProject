from math import nan

import pytest


@pytest.fixture
def sample_card_and_account_data() -> list[str]:
    """Создаем фикстуру для тестирования"""
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def sample_transaction_data() -> list[dict]:
    """Создаем фикстуру для тестирования"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def similar_date_transactions() -> list[dict]:
    """Создаем фикстуру для тестирования по одинаковым датам"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:29.512364"},
    ]


@pytest.fixture
def sample_transactions_json() -> list[dict]:
    """Создаем фикстуру для тестирования"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def sample_transactions_empty() -> list:
    """Создаем фикстуру для тестирования"""
    return []


@pytest.fixture
def sample_transaction_csv() -> list[dict]:
    """Создаем фикстуру для тестирования функции get_transaction_amount"""
    return [
        {"id": 650703.0, "state": "EXECUTED", "amount": 16210.0, "currency_name": "Sol", "currency_code": "PEN"},
        {"id": 3598919.0, "state": "EXECUTED", "amount": 29740.0, "currency_name": "Peso", "currency_code": "COP"},
        {
            "id": 4234093.0,
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": 23182.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
        },
        {
            "id": 302564.0,
            "state": "EXECUTED",
            "date": "2021-01-05T12:20:25Z",
            "amount": 21153.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
        },
        {
            "id": 3463793.0,
            "state": "PENDING",
            "date": "2020-02-25T07:24:59Z",
            "amount": 17655.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
        },
        {
            "id": 2300960.0,
            "state": "PENDING",
            "date": "2020-05-10T21:18:59Z",
            "amount": 21170.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
        },
    ]


@pytest.fixture
def sample_transaction_in_rub() -> dict:
    """Создаем фикстуру для тестирования функции get_transaction_amount"""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }


@pytest.fixture
def sample_transaction_in_usd() -> dict:
    """Создаем фикстуру для тестирования функции get_transaction_amount"""
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    }


@pytest.fixture
def sample_transaction_with_nan() -> list[dict]:
    """Создаем фикстуру для тестирования функции get_transaction_amount"""
    return [
        {
            "id": 3967324.0,
            "state": "EXECUTED",
            "date": "2021-05-22T07:46:10Z",
            "amount": 30809.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": nan,
            "to": "Счет 99143269778241825075",
            "description": "Открытие вклада",
        },
        {
            "id": 5515847.0,
            "state": "EXECUTED",
            "date": "2021-08-30T06:11:23Z",
            "amount": 18687.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 3924599516675344",
            "to": "Visa 4023206149439133",
            "description": "Перевод с карты на карту",
        },
    ]

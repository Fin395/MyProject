import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transaction_data() -> list[dict]:
    """Создаем фикстуру для тестирования"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state_correct_filtering(
    sample_transaction_data: list[dict], state: str, expected: list[dict]
) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(sample_transaction_data, state) == expected


def test_filter_by_state_without_status() -> None:
    """Тестирование корректной работы функции, если отсутстыует статус транзакции"""
    assert (
        filter_by_state(
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
        is None
    )


def test_sort_by_date_correct_sorting(sample_transaction_data: list[dict]) -> None:
    """Тестирование корректности сортировки"""
    assert sort_by_date(sample_transaction_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def similar_date_transactions() -> list[dict]:
    """Создаем фикстуру для тестирования по одинаковым датам"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:29.512364"},
    ]


def test_sort_by_date_similar_date(similar_date_transactions: list[dict]) -> None:
    """Тестирование корректности сортировки"""
    assert sort_by_date(similar_date_transactions) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

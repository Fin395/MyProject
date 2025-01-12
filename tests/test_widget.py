import pytest

from src.widget import get_date, mask_account_card


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


@pytest.mark.parametrize(
    "sample_card_and_account_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_correct_mask(sample_card_and_account_data: str, expected: str) -> None:
    """Тестирование корректности маскировки номера карты или счета"""
    assert mask_account_card(sample_card_and_account_data) == expected


def test_mask_account_card_no_data_length() -> None:
    """Тестирование корректной работы функции, если номер карты или счета не введен"""
    assert mask_account_card("") is None


def test_get_date_correct_formatting() -> None:
    """Тестирование корректного преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_no_data() -> None:
    """Тестирование корректности обработки входных строк, когда дата отсутстыует"""
    assert get_date("") is None

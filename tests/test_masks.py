import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_correct_mask() -> None:
    """Тестирование корректности маскировки номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_increased_length() -> None:
    """Тестирование номера карты длиннее положенного"""
    with pytest.raises(ValueError):
        get_mask_card_number("78965412365478977")


def test_get_mask_card_number_reduced_length() -> None:
    """Тестирование номера карты короче положенного"""
    with pytest.raises(ValueError):
        get_mask_card_number("789654123654789")


def test_get_mask_card_number_zero_length() -> None:
    """Тестирование случая, когда номер карты отсутствует"""
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_all_characters_are_digits() -> None:
    """Тестирование номера карты на отсутствие посторонних символов"""
    with pytest.raises(TypeError):
        get_mask_card_number("789654l236547897")


def test_get_mask_account_correct_mask() -> None:
    """Тестирование корректности маскировки номера счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_increased_length() -> None:
    """Тестирование номера счета длиннее положенного"""
    with pytest.raises(ValueError):
        get_mask_account("789654123654789772154")


def test_get_mask_account_reduced_length() -> None:
    """Тестирование номера счета короче положенного"""
    with pytest.raises(ValueError):
        get_mask_account("789654123654789")


def test_get_mask_account_zero_length() -> None:
    """Тестирование случая, когда номер счета отсутствует"""
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_account_all_characters_are_digits() -> None:
    """Тестирование номера счета на отсутствие посторонних символов"""
    with pytest.raises(TypeError):
        get_mask_account("789654l2365478971236")

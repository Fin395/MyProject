from typing import Any
from unittest.mock import patch

import pandas as pd

from src.transactions import get_transactions_from_csv, get_transactions_from_excel


@patch("pandas.read_csv")
def test_get_transactions_from_csv_success(mock_read_csv: Any) -> None:
    """Тестируем корректное считывание данных из csv-файла"""
    mock_data = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0, 593027.0],
            "state": ["EXECUTED", "EXECUTED", "CANCELED"],
            "amount": [16210.0, 29740.0, 30368.0],
        }
    )
    mock_read_csv.return_value = mock_data
    result = get_transactions_from_csv("fake")
    expected = [
        {"id": 650703.0, "state": "EXECUTED", "amount": 16210.0},
        {"id": 3598919.0, "state": "EXECUTED", "amount": 29740.0},
        {"id": 593027.0, "state": "CANCELED", "amount": 30368.0},
    ]
    assert result == expected


def test_get_transactions_from_csv() -> None:
    """Тестирование работы функции при ошибочно указанном пути к файлу"""
    assert get_transactions_from_csv("C:/Users/Sergei/PycharmProjects/MyProject/operations.json") == []


@patch("pandas.read_excel")
def test_get_transactions_from_excel_success(mock_read_excel: Any) -> None:
    """Тестируем корректное считывание данных из csv-файла"""
    mock_data = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0, 593027.0],
            "state": ["EXECUTED", "EXECUTED", "CANCELED"],
            "amount": [16210.0, 29740.0, 30368.0],
        }
    )
    mock_read_excel.return_value = mock_data
    result = get_transactions_from_excel("fake")
    expected = [
        {"id": 650703.0, "state": "EXECUTED", "amount": 16210.0},
        {"id": 3598919.0, "state": "EXECUTED", "amount": 29740.0},
        {"id": 593027.0, "state": "CANCELED", "amount": 30368.0},
    ]
    assert result == expected


def test_get_transactions_from_excel() -> None:
    """Тестирование работы функции при ошибочно указанном пути к файлу"""
    assert get_transactions_from_excel("C:/Users/Sergei/PycharmProjects/MyProject/operations.json") == []

from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount_if_rub(sample_transaction_in_rub: dict) -> None:
    """Тестирование функции, если валюта в рублях"""
    assert get_transaction_amount(sample_transaction_in_rub) == "31957.58"


def test_get_transaction_amount_if_usd(sample_transaction_in_usd: dict) -> None:
    """Тестирование функции, если валюта в долларах"""

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 122718.492, "success": True}
    with patch("requests.get", return_value=mock_response):
        result = get_transaction_amount(sample_transaction_in_usd)
        assert result == 122718.492


def test_get_transaction_amount_if_failed(sample_transaction_in_usd: dict) -> None:
    """Тестирование функции в случае возникновения ошибки"""
    mock_response = Mock()
    mock_response.status_code = 500
    with patch("requests.get", return_value=mock_response):
        assert get_transaction_amount(sample_transaction_in_usd) is None

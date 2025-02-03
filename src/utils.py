import json
from typing import Any


def get_transactions(path_to_file: str) -> Any:
    """Функция возвращает из файла список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to_file, encoding="utf-8") as operations_data:
            transactions_data = json.load(operations_data)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    else:
        return transactions_data

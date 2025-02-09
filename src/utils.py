import json
import logging
from typing import Any
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, '..', 'logs', 'utils.log')

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(logs_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(path_to_file: str) -> Any:
    """Функция возвращает из файла список словарей с данными о финансовых транзакциях"""
    try:
        logger.info(f"Получаем данные о финансовых транзакциях из файла {path_to_file}")
        with open(path_to_file, encoding="utf-8") as operations_data:
            transactions_data = json.load(operations_data)
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except json.decoder.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    else:
        return transactions_data

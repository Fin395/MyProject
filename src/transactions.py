from typing import Any

import pandas as pd


def get_transactions_from_csv(path_to_csv_file: str) -> list[Any]:
    """Получаем список транзакций из csv-файла"""
    try:
        transactions_reader = pd.read_csv(path_to_csv_file, delimiter=";")
        transactions_reader_as_dict = transactions_reader.to_dict(orient="records")
        return transactions_reader_as_dict
    except Exception:
        print("Ошибка, не удалось получить данные")
        return []


def get_transactions_from_excel(path_to_excel_file: str) -> list[Any]:
    """Получаем список транзакций из excel-файла"""
    try:
        transactions_reader = pd.read_excel(path_to_excel_file)
        transactions_reader_as_dict = transactions_reader.to_dict(orient="records")
        return transactions_reader_as_dict
    except Exception:
        print("Ошибка, не удалось получить данные")
        return []

#result= get_transactions_from_csv(r"C:\Users\Sergei\OneDrive\Рабочий стол\УЧЕБА\transactions.csv")
#print(result)
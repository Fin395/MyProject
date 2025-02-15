from src.generators import filter_by_currency_csv_or_excel, filter_by_currency_json
from src.processing import filter_by_state, sort_by_date
from src.search_for_transaction import search_for_transcations_by_string
from src.transactions import get_transactions_from_csv, get_transactions_from_excel
from src.utils import get_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция, которая соединяет логику и взаимодействует с пользователем"""
    transactions_data = []
    user_input = int(
        input(
            """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    )
    if user_input == 1:
        print("Для обработки выбран JSON-файл.")
        transactions_data = get_transactions(r"C:\Users\Sergei\PycharmProjects\MyProject\src\..\data\operations.json")
    elif user_input == 2:
        print("Для обработки выбран CSV-файл.")
        transactions_data = get_transactions_from_csv(r"C:\Users\Sergei\OneDrive\Рабочий стол\УЧЕБА\transactions.csv")
    elif user_input == 3:
        print("Для обработки выбран XLSX-файл.")
        transactions_data = get_transactions_from_excel(
            r"C:\Users\Sergei\OneDrive\Рабочий стол\УЧЕБА\transactions_excel.xlsx"
        )

    status_selected = input(
        """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )

    while status_selected.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status_selected} недоступен")
        status_selected = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
    if status_selected.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Операции отфильтрованы по статусу {status_selected.upper()}.")
        filtered_transactions = filter_by_state(transactions_data, status_selected.upper())

    user_sorting = input("Отсортировать операции по дате? Да/Нет\n")
    if user_sorting.lower() == "нет":
        filtered_transactions = filtered_transactions
    elif user_sorting.lower() == "да":
        kind_of_sorting = input("Отсортировать по возрастанию или по убыванию?\n")
        if kind_of_sorting.lower() == "по возрастанию":
            sorted_transactions = sort_by_date(filtered_transactions, reverse=False)
            filtered_transactions = sorted_transactions
        else:
            sorted_transactions = sort_by_date(filtered_transactions)
            filtered_transactions = sorted_transactions

    select_rub = input("Выводить только рублевые транзакции? Да/Нет\n")
    if select_rub.lower() == "нет":
        filtered_transactions = filtered_transactions
    else:
        if user_input == 1:
            filtered_transactions = list(filter_by_currency_json(filtered_transactions, "RUB"))
        else:
            filtered_transactions = list(filter_by_currency_csv_or_excel(filtered_transactions, "RUB"))

    select_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if select_filter.lower() == "нет":
        filtered_transactions = list(filtered_transactions)
        print(filtered_transactions)

    else:
        user_search_string = input("Введите слово для поиска:\n")
        filtered_transactions_by_string = search_for_transcations_by_string(filtered_transactions, user_search_string)
        filtered_transactions = filtered_transactions_by_string
        print(filtered_transactions)

    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...\n")
        length_of_filtered_transactions = len(filtered_transactions)
        print(f"Всего банковских операций в выборке: {length_of_filtered_transactions}\n")

        for trans in filtered_transactions:
            date_of_trans = get_date(trans["date"])
            kind_of_trans = trans["description"]
            for key in trans.keys():
                if key == "operationAmount":
                    total_amount = trans["operationAmount"]["amount"]
                    currency_name = trans["operationAmount"]["currency"]["name"]
                elif key == "amount":
                    total_amount = trans["amount"]
                    currency_name = trans["currency_name"]
                else:
                    continue
                print(f"{date_of_trans} {kind_of_trans}")
                if trans["description"] == "Открытие вклада":
                    masked_account = mask_account_card(trans["to"])
                    print(masked_account)
                else:
                    masked_number_from = mask_account_card(trans["from"])
                    masked_number_to = mask_account_card(trans["to"])
                    print(f"{masked_number_from} -> {masked_number_to}")
                print(f"Сумма: {total_amount} {currency_name}\n")


if __name__ == "__main__":
    main()

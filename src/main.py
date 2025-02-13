from src.utils import get_transactions
from src.transactions import get_transactions_from_csv, get_transactions_from_excel
from src.processing import filter_by_state, sort_by_date

def main():
    transactions_data = []
    user_input = int(input("""Привет! 
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
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
        transactions_data = get_transactions_from_excel(r"C:\Users\Sergei\OneDrive\Рабочий стол\УЧЕБА\transactions_excel.xlsx")
    else:
        print("Ошибка. Нет такого пункта")

    status_selected = input("""
#Введите статус, по которому необходимо выполнить фильтрацию.
#Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
                            ).upper()
    while status_selected not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status_selected} недоступен")
        status_selected = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
                    ).upper()
    if status_selected in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"""Операции отфильтрованы по статусу {status_selected}.""")

    filtered_transactions = filter_by_state(transactions_data, status_selected )

    user_sorting = input("Отсортировать операции по дате? Да/Нет\n")
    if user_sorting == "Нет":
        print(filtered_transactions)
    if user_sorting == "Да":
        kind_of_sorting = input("Отсортировать по возрастанию или по убыванию?\n")
        if kind_of_sorting == "по возрастанию":
            sorting_transactions = sort_by_date(filtered_transactions, reverse=False)
            print(sorting_transactions)

if __name__ == "__main__":
    main()
#    print(widget.mask_account_card(input("Введите номер карты или счета: ")))
#    print(widget.get_date(input("Введите дату: ")))

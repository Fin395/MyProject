def filter_by_state(list_of_transactions: list, state: str = "EXECUTED") -> list:
    """Отбирает те транзакции, которые были исполнены"""
    filtered_transactions = []

    for transaction in list_of_transactions:
        if state in transaction.values():
            filtered_transactions.append(transaction)
    return filtered_transactions


# пример входных данных и работы функции
# result = filter_by_state(
#    [
#        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#    ]
# )
# print(result)


def sort_by_date(list_of_transactions: list, reverse: bool = True) -> list:
    """Сортирует транзакции в порядке убывания по дате их осуществления"""
    return sorted(list_of_transactions, key=lambda x: x["date"], reverse=reverse)


# пример входных данных и работы функции
# result = sort_by_date(
#    [
#        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#    ]
# )
# print(result)

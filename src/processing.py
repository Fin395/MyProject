def filter_by_state(list_of_transactions: list[dict], state: str = "EXECUTED") -> list:
    """Отбирает те транзакции, которые были исполнены"""
    filtered_transactions = []
    try:
        for transaction in list_of_transactions:
            if len(transaction) !=0:
                if transaction["state"] == state:
                    filtered_transactions.append(transaction)
            else:
                continue
    except KeyError:
        print("Отсутствуют сведения о статусе транзакции")
    finally:
        return filtered_transactions


def sort_by_date(list_of_transactions: list, reverse: bool = True) -> list:
    """Сортирует транзакции в порядке убывания по дате их осуществления"""
    return sorted(list_of_transactions, key=lambda x: x["date"], reverse=reverse)

from src.search_for_transaction import count_transactions_category, search_for_transcations_by_string


def test_search_for_transcations_by_string(sample_transactions_json: list[dict]) -> None:
    """Проверяем корректность выборки по слову "счет" """
    result = search_for_transcations_by_string(sample_transactions_json, "счет")
    assert result == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_search_for_transcations_by_string_no_match(sample_transactions_json: list[dict]) -> None:
    """Проверяем, что функция возвращает пустой список, если шаблон не найден"""
    result = search_for_transcations_by_string(sample_transactions_json, "вклад")
    assert result == []


def test_search_for_transcations_by_string_if_nan(sample_transaction_with_nan: list[dict]) -> None:
    """Проверяем корректность выборки, если значение указано как "nan" """
    result = search_for_transcations_by_string(sample_transaction_with_nan, "вклад")
    assert result == [
        {
            "id": 3967324.0,
            "state": "EXECUTED",
            "date": "2021-05-22T07:46:10Z",
            "amount": 30809.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": None,
            "to": "Счет 99143269778241825075",
            "description": "Открытие вклада",
        }
    ]


def test_search_for_transcations_by_string_if_upper_case(sample_transaction_with_nan: list[dict]) -> None:
    """Проверяем корректность выборки независимо от регистра слова поиска"""
    result = search_for_transcations_by_string(sample_transaction_with_nan, "перевод")
    assert result == [
        {
            "id": 5515847.0,
            "state": "EXECUTED",
            "date": "2021-08-30T06:11:23Z",
            "amount": 18687.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 3924599516675344",
            "to": "Visa 4023206149439133",
            "description": "Перевод с карты на карту",
        }
    ]


def test_count_transactions_category(sample_transactions_json: list[dict]) -> None:
    """Проверяем корректность подсчета операций по заданным категориям"""
    categories = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    result = count_transactions_category(sample_transactions_json, categories)
    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}


def test_count_transactions_category_lack_of_category(sample_transactions_json: list[dict]) -> None:
    """Проверяем корректность подсчета операций, если заданной категории нет в списке операций"""
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_transactions_category(sample_transactions_json, categories)
    assert result == {"Перевод организации": 2, "Открытие вклада": 0}

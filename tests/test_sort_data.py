import pytest

@pytest.fixture()
def some_data():
    return [
    {'id': 3330422.0, 'state': 'EXECUTED', 'date': '2023-08-05T07:11:26Z', 'amount': 30065.0, 'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 9458117363112215', 'to': 'Visa 6335859532296628', 'description': 'Перевод с карты на карту'},
    {'id': 3794942.0, 'state': 'EXECUTED', 'date': '2021-05-24T02:37:49Z', 'amount': 14174.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Mastercard 8628645140673956', 'to': 'Счет 36990402090010935845', 'description': 'Перевод организации'},
    {'id': 3967324.0, 'state': 'EXECUTED', 'date': '2021-05-22T07:46:10Z', 'amount': 30809.0, 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'nan', 'to': 'Счет 99143269778241825075', 'description': 'Открытие вклада'},
    {'id': 5515847.0, 'state': 'EXECUTED', 'date': '2021-08-30T06:11:23Z', 'amount': 18687.0, 'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 3924599516675344', 'to': 'Visa 4023206149439133', 'description': 'Перевод с карты на карту'},
    {'id': 308178.0, 'state': 'EXECUTED', 'date': '2020-09-07T17:16:11Z', 'amount': 17368.0, 'currency_name': 'Zloty', 'currency_code': 'PLN', 'from': 'Discover 2547099241263746', 'to': 'Discover 1506530746937020', 'description': 'Перевод с карты на карту'},
    {'id': 4808031.0, 'state': 'EXECUTED', 'date': '2022-08-13T09:20:42Z', 'amount': 14650.0, 'currency_name': 'Dinar', 'currency_code': 'TND', 'from': 'Visa 2860183248053465', 'to': 'Discover 4880897470446329', 'description': 'Перевод с карты на карту'},
    ]


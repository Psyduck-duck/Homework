# Homework
## Описание:

Виджет банковских операций клиета

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Psyduck-duck/Homework.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

Функция `get_mask_card_number` принимает на обработку число формата int длинной 16 знаков.

Функция `get_mask_account` принимает на обработку число формата int длинной 20 знаков.

Функция `mask_account_card` принимает на обработку строку из названия карты или счета 
и число из 16 или 20 знаков соответсвенно.

Функция `get_data` принимает на обработку стркоу начинающуюся с формата `yyyy-mm-dd`.

Функция `sort_by_date` принимает на обработку словари с форматом `date` начинающуюся c `yyyy-mm-dd`.

Функция `filter_by_currency` принимает список словарей и возвращает генератор, 
возвращающий только словари с нужной валютой.

Функция `transaction_descriptions` принимает список словарей и возвращает генератор, возвращающий инйормацию
об операции с каждого словаря.

Функция `card_number_generator` генерирует номера карт формата ХХХХ ХХХХ ХХХХ ХХХх в заданном диапозоне.

## Тесты

По всем написанным функциям прописанны тесты на основные возможные сценарии, отработаны исключения при
некорректном вводе информации, площадь покрытия кода 98%.

## Документация:

## Лицензия:
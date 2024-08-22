import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "card_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_data, expected):
    assert mask_account_card(card_data) == expected


def test_mask_account_card_invalid_input():
    with pytest.raises(ValueError):
        mask_account_card("счет 123456789012345678901326464984311465431618")
        mask_account_card("Visa 1234")


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1956-12-12T12:12:12.671512", "12.12.1956"),
        ("2021-07-28T00:00:00.123456", "28.07.2021"),
        ("2014-02-21T02:26:18.671407", "21.02.2014"),
    ],
)
def test_get_data(date, expected):
    get_data(date) == expected


def test_get_data_invalid_date():
    with pytest.raises(ValueError):
        get_data("2024-13-11T02:26:18.671407")
        get_data("2024-10-32T02:26:18.671407")


def test_get_data_short_date():
    assert get_data("2024-12-12") == "12.12.2024"

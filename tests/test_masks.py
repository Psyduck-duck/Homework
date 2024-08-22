import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(1234567890123456) == '1234 56** **** 3456'


@pytest.mark.parametrize('number', [(1234), (123456780321565465432165), (-1)])
def test_get_mask_card_number_invalid_number(number):
    with pytest.raises(ValueError):
        get_mask_card_number(number)


def test_get_mask_card_number_invalid_type():
    with pytest.raises(TypeError):
        get_mask_card_number('номер карты')


def test_get_mask_account():
    assert get_mask_account(12345678901234567890) == '**7890'


def test_get_mask_invalid_type_account():
    with pytest.raises(TypeError):
        get_mask_account('Hello')


def test_get_mask_account_invalid_len():
    with pytest.raises(ValueError):
        get_mask_account(123456789)
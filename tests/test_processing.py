import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def some_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(some_data):
    assert filter_by_state(some_data, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_witout_state():
    assert (
        filter_by_state(
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
        == []
    )


def test_sort_by_date(some_data):
    assert sort_by_date(some_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_invalid_date():
    with pytest.raises(ValueError):
        sort_by_date(
            [
                {"id": 41428829, "date": "2019-14-03T18:35:29.512364"},
                {"id": 939719570, "date": "2018-06-32T02:08:58.425572"},
            ]
        )


def test_sort_by_date_invalid_type():
    with pytest.raises(ValueError):
        sort_by_date([{"id": 41428829, "date": "15"}, {"id": 939719570, "date": "2018-06-32T02:08:58.425572"}])


def test_sort_by_date_equal_date():
    assert sort_by_date(
        [
            {"id": 41428829, "date": "2019-10-03T18:35:29.512364"},
            {"id": 939719570, "date": "2019-10-03T18:35:29.512364"},
        ]
    ) == [
        {"id": 41428829, "date": "2019-10-03T18:35:29.512364"},
        {"id": 939719570, "date": "2019-10-03T18:35:29.512364"},
    ]

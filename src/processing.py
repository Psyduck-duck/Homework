from widget import get_data


def filter_by_state(operation_list: list, state: str = "EXECUTED") -> list:
    new_list = []
    for dict in operation_list:
        if dict["state"] == state:
            new_list.append(dict)
    return new_list


def sort_by_date(operation_list: list, reverse_: bool = True) -> list:
    sorted_list = sorted(
        operation_list, key=lambda x: ".".join(reversed((get_data(x["date"]).split(".")))), reverse=reverse_
    )
    return sorted_list


if __name__ == "__main__":
    data_for_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    data_for_test_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    #print(filter_by_state(data_for_test, 'CANCELED'))
    #print(sort_by_date(data_for_test_1))

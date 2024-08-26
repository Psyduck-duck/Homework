


def filter_by_currency(operation_list: list, currency: str):
    return (x for x in operation_list if x['operationAmount']['currency']['code'] == currency)


def transaction_descriptions(operation_list):
    return (x['description'] for x in operation_list)
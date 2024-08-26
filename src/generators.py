


def filter_by_currency(operation_list: list, currency: str):
    return (x for x in operation_list if x['operationAmount']['currency']['name'] == currency)

#usd_trans = filter_by_currency(operation_list, 'USD')

#for i in range(3):
    print(next(usd_trans))
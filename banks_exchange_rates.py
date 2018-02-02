from banks import belinvest, tinkoff


def fetch_currencies(currencies, banks):
    if isinstance(currencies, str):
        currencies = currencies.split(',')
    if isinstance(banks, str):
        banks = banks.split(',')

    banks_rates = {
        'tinkoff': tinkoff.fetch_rates,
        'belinvest': belinvest.fetch_rates,
    }

    rates = {
        bank: banks_rates[bank]() for bank in banks
    }

    result = {}
    for currency in currencies:
        result[currency] = {}
        for bank, data in rates.items():
            result[currency][bank] = list(filter(lambda rate: rate['from'] == currency, data))

    return result

if __name__ == '__main__':
    import sys
    import json
    try:
        currencies = sys.argv[1]
        banks = sys.argv[2]
    except IndexError:
        sys.exit('Currencies and banks args are required')
    result = fetch_currencies(currencies, banks)
    print(json.dumps(result, indent=4))

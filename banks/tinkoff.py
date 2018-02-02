import requests


TINKOFF_ENDPOINT = 'https://api05.tinkoff.ru/v1/grouped_requests?origin=web'


def fetch_rates():
    response = requests.post(TINKOFF_ENDPOINT, data={'requestsData': '[{"key":0,"operation":"currency_rates"}]'})
    content = response.json()

    if not content.get('resultCode') == 'OK':
        return []

    rates = filter(
        lambda rate: rate['category'] == 'C2CTransfers', 
        content['payload']['0']['payload']['rates'],
    )

    return [{
        'from': rate['fromCurrency']['name'],
        'to': rate['toCurrency']['name'],
        'buy': f'{rate["buy"]:.2f}',
        'sell': f'{rate["sell"]:.2f}',
    } for rate in rates]
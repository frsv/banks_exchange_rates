import requests
from urllib.parse import urlencode


CURRENCY_CODES_MAPPING = {
    'EUR': '978',
    'USD': '840',
    'JPY': '392',
    'CHF': '756',
    'GBP': '826',
}
SBERBANK_PARAMS = {
    'regionId': 77,
    'currencyCode': CURRENCY_CODES_MAPPING.values(),
    'rateCategory': ['cards'],  # ['base', 'beznal', 'cards']
}
SBERBANK_URL = 'http://localhost/rates-web/rateService/rate/current'
SBERBANK_PROXY_URL = 'https://www.sberbank.ru/portalserver/proxy/'
SBERBANK_PROXY_PARAMS = {
    'pipe': 'shortCachePipe',
    'url': f'{SBERBANK_URL}?{urlencode(SBERBANK_PARAMS, True)}',
}


def fetch_rates():
    response = requests.get(SBERBANK_PROXY_URL, params=SBERBANK_PROXY_PARAMS)
    content = response.json()
    return [{
        'from': rate['0']['isoCur'],
        'to': 'RUB',
        'buy': rate['0']['buyValue'],
        'sell': rate['0']['sellValue'],
    } for currency_code, rate in content['cards'].items()]

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode


TINKOFF_ENDPOINT = 'https://api05.tinkoff.ru/v1/grouped_requests?origin=web'
BELINVEST_ENDPOINT = 'https://ibank.belinvestbank.by/api/cardsCourses.php'



def fetch_tinkoff_currencies():
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


def fetch_belinvest_currencies():
    response = requests.get(BELINVEST_ENDPOINT)
    content = BeautifulSoup(response.text, 'html.parser')
    rates = content.find_all('forexrateinqrs')

    return [{
        'from': rate.curcode.string,
        'to': rate.basecurcode.string,
        'operation': rate.forexratedealtype.string.lower(),
        'amount': rate.curamnt.string,
        'value': rate.currate.string,
    } for rate in rates]


def fetch_currencies(currencies, banks):
    pass

# rates = fetch_tinkoff_currencies()
# print('Tinkoff')
# for rate in rates:
#     print(f'\n{rate["from"]} -> {rate["to"]}')
#     print(f'\tbuy: {rate["buy"]}')
#     print(f'\tsell: {rate["sell"]}')

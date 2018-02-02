import requests
from bs4 import BeautifulSoup


BELINVEST_ENDPOINT = 'https://ibank.belinvestbank.by/api/cardsCourses.php'


def _combine_buy_sell_rates(rates):
    combined = {}
    for rate in rates:
        key = f'{rate.curcode.string}-{rate.basecurcode.string}'
        combined_rate = combined.setdefault(key, {
            'from': rate.curcode.string,
            'to': rate.basecurcode.string,
        })
        combined_rate[rate.forexratedealtype.string.lower()] = f'{float(rate.currate.string):.2f}'
    return list(combined.values())


def fetch_rates():
    response = requests.get(BELINVEST_ENDPOINT)
    content = BeautifulSoup(response.text, 'html.parser')
    rates = content.find_all('forexrateinqrs')
    rates = _combine_buy_sell_rates(rates)
    return rates

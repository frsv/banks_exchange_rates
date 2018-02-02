import json
from os.path import join, dirname
from unittest import TestCase
from unittest.mock import patch, Mock

from ..tinkoff import fetch_rates


class MockedResponse:
    @staticmethod
    def json():
        with open(join(dirname(__file__), 'tinkoff.json')) as data_file:
            return json.load(data_file)


@patch('requests.post', Mock(return_value=MockedResponse))
class TestBelinvest(TestCase):
    def test_ok(self):
        result = sorted(fetch_rates(), key=lambda rate: rate['from'])

        self.assertEqual(result, [
            {
                'from': 'EUR',
                'to': 'RUB',
                'buy': '68.90',
                'sell': '71.70',
            },
            {
                'from': 'EUR',
                'to': 'USD',
                'buy': '1.22',
                'sell': '1.27',
            },
            {
                'from': 'GBP',
                'to': 'RUB',
                'buy': '78.40',
                'sell': '81.70',
            },
            {
                'from': 'GBP',
                'to': 'USD',
                'buy': '1.39',
                'sell': '1.45',
            },
            {
                'from': 'GBP',
                'to': 'EUR',
                'buy': '1.11',
                'sell': '1.16',
            },
            {
                'from': 'USD',
                'to': 'RUB',
                'buy': '55.15',
                'sell': '57.40',
            },
        ])

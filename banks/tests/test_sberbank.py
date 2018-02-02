import json
from os.path import join, dirname
from unittest import TestCase
from unittest.mock import patch, Mock

from ..sberbank import fetch_rates


class MockedResponse:
    @staticmethod
    def json():
        with open(join(dirname(__file__), 'sberbank.json')) as data_file:
            return json.load(data_file)


@patch('requests.post', Mock(return_value=MockedResponse))
class TestBelinvest(TestCase):
    def test_ok(self):
        result = sorted(fetch_rates(), key=lambda rate: rate['from'])

        self.assertEqual(result, [
            {
                'from': 'EUR',
                'to': 'RUB',
                'buy': 68.46,
                'sell': 71.96,
            },
            {
                'from': 'USD',
                'to': 'RUB',
                'buy': 54.84,
                'sell': 57.96,
            },
        ])

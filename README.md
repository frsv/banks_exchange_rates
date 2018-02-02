Banks exchange rates
====================

[![Build Status](https://travis-ci.org/frsv/banks_exchange_rates.svg?branch=master)](https://travis-ci.org/frsv/banks_exchange_rates)

Banks exchange rates for some banks in Belarus and Russia

Installation
------------

Clone this repo

Usage
-----

As module:

```python
from banks_exchange_rates import fetch_currency

fetch_currency(['USD', 'EUR'], ['tinkoff', 'sberbank', 'belinvest'])
```

As python script:

```bash
python banks_exchange_rates.py USD,EUR tinkoff,sberbank

{
    "USD": {
        "sberbank": [
            {
                "from": "USD",
                "to": "RUB",
                "buy": 54.84,
                "sell": 57.96
            }
        ],
        "tinkoff": [
            {
                "from": "USD",
                "to": "RUB",
                "buy": "55.25",
                "sell": "57.50"
            }
        ]
    },
    "EUR": {
        "sberbank": [
            {
                "from": "EUR",
                "to": "RUB",
                "buy": 68.46,
                "sell": 71.96
            }
        ],
        "tinkoff": [
            {
                "from": "EUR",
                "to": "RUB",
                "buy": "68.75",
                "sell": "71.60"
            },
            {
                "from": "EUR",
                "to": "USD",
                "buy": "1.22",
                "sell": "1.27"
            }
        ]
    }
}
```


Tests running
-------------

Just run
```bash
python -m unittest
```

License
-------
[MIT](LICENSE.md)

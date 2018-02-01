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

# fetch_currency(currency, banks)
fetch_currency(['usd', 'euro'], ['tinkoff', 'sberbank', 'belinvest'])
```

As python script:

```bash
python banks_exchange_rates.py usd tinkoff,sberbank,belinvest

USD buy:
    60,00 tinkoff
    61,00 sberbank
    2,01 belinvest
USD sell:
    65,00 tinkoff
    66,00 sberbank
    2,2 belinvest
```


Tests running
-------------

Just run
```bash
pytest
```

License
-------
[MIT](LICENSE.md)

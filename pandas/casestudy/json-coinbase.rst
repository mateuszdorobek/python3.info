JSON Coinbase
=============

>>> import requests
>>>
>>>
>>> DATA = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
>>>
>>> resp = requests.get(DATA)
>>> data = resp.json()['data']
>>>
>>> data  # doctest: +SKIP
{'base': 'BTC', 'currency': 'USD', 'amount': '36520.77'}

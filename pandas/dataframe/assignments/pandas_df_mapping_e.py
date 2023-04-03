"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Use `requests` library
    3. Transpose data
    4. If cell is a `dict`, then extract value for `summary`
    5. If cell is empty, leave `pd.NA`
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Użyj biblioteki `requests`
    3. Transponuj dane
    4. Jeżeli komórka jest `dict`, to wyciągnij wartość dla `summary`
    5. Jeżeli komórka jest pusta, pozostaw `pd.NA`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> list(result.columns)
    ['put', 'post', 'get', 'delete']

    >>> list(result.index)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""

import pandas as pd
import requests


DATA = 'https://python3.info/_static/openapi.json'

# type: pd.DataFrame
result = ...


# Solution
df = requests.get(DATA).json()
result = (pd.DataFrame(df['paths'])
            .transpose()
            .applymap(lambda x: x['summary'] if type(x) == dict else pd.NA))

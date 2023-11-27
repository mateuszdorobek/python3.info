"""
* Assignment: Loop Dict Reverse
* Type: homework
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use iteration to reverse dict:
       that is: change keys for values and values for keys
    2. Run doctests - all must succeed

Polish:
    1. Użyj iterowania do odwócenia dicta:
       to jest: zamień klucze z wartościami i wartości z kluczami
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict.items()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())
    >>> assert len(result.keys()) == 3

    >>> assert 'virginica' in result.keys()
    >>> assert 'setosa' in result.keys()
    >>> assert 'versicolor' in result.keys()

    >>> assert 0 in result.values()
    >>> assert 1 in result.values()
    >>> assert 2 in result.values()

    >>> result
    {'virginica': 0, 'setosa': 1, 'versicolor': 2}
"""

DATA = {
    0: 'virginica',
    1: 'setosa',
    2: 'versicolor'}

# dict[str,int]:
result = ...

# Solution
result = {}

for key, value in DATA.items():
    result[value] = key

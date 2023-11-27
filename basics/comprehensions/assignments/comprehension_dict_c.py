"""
* Assignment: Comprehension Dict Reverse
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use dict comprehension to reverse dict:
       that is: change keys for values and values for keys
    2. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia słownikowego do odwócenia słownika:
       to jest: zamień klucze z wartościami i wartości z kluczami
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict.items()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict
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

# type: dict[str,int]
result = ...

# Solution
result = {v:k for k,v in DATA.items()}

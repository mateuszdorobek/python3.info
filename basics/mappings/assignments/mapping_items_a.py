"""
* Assignment: Mapping Items List
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    3. Define `result: list[tuple]` with list of `DATA` key-value pairs
    4. Run doctests - all must succeed

Polish:
    3. Zdefiniuj `result: list[tuple]` z listą par klucz-wartość z `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list()`
    * `dict.items()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuples'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('sepal_length', 5.8),
     ('sepal_width', 2.7),
     ('petal_length', 5.1),
     ('petal_width', 1.9)]
"""

DATA = {
    'sepal_length': 5.8,
    'sepal_width': 2.7,
    'petal_length': 5.1,
    'petal_width': 1.9,
}

# List with key-value pairs from DATA
# type: list[tuple]
result = ...

# Solution
result = list(DATA.items())

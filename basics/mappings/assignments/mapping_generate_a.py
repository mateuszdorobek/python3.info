"""
* Assignment: Mapping Generate Pairs
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: dict`
    2. Convert `DATA` to `dict` and assign to `result`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict`
    2. Przekonwertuj `DATA` do `dict` i przypisz do `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys()), \
    'All dict keys should be str'

    >>> assert 'sepal_length' in result.keys()
    >>> assert 'sepal_width' in result.keys()
    >>> assert 'petal_length' in result.keys()
    >>> assert 'petal_width' in result.keys()
    >>> assert 'species' in result.keys()

    >>> assert 5.8 in result.values()
    >>> assert 2.7 in result.values()
    >>> assert 5.1 in result.values()
    >>> assert 1.9 in result.values()
    >>> assert 'virginica' in result.values()

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': 5.8,
     'sepal_width': 2.7,
     'petal_length': 5.1,
     'petal_width': 1.9,
     'species': 'virginica'}
"""

DATA = [
    ('sepal_length', 5.8),
    ('sepal_width', 2.7),
    ('petal_length', 5.1),
    ('petal_width', 1.9),
    ('species', 'virginica'),
]

# Dict with converted DATA
# type: dict[str,float|str]
result = ...

# Solution
result = dict(DATA)

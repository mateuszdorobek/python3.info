"""
* Assignment: Idiom Zip Dict
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: dict`
    2. Assign to `result` zipped `KEYS` and `VALUES` to `dict`
    3. Use `zip()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict`
    2. Przypisz do `result` zzipowane `KEYS` i `VALUES` do `dict`
    3. Użyj `zip()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`
    * `zip()`

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

KEYS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

# Dict with Zipped KEYS and VALUES
# type: dict[str,float|str]
result = ...

# Solution
result = dict(zip(KEYS, VALUES))

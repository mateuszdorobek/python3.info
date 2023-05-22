"""
* Assignment: Star Assignment Loop
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Iterate over data splitting `values` from `species`
    2. Define `result: list[str]` with
       species names ending with "ca" or "osa"
    3. Use star expression
    4. Run doctests - all must succeed

Polish:
    1. Iteruj po danych rozdzielając `values` od `species`
    2. Zdefiniuj `result: list[str]` z
       nazwami gatunków kończącymi się na "ca" lub "osa"
    3. Użyj wyrażenia z gwiazdką
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.endswith()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert len(result) > 0, \
    'Variable `result` cannot be empty'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['virginica', 'setosa', 'virginica', 'setosa']
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

SUFFIXES = ('ca', 'osa')

# species names ending with "ca" or "osa"
# type: list[str]
result = ...

# Solution
result = [species
          for *values, species in DATA[1:]
          if species.endswith(SUFFIXES)]

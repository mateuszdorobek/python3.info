"""
* Assignment: Iterable Slice Header/Rows
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Separate header (first line) from rows:
       a. Define `header: tuple[str]` with header
       b. Define `rows: list[tuple]` with other rows
    2. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek (pierwsza linia) od danych:
       a. Zdefiniuj `header: tuple[str]` z nagłówkiem
       b. Zdefiniuj `rows: list[tuple]` z pozostałymi wierszami
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, \
    'Assign your result to variable `header`'
    >>> assert rows is not Ellipsis, \
    'Assign your result to variable `rows`'
    >>> assert type(header) is tuple, \
    'Variable `header` has invalid type, should be tuple'
    >>> assert all(type(x) is tuple for x in rows), \
    'All elements in `rows` should be tuple'
    >>> assert header not in rows, \
    'Header should not be in `rows`'

    >>> header
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> rows  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa'),
     (4.9, 2.5, 4.5, 1.7, 'virginica')]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]


# Tuple with row at index 0 from DATA
# type: tuple[str]
header = ...

# List with rows at all the other indexes from DATA
# type: list[tuple]
rows = ...

# Solution
header = DATA[0]
rows = DATA[1:]

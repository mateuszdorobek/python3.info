"""
* Assignment: Star Assignment Nested
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate header and rows
    2. Use star expression
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od wierszy danych
    2. Użyj wyrażenia z gwiazdką
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, \
    'Assign result to variable: `header`'
    >>> assert rows is not Ellipsis, \
    'Assign result to variable: `rows`'
    >>> assert len(header) > 0, \
    'Variable `header` cannot be empty'
    >>> assert len(rows) > 0, \
    'Variable `rows` cannot be empty'
    >>> assert type(header) is tuple, \
    'Variable `header` has invalid type, should be tuple'
    >>> assert type(rows) is list, \
    'Variable `hosts` has invalid type, should be list'
    >>> assert all(type(x) is str for x in header), \
    'All rows in `header` should be str'
    >>> assert all(type(x) is tuple for x in rows), \
    'All rows in `rows` should be tuple'

    >>> header
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> rows  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
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

# first line from DATA
# example: ('sepal_length', 'sepal_width', ...)
# type: tuple[str]
header = ...

# all the other lines from DATA, beside first line
# example: [(5.8, 2.7, 5.1, 1.9, 'virginica'),  ...]
# type: list[tuple]
rows = ...

# Solution
header, *rows = DATA

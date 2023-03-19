"""
* Assignment: Sequence UnpackStar Nested
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate header from records
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od danych
    2. Skorzystaj z notacji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, \
    'Assign your result to variable `header`'
    >>> assert rows is not Ellipsis, \
    'Assign your result to variable `data`'

    >>> assert len(header) > 0, \
    'Variable `header` cannot be empty'
    >>> assert len(rows) > 0, \
    'Variable `data` cannot be empty'

    >>> assert type(header) is tuple, \
    'Variable header must be a tuple'
    >>> assert type(rows) is list, \
    'Variable data must be a list'
    >>> assert all(type(x) is str for x in header), \
    'All header elements must be a str'
    >>> assert all(type(row) is tuple for row in rows), \
    'All rows in data must be tuples'

    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

    >>> rows  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa')]

# Tuple with row with index 0: ('Sepal length', 'Sepal width', ...)
# type: tuple[str]
header = ...

# List with all other rows: (5.8, 2.7, 5.1, 1.9, 'virginica'),  ...
# type: list[tuple]
rows = ...

# Solution
header, *rows = DATA

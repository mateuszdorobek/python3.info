"""
* Assignment: Iterable GetItem Header/Data
* Type: class assignment
* Complexity: easy
* Lines of code: 11 lines
* Time: 5 min

English:
    1. Separate header (first line) from data:
       a. Define `header: tuple[str]` with header
       b. Define `data: list[tuple]` with other data without header
    2. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
       c. You can use copy and paste and/or vertical select `alt`
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek (pierwsza linia) od danych:
       a. Zdefiniuj `header: tuple[str]` z nagłówkiem
       b. Zdefiniuj `data: list[tuple]` z danymi bez nagłówka
    2. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
       c. Możesz użyć kopiowania i wklejania lub/i zaznaczania pioniwego `alt`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, \
    'Assign your result to variable `header`'
    >>> assert data is not Ellipsis, \
    'Assign your result to variable `data`'
    >>> assert type(header) is tuple, \
    'Variable `header` has invalid type, should be tuple'
    >>> assert all(type(x) is tuple for x in data), \
    'All elements in `data` should be tuple'
    >>> assert header not in data, \
    'Header should not be in `data`'

    >>> header
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> data  # doctest: +NORMALIZE_WHITESPACE
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

# Row at index 0 from DATA
# type: tuple[str]
header = ...

# Rows at all the other indexes from DATA (use only getitem)
# type: list[tuple]
data = ...

# Solution
header = DATA[0]
data = []
data.append(DATA[1])
data.append(DATA[2])
data.append(DATA[3])
data.append(DATA[4])
data.append(DATA[5])
data.append(DATA[6])

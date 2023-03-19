"""
* Assignment: Sequence GetItem Header
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: tuple[str]`
    2. Select header from `DATA` (row with index 0)
    3. Write header to `result`
    4. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: tuple[str]`
    2. Wybierz nagłówek z `DATA` (wiersz o indeksie 0)
    3. Zapisz nagłówek do `result`
    4. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is tuple, \
    'Variable `result` has invalid type, should be tuple'
    >>> assert len(result) == 5, \
    'Variable `result` length should be 5'

    >>> result
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# Header from `DATA` (row with index 0)
# type: tuple[str]
result = ...

# Solution
result = DATA[0]

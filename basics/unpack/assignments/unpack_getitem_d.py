"""
* Assignment: Iterable GetItem Select
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create `result: list`
       a. Append to `result` a row from `DATA` at index 2
       b. Append to `result` a row from `DATA` at index 4
       c. Append to `result` a row from `DATA` at index -2
    2. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: list`
       a. Dodaj do `result` wiersz z `DATA` o indeksie 2
       b. Dodaj do `result` wiersz z `DATA` o indeksie 4
       c. Dodaj do `result` wiersz z `DATA` o indeksie -2
    2. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 3, \
    'Variable `result` length should be 6'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [(5.1, 3.5, 1.4, 0.2, 'setosa'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor')]
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

# Empty list
# type: list[list|tuple|set]
result = ...

# Append row from DATA at index 2
...

# Append row from DATA at index 4
...

# Append row from DATA at index -2
...

# Solution
result = []
result.append(DATA[2])
result.append(DATA[4])
result.append(DATA[-2])

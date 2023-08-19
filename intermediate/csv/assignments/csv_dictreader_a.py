"""
* Assignment: CSV DictReader Iris
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Using `csv.DictReader` read the `FILE` content
    2. Use explicit `encoding`, `delimiter` and `quotechar`
    3. Replace column names with `FIELDNAMES`
    4. Skip the first line (header)
    5. Add rows to `result: list[dict]`
    6. Run doctests - all must succeed

Polish:
    1. Korzystając z `csv.DictReader` wczytaj zawartość pliku `FILE`
    2. Podaj jawnie `encoding`, `delimiter` oraz `quotechar`
    3. Podmień nazwy kolumn na `FIELDNAMES`
    4. Pomiń pierwszą linię (nagłówek)
    5. Dodaj wiersze do `result: list[dict]`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1',
      'petal_width': '1.9', 'species': 'virginica'},
     {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4',
      'petal_width': '0.2', 'species': 'setosa'},
     {'sepal_length': '5.7', 'sepal_width': '2.8', 'petal_length': '4.1',
      'petal_width': '1.3', 'species': 'versicolor'}]
"""

import csv


DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

FIELDNAMES = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
    'species',
]

FILE = r'_temporary.csv'

with open(FILE, mode='w') as file:
    file.write(DATA)

# Using `csv.DictReader` read the `FILE` content
# type: list[dict]
result = ...

# Solution
result = []

with open(FILE, mode='rt') as file:
    reader = csv.DictReader(file)
    result = list(reader)

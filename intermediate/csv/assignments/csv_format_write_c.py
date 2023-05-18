"""
* Assignment: CSV Format WriteSchemaless
* Complexity: hard
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Define `header: str` with sorted list of unique keys from `DATA`
    2. `header` must be automatically generated from `DATA`
    3. Iterate over `DATA` and extract values for each header column
    4. Define `result: str` with header and matching values
    5. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: `"`
       c. Quoting: always
       d. Delimiter: `,`
       e. Lineseparator: `\n`
       f. Sort `fieldnames`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `header: str` z posortowaną listą unikalnych kluczy z `DATA`
    2. `header` musi być generowany automatycznie z `DATA`
    3. Iteruj po `DATA` i wyciągnij wartości dla każdej kolumny z nagłówka
    4. Zdefiniuj `result: str` z nagłówkiem i pasującymi wartościami
    5. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: `"`
       c. Quoting: zawsze
       d. Delimiter: `,`
       e. Lineseparator: `\n`
       f. Posortuj `fieldnames`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * sorted()

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "petal_length","petal_width","sepal_length","sepal_width","species"
    "","","5.1","3.5","setosa"
    "4.1","1.3","","","versicolor"
    "","1.8","6.3","","virginica"
    "","0.2","5.0","","setosa"
    "4.1","","","2.8","versicolor"
    "","1.8","","2.9","virginica"
    <BLANKLINE>
"""

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

# header has unique keys from DATA, row values match header columns
# type: str
result = ...

# Solution
result = ''
header = set()

def make_line(data):
    return ','.join(f'"{x}"' for x in data) + '\n'


for row in DATA:
    header.update(row.keys())

header = sorted(header)
result += make_line(header)

for row in DATA:
    line = [row.get(key, '') for key in header]
    result += make_line(line)

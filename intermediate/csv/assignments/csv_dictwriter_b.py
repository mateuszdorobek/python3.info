"""
* Assignment: CSV DictWriter Schemaless
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Using `csv.DictWriter()` write variable schema data to `FILE`
    2. `fieldnames` must be automatically generated from `DATA`
    3. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` line terminator
        e. Sort `fieldnames` using `sorted()`
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz dane o zmiennej strukturze do `FILE`
    2. `fieldnames` musi być generowane automatycznie na podstawie `DATA`
    3. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj `fieldnames` używając `sorted()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

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
import csv


DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

FILE = r'_temporary.csv'


# Write DATA to FILE, generate header from DATA
# type: ContextManager
with open(FILE, mode='w', encoding='utf-8') as file:
    ...


# Solution
fieldnames = set()
for row in DATA:
    fieldnames.update(row.keys())

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(f=file,
                            fieldnames=sorted(fieldnames),
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
    writer.writeheader()
    writer.writerows(DATA)

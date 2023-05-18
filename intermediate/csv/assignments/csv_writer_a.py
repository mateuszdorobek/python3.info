"""
* Assignment: CSV Writer Iris
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Using `csv.writer()` save `DATA` to file
    2. Use Unix `\n` line terminator
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.writer()` zapisz `DATA` do pliku
    2. Użyj zakończenia linii Unix `\n`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

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
    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    7.0,3.2,4.7,1.4,versicolor
    7.6,3.0,6.6,2.1,virginica
    4.9,3.0,1.4,0.2,setosa
    <BLANKLINE>
"""

import csv


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
]

FILE = r'_temporary.csv'


# Write DATA to FILE, generate header from DATA
# type: ContextManager
with open(FILE, mode='w') as file:
    ...

# Solution
with open(FILE, mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(DATA)

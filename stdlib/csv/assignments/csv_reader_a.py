"""
* Assignment: CSV Reader Iris
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Using `csv.reader()` data from file
    2. Define `result: list[tuple]` with converted data
    3. Use Unix `\n` line terminator
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.reader()` data z pliku
    2. Zdefiniuj `result: list[tuple]` z przekonwerowanymi danymi
    3. Użyj zakończenia linii Unix `\n`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     ('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
    >>> from os import remove
    >>> remove(FILE)
"""

import csv


DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

FILE = r'_temporary.csv'


with open(FILE, mode='w') as file:
    file.write(DATA)

# list[tuple]: data from file (note the list[tuple] format!)
result = []

# Solution


with open(FILE, mode='r') as file:
    data = csv.reader(file, lineterminator='\n')
    for row in data:
        result.append(tuple(row))

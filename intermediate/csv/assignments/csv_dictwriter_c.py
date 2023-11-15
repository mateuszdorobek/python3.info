"""
* Assignment: CSV DictWriter Objects
* Complexity: medium
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Using `csv.DictWriter()` save data to `FILE`
    2. Non-functional requirements:
        a. Use `,` to separate columns
        b. Use `utf-8` encoding
        c. Use Unix `\n` line terminator
        d. sort header (fieldnames)
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz dane do `FILE`
    2. Wymagania niefunkcjonalne:
        a. Użyj `,` do oddzielenia kolumn
        b. Użyj kodowania `utf-8`
        c. Użyj zakończenia linii Unix `\n`
        d. posortuj nagłówek (fieldnames)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars()`

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
    petal_length,petal_width,sepal_length,sepal_width,species
    1.4,0.2,5.1,3.5,setosa
    5.1,1.9,5.8,2.7,virginica
    1.4,0.2,5.1,3.5,setosa
    4.1,1.3,5.7,2.8,versicolor
    5.6,1.8,6.3,2.9,virginica
    4.5,1.5,6.4,3.2,versicolor
    <BLANKLINE>
"""

import csv


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


DATA = [
    Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
    Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
    Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
    Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
]

FILE = r'_temporary.txt'


# Write DATA to FILE, generate header from DATA
# type: ContextManager
with open(FILE, mode='w', encoding='utf-8') as file:
    ...


# Solution
data = [vars(iris) for iris in DATA]
header = data[0].keys()

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(header))
    writer.writeheader()
    writer.writerows(data)

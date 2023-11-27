"""
* Assignment: File Write Iris
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Write `DATA` to file `FILE`
    2. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)
    5.8,2.7,5.1,1.9
    5.1,3.5,1.4,0.2
    5.7,2.8,4.1,1.3
    <BLANKLINE>
"""

FILE = '_temporary.txt'
DATA = [
    ('5.8', '2.7', '5.1', '1.9'),
    ('5.1', '3.5', '1.4', '0.2'),
    ('5.7', '2.8', '4.1', '1.3'),
]

# Solution
data = []

for row in DATA:
    line = ','.join(row) + '\n'
    data.append(line)

with open(FILE, mode='wt') as file:
    file.writelines(data)

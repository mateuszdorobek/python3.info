"""
* Assignment: File Write Iris
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Check in your operating system if data was written correctly
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> open(FILE).read()
    '5.8,2.7,5.1,1.9\\n5.1,3.5,1.4,0.2\\n5.7,2.8,4.1,1.3\\n'
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
FILE = r'_temporary.txt'
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

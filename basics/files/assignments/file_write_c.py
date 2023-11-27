"""
* Assignment: File Write List
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Write `DATA` to file `FILE`
    2. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add newline `\n` at the end of line and file
    * `str.join()`
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> result
    'hello,world\\n'
"""

FILE = '_temporary.txt'
DATA = ['hello', 'world']

# Solution
data = ','.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)

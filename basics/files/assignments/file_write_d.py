"""
* Assignment: File Write Non-Str
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
    * `[str(x) for x in data]`
    * `str.join()`
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> result
    '5.1,3.5,1.4,0.2,setosa\\n'
"""

FILE = '_temporary.txt'
DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

# Solution
data = ','.join(str(x) for x in DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)

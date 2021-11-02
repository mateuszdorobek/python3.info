"""
* Assignment: File Write List
* Required: yes
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
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> open(FILE).read()
    'hello\\nworld\\n'

    >>> remove(FILE)
"""

FILE = '_temporary.txt'
DATA = ['hello', 'world']

# Solution
data = '\n'.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)

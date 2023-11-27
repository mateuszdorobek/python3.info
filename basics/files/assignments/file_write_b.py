"""
* Assignment: File Write Multiline
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
    * There is already a newline `\n` at the end of file
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)
    127.0.0.1       localhost
    10.13.37.1      nasa.gov esa.int polsa.gov.pl
    255.255.255.255 broadcasthost
    ::1             localhost
    <BLANKLINE>
"""

FILE = '_temporary.txt'
DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int polsa.gov.pl
255.255.255.255 broadcasthost
::1             localhost"""


# Solution
data = DATA + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)

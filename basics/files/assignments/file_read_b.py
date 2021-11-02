"""
* Assignment: File Read Multiline
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read `FILE` to `result: list[str]`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: list[str]`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> assert type(result) is list
    >>> assert all(type(x) is str for x in result)

    >>> result
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    >>> remove(FILE)
"""

FILE = '_temporary.txt'
DATA = 'sepal_length\nsepal_width\npetal_length\npetal_width\nspecies\n'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# Solution
with open(FILE, mode='rt') as file:
    result = [x.strip() for x in file.readlines()]

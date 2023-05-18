"""
* Assignment: Typing Annotations Alias
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `data` with value 1
       b. Variable `data` with value None
    2. Use alias with | notation (pipe)
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `data` z wartością 1
       b. Zmienna `data` z wartością None
    2. Użyj aliasów z notacją | (pionowej kreski)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data is None, \
    'Do not modify variable `data` value, just add type annotation'
"""

# add proper type annotation for following values
data: ...

data = 1
data = None

# Solution
data: int | None

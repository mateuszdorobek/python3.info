"""
* Assignment: Typing Annotations Union
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `data` with value 0
       b. Variable `data` with value 0.0
    2. Use union with | notation (pipe)
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `data` z wartością 0
       b. Zmienna `data` z wartością 0.0
    2. Użyj unii z notacją | (pionowej kreski)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data == 0.0, \
    'Do not modify variable `data` value, just add type annotation'
"""


# add proper type annotation for following values
data: ...

data = 0
data = 0.0



# Solution
data: int | float

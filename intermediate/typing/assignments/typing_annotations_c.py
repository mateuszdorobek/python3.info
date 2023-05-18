"""
* Assignment: Typing Annotations Alias
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Declare proper types for variables:
       a. Variable `data` with value 0
       b. Variable `data` with value 0.0
    2. Use alias with | notation (pipe)
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `data` z wartością 0
       b. Zmienna `data` z wartością 0.0
    2. Użyj aliasów z notacją | (pionowej kreski)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    # >>> assert data == 0, \
    # 'Do not modify variable `a` value, just add type annotation'
    >>> assert data == 0.0, \
    'Do not modify variable `b` value, just add type annotation'
"""

number = ...

# add proper type annotation for following values
data: number = 0
data: number = 0.0


# Solution
number = int | float

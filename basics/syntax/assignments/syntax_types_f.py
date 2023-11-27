"""
* Assignment: Syntax Types Type
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with
       result of type cheking of DATA
    2. Use `type()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z
       rezultatem sprawdzania typu DATA
    2. Użyj `type()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is type, \
    'Variable `result` has invalid type, should be type'
    >>> assert result is int, \
    'Variable `result` has invalid value, should be int'
"""

DATA = 1

# With value None
# type: type[int]
result = ...


# Solution
result = type(DATA)

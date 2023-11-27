"""
* Assignment: Syntax Types IsInstance
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with
       result of checking if DATA is an instance of an int
    2. Use `isinstnace()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z
       rezultatem sprawdzania czy DATA jest instancją int
    2. Użyj `isinstnace()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is bool, \
    'Variable `result` has invalid type, should be bool'
    >>> assert result is True, \
    'Variable `result` has invalid value, should be True'
"""

DATA = 1

# With value None
# type: bool
result = ...


# Solution
result = isinstance(DATA, int)

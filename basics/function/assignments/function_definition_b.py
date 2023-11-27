"""
* Assignment: Function Definition Call
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Call function `beetlejuice` three times
    2. Run doctests - all must succeed

Polish:
    1. Wywołaj funkcję `beetlejuice` trzy razy
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(beetlejuice), \
    'Object `beetlejuice` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['Beetlejuice', 'Beetlejuice', 'Beetlejuice']
"""

result = []

def beetlejuice():
    result.append('Beetlejuice')


# Solution
beetlejuice()
beetlejuice()
beetlejuice()

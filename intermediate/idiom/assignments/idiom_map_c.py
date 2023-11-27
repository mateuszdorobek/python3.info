"""
* Assignment: Idiom Map Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define function `upper()`:
       a. takes one argument (str)
       b. returns argument uppercased
    2. Use `map()` to apply function `upper()` to DATA
    3. Define `result: map` with result
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funckję `upper()`:
       a. przyjmuje jeden argument (str)
       b. zwraca argument dużymi literami
    2. Użyj `map()` aby zaaplikować funkcję `upper()` do DATA
    3. Zdefiniuj `result: map` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * map()
    * str.upper()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(upper), \
    'Object `upper` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['A', 'B', 'C']
"""

DATA = ['a', 'b', 'c']

# Define function `upper()`:
# - takes one argument (str)
# - returns argument uppercased
# type: Callable[[str], [str]]
def upper():
    ...

# Use `map()` to apply function `upper()` to DATA
# type: map
result = ...

# Solution
def upper(x):
    return x.upper()

result = map(upper, DATA)

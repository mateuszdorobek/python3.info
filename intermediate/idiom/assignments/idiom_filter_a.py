"""
* Assignment: Idiom Filter Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define function `odd()`:
       a. takes one argument
       b. returns True if argument is odd
       c. returns False if argument is even
    2. Use `filter()` to apply function `odd()` to DATA
    3. Define `result: filter` with result
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funckję `odd()`:
       a. przyjmuje jeden argument
       b. zwraca True jeżeli argument jest nieparzysty
       c. zwraca False jeżeli argument jest parzysty
    2. Użyj `filter()` aby zaaplikować funkcję `odd()` do DATA
    3. Zdefiniuj `result: filter` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * filter()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(odd), \
    'Object `odd` must be a function'

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is filter, \
    'Variable `result` has invalid type, should be filter'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is int for x in result), \
    'All rows in `result` should be int'

    >>> result
    [1, 3, 5, 7, 9]
"""


DATA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Returns if number is odd (modulo divisible by 2 without reminder)
# type: Callable[[int], bool]
def odd(x):
    ...

# Cube numbers in DATA
# type: filter
result = ...


# Solution
def odd(x):
    return x % 2

result = filter(odd, DATA)

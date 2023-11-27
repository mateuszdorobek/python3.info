"""
* Assignment: Idiom MapFilter Chain
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use `range()` to get numbers:
       a. from 0 (inclusive)
       b. to 10 (exclusive)
    2. Redefine `result` with odd numbers from `result`
    3. Redefine `result` with cubed numbers from `result`
    4. Redefine `result` with evaluated `result`
    5. At the end `result` must be a `list` type
    6. Run doctests - all must succeed

Polish:
    1. Użyj `range()` aby otrzymać liczby:
       a. od 0 (włącznie)
       b. do 10 (rozłącznie)
    2. Przedefiniuj `result` z nieparzystymi liczbami z `result`
    3. Przedefiniuj `result` z podniesionymi do sześcianiu liczbami z `result`
    4. Przedefiniuj `result` z ewaluaownym `result`
    5. Na końcu `result` musi być typu `list`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * range()
    * map()
    * filter()
    * list()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(odd), \
    'Object `odd` must be a function'
    >>> assert isfunction(cube), \
    'Object `cube` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is int for x in result), \
    'All rows in `result` should be int'

    >>> result
    [1, 27, 125, 343, 729]
"""

def odd(x):
    return x % 2


def cube(x):
    return x ** 3


# Range from 0 to 10 (exclusive)
# type: range
result = ...

# Filter odd numbers
# type: filter
result = ...

# Cube result
# type: map
result = ...

# Get list of results
# type: list[int]
result = ...


# Solution
result = range(0, 10)
result = filter(odd, result)
result = map(cube, result)
result = list(result)

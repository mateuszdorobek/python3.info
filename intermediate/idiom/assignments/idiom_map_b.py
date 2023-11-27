"""
* Assignment: Idiom Map Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define function `cube()`:
       a. takes one argument
       b. returns its argument cubed (raised to the power of 3)
    2. Use `map()` to apply function `cube()` to DATA
    3. Define `result: map` with result
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funckję `cube()`:
       a. przyjmuje jeden argument
       b. zwraca argument podniesiony do sześcianu (do 3 potęgi)
    2. Użyj `map()` aby zaaplikować funkcję `cube()` do DATA
    3. Zdefiniuj `result: map` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * map()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(cube), \
    'Object `cube` must be a function'
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is int for x in result), \
    'All rows in `result` should be int'

    >>> result
    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
"""

DATA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Returns its argument cubed (raised to the power of 3)
# type: Callable[[int], [int]]
def cube(x):
    ...

# Cube numbers in DATA
# type: map
result = ...

# Solution
def cube(x):
    return x ** 3

result = map(cube, DATA)

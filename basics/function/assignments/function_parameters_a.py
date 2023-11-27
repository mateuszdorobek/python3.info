"""
* Assignment: Function Parameters Square
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `square`:
       a. takes `x: int`
       b. returns square of `x`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `square`:
       a. przyjmuje `x: int`
       b. zwraca kwadrat `x`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert square is not Ellipsis, \
    'Write solution inside `square` function'
    >>> assert isfunction(square), \
    'Object `square` must be a function'

    >>> square(2)
    4
    >>> square(8)
    64
    >>> square(32)
    1024
"""

# Returns square of `x`
# type: Callable[[int], int]
...


# Solution
def square(x):
    return x ** 2

"""
* Assignment: Function Parameters IsEven
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `is_even`:
       a. takes `x: int`
       b. returns True/False if `x` is even
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `is_even`:
       a. przyjmuje `x: int`
       b. zwraca True/False czy `x` jest parzysty
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert is_even is not Ellipsis, \
    'Write solution inside `is_even` function'
    >>> assert isfunction(is_even), \
    'Object `is_even` must be a function'

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    >>> is_even(6)
    True
    >>> is_even(7)
    False
"""

# Returns True/False if `x` is even
# type: Callable[[int], bool]
...


# Solution
def is_even(x):
    return x % 2 == 0

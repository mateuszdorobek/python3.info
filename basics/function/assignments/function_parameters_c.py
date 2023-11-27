"""
* Assignment: Function Parameters Sum
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define function `total`:
       a. takes `data: tuple|list|set` of objects `int | float`
       b. returns sum of all values in a sequence
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `total`:
       a. przyjmuje `data: tuple|list|set` obiektów `int | float`
       b. zwraca sumę wszystkich wartości z sekwencji
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sum()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert total is not Ellipsis, \
    'Write solution inside `total` function'
    >>> assert isfunction(total), \
    'Object `total` must be a function'

    >>> total([1,2,3])
    6
    >>> total([1,2,3,4,5,6])
    21
    >>> total(range(0,101))
    5050
"""

# Returns sum of all values in a sequence
# type: Callable[[tuple|list|set], int]
...


# Solution
def total(data):
    return sum(data)

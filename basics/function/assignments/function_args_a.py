"""
* Assignment: Function Arguments Sequence
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function which takes sequence of integers as an argument
    2. Sum only even numbers, use `even()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    2. Zsumuj tylko parzyste liczby, użyj `even()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert total is not Ellipsis, \
    'Write solution inside `total` function'
    >>> assert isfunction(total), \
    'Object `total` must be a function'

    >>> total([1,2,3,4])
    6
    >>> total([2,-1,0,2])
    4
    >>> total(range(0,101))
    2550
"""

def even(x):
    return x % 2 == 0

# Solution
def total(sequence):
    return sum(x for x in sequence if even(x))

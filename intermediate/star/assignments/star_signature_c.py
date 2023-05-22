"""
* Assignment: Star Signature Mixed
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min
* Warning: This assignment will work only in Python 3.8+

English:
    1. Create function `compute`, which always returns `None`
    2. Function takes arguments:
       a. `a, b, c` - positional only
       b. `func` - keyword only
    3. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `compute`, która zawsze zwraca `None`
    2. Funkcja przyjmuje argumenty:
       a. `a, b, c` - tylko pozycyjne
       b. `func` - tylko keyword
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert callable(compute)
    >>> assert isfunction(compute)

    >>> compute(1, 2, 3)
    >>> compute(1, 2, 3, func=lambda:None)

    >>> compute(1, 2)
    Traceback (most recent call last):
    TypeError: compute() missing 1 required positional argument: 'c'

    >>> compute()  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: compute() missing 3 required positional arguments: 'a', 'b',
    and 'c'

    >>> compute(1, 2, 3, lambda:None)
    Traceback (most recent call last):
    TypeError: compute() takes 3 positional arguments but 4 were given

    >>> compute(a=1, b=2, c=3)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: compute() got some positional-only arguments passed as
    keyword arguments: 'a, b, c'
"""


# Argument a,b,c must be passed only as positional, func as keyword
# type: Callable[[int,int,int,Callable],None]
def compute(a, b, c, func=lambda: ...):
    pass


# Solution
def compute(a, b, c, /, *, func=lambda: ...):
    pass

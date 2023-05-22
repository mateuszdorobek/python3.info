"""
* Assignment: Star Parameters Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create function `mean()`, which calculates arithmetic mean
    2. Function can have arbitrary number of positional arguments

Polish:
    1. Napisz funkcję `mean()`, wyliczającą średnią arytmetyczną
    2. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów

Non-functional requirements:
    * Do not import any libraries and modules
    * Use builtin functions `sum()` and `len()`
    * Run doctests - all must succeed

Hints:
    * `raise ValueError('error message')`
    * `sum(...) / len(...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mean(1)
    1.0
    >>> mean(1, 2)
    1.5
    >>> mean(1, 2, 3)
    2.0
    >>> mean(1, 2, 3, 4)
    2.5
    >>> mean()
    Traceback (most recent call last):
    ValueError: At least one argument is required
"""


# Solution
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)

"""
* Assignment: Star Signature Kwargs
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create function `set_position`
    2. Function takes two arguments `x`, `y` and always returns `None`
    3. Arguments must be passed only as keywords
    4. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `set_position`
    2. Funkcja przyjmuje dwa argumenty `x`, `y` i zawsze zwraca `None`
    3. Argumenty można podawać tylko nazwanie (keyword)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert callable(set_position)
    >>> assert isfunction(set_position)

    >>> set_position(x=1, y=2)

    >>> set_position()  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: set_position() missing 2 required keyword-only arguments: 'x'
    and 'y'

    >>> set_position(1)
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 1 was given

    >>> set_position(1, 2)
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 2 were given

    >>> set_position(1, y=1)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 1 positional
    argument (and 1 keyword-only argument) were given

    >>> set_position(x=1, 2)
    Traceback (most recent call last):
    SyntaxError: positional argument follows keyword argument
"""


# Arguments must be passed only as keywords
# type: Callable[[int,int],None]
def set_position(x, y):
    pass


# Solution
def set_position(*, x, y):
    pass

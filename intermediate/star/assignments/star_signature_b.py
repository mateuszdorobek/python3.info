"""
* Assignment: Unpack ParameterSyntax Args
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min
* Warning: This assignment will work only in Python 3.8+

English:
    1. Refactor function `take_damage`
    2. Function takes one argument `dmg` and always returns `None`
    3. Argument must be passed only as positional
    4. Run doctests - all must succeed

Polish:
    1. Zrefaktoruj funkcję `take_damage`
    2. Funkcja przyjmuje jeden argument `dmg` i zawsze zwraca `None`
    3. Argument można podawać tylko pozycyjnie
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert callable(take_damage)
    >>> assert isfunction(take_damage)

    >>> take_damage(1)

    >>> take_damage(1, 2)
    Traceback (most recent call last):
    TypeError: take_damage() takes 1 positional argument but 2 were given

    >>> take_damage()
    Traceback (most recent call last):
    TypeError: take_damage() missing 1 required positional argument: 'dmg'

    >>> take_damage(dmg=1)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: take_damage() got some positional-only arguments passed as
    keyword arguments: 'dmg'
"""


# Argument must be passed only as positional
# type: Callable[[int],None]
def take_damage(dmg):
    pass


# Solution
def take_damage(dmg, /):
    pass

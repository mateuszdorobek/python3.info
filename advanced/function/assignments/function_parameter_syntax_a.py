"""
* Assignment: Function Parameter Syntax Kwargs
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create function `set_position`
    2. Function takes two arguments `x`, `y` and always returns `None`
    3. Arguments must be passed only as keywords
    4. Test function by running with keyword arguments
    5. Test function by running with positional arguments
    6. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `set_position`
    2. Funkcja przyjmuje dwa argumenty `x`, `y` i zawsze zwraca `None`
    3. Argumenty można podawać tylko nazwanie (keyword)
    4. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    5. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> from inspect import isfunction
    >>> assert callable(set_position)
    >>> assert isfunction(set_position)

    >>> set_position(x=1, y=2)

    >>> set_position()
    Traceback (most recent call last):
    TypeError: set_position() missing 2 required keyword-only arguments: 'x' and 'y'

    >>> set_position(1)
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 1 was given

    >>> set_position(1, 2)
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 2 were given

    >>> set_position(1, y=1)
    Traceback (most recent call last):
    TypeError: set_position() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

    >>> set_position(x=1, 2)
    Traceback (most recent call last):
    SyntaxError: positional argument follows keyword argument
"""


# Solution
def set_position(*, x, y):
    ...

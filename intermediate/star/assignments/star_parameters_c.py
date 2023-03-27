"""
* Assignment: Unpack Parameters Kwargs
* Complexity: medium
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Create function `isnumeric`
    2. Function takes arbitrary number of positional and keyword arguments
    3. Arguments can be of any type
    4. Return `True` if all arguments are `int` or `float` only
    5. Return `False` if any argument is different type
    6. Do not use `all()` and `any()`
    7. Compare using `type()` and `isinstance()` passing `True` as an argument
    8. Run the function without any arguments
    9. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `isnumeric`
    2. Funkcja przyjmuje dowolną liczbę argumentów pozycyjnych i nazwanych
    3. Podawane argumenty mogą być dowolnego typu
    4. Zwróć `True` jeżeli wszystkie argumenty są tylko typów `int` lub `float`
    5. Zwróć `False` jeżeli którykolwiek jest innego typu
    6. Nie używaj `all()` oraz `any()`
    7. Porównaj użycie `type()` i `isinstance()` podając `True` jako argument
    8. Uruchom funkcję bez podawania argumentów
    9. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `isinstance(obj, (type1, type2))`
    * `type(obj)`
    * `len()`
    * `dict.values()`
    * `tuple() + tuple()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(isnumeric), \
    'isnumeric must be a function'

    >>> isnumeric()
    False
    >>> isnumeric(0)
    True
    >>> isnumeric(1)
    True
    >>> isnumeric(-1)
    True
    >>> isnumeric(1.1)
    True
    >>> isnumeric('one')
    False
    >>> isnumeric([1, 1.1])
    False
    >>> isnumeric(1, 1.1)
    True
    >>> isnumeric(1, 'one')
    False
    >>> isnumeric(1, 'one', 'two')
    False
    >>> isnumeric(True)
    False
    >>> isnumeric(a=1)
    True
    >>> isnumeric(a=1.1)
    True
    >>> isnumeric(a='one')
    False
"""


# Return True if all arguments are int or float, otherwise False
# type: Callable[[int|float],bool]
def isnumeric(*args, **kwargs):
    ...


# Solution
def isnumeric(*args, **kwargs):
    args += tuple(kwargs.values())

    if not args:
        return False

    for arg in args:
        if type(arg) not in (float, int):
            return False

    return True

"""
* Assignment: Test Doctest Temperature
* Type: homework
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Write doctests to `celsius_to_kelvin` function
    2. Parameter `degrees` can be:
        a. int
        b. float
        c. list[int|float]
        d. tuple[int|float,...]
        e. set[int|float]
        f. In other case raise an exception: TypeError
           with message: "Invalid argument type"
    3. Run doctests - all must succeed

Polish:
    1. Napisz doctesty do funkcji `celsius_to_kelvin`
    2. Parametr `degrees` może być:
        a. int
        b. float
        c. list[int|float]
        d. tuple[int|float,...]
        e. set[int|float]
        f. W przeciwnym wypadku podnieś wyjątek: TypeError
           z komunikatem: "Invalid argument type"
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction
"""

def celsius_to_kelvin(degrees):
    if type(degrees) in (int, float):
        return 273.15 + degrees
    if type(degrees) in (list, tuple, set):
        cls = type(degrees)
        return cls(x+273.15 for x in degrees)
    raise TypeError('Invalid argument type')


# Solution
"""
>>> isfunction(celsius_to_kelvin)
True
>>> celsius_to_kelvin(0)
273.15
>>> celsius_to_kelvin(1)
274.15
>>> celsius_to_kelvin(-1)
272.15
>>> celsius_to_kelvin('a')
Traceback (most recent call last):
TypeError: Invalid argument type
>>> celsius_to_kelvin([0, 1])
[273.15, 274.15]
>>> celsius_to_kelvin((0, 1))
(273.15, 274.15)
>>> celsius_to_kelvin({0, 1})
{273.15, 274.15}
"""

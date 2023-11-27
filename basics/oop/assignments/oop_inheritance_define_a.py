"""
* Assignment: OOP Inheritance Simple
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create class `Woman` which inherits from `Venus`
    2. Create class `Man` which inherits from `Mars`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Woman`, która dziedziczy po `Venus`
    2. Stwórz klasę `Man`, która dziedziczy po `Mars`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Venus)
    >>> assert isclass(Woman)
    >>> assert isclass(Mars)
    >>> assert isclass(Man)
    >>> assert issubclass(Woman, Venus)
    >>> assert issubclass(Man, Mars)
"""


class Venus:
    pass


class Mars:
    pass


# Solution
class Woman(Venus):
    pass


class Man(Mars):
    pass

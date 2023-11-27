"""
* Assignment: OOP Method Syntax
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define class `Calculator`
    2. Define method `add` in class `Calculator`
    3. Method `add` take `a` and `b` as arguments
    4. Method returns sum of `a` and `b`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Calculator`
    2. Zdefiniuj metodę `add` w klasie `Calculator`
    3. Metoda `add` przyjmuje `a` i `b` jako argumenty
    4. Metoda zwraca sumę `a` i `b`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Calculator)
    >>> calc = Calculator()
    >>> assert ismethod(calc.add)
    >>> calc.add(1, 2)
    3
"""


# Solution
class Calculator:
    def add(self, a, b):
        return a + b

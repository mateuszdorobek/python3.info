"""
* Assignment: OOP Method Mean
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define class `Stats`
    2. Define method `mean()` in `Stats` class
    3. Method takes `data: list[float]` as an argument
    4. Method returns arithmetic mean of the `data`
    5. Returned value must be rounded to one decimal places
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Stats`
    2. Zdefiniuj metodę `mean()` w klasie `Stats`
    3. Metoda przyjmuje `data: list[float]` jako argument
    4. Metoda zwraca średnią arytmetyczną z `data`
    5. Zwracana wartość ma być zaokrąglona do jednego miejsca po przecinku
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `round()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Stats)
    >>> stats = Stats()
    >>> assert ismethod(stats.mean)

    >>> stats.mean([1, 2])
    1.5
    >>> stats.mean([5.8, 2.7, 5.1, 1.9])
    3.9
"""


# Solution
class Stats:
    def mean(self, data):
        mean = sum(data) / len(data)
        return round(mean, 1)

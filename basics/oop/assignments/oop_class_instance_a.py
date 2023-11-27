"""
* Assignment: OOP Class Iris
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Create instance `setosa` of a class `Iris`
    2. Create instance `virginica` of a class `Iris`
    3. Create instance `versicolor` of a class `Iris`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz instancję `setosa` klasy `Iris`
    2. Stwórz instancję `virginica` klasy `Iris`
    3. Stwórz instancję `versicolor` klasy `Iris`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Iris)
    >>> assert isinstance(setosa, Iris)
    >>> assert isinstance(versicolor, Iris)
    >>> assert isinstance(virginica, Iris)
"""

class Iris:
    pass



# Solution
setosa = Iris()
versicolor = Iris()
virginica = Iris()

"""
* Assignment: OOP Class Instance
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define class `Astronaut`
    2. Define class `SpaceAgency`
    3. Create instance `watney` of a class `Astronaut`
    4. Create instance `nasa` of a class `SpaceAgency`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Astronaut`
    2. Zdefiniuj klasę `SpaceAgency`
    3. Stwórz instancję `watney` klasy `Astronaut`
    4. Stwórz instancję `nasa` klasy `SpaceAgency`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Astronaut)
    >>> assert isclass(SpaceAgency)
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
"""

class Astronaut:
    pass


class SpaceAgency:
    pass



# Solution
watney = Astronaut()
nasa = SpaceAgency()

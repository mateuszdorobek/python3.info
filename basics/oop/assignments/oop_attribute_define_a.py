"""
* Assignment: OOP Attribute Define
* Required: yes
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Modify code below
    2. Add type annotation attibutes to model the data:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Dodaj anotację typów atrybutów by zamodelować dane:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert len(Astronaut.__annotations__) == 3
    >>> assert len(SpaceAgency.__annotations__) == 3
"""


# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29

class Astronaut:
    ...


class SpaceAgency:
    ...


# Solution
class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str

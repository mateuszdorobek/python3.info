"""
* Assignment: OOP Attribute Set
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Modify code below
    2. Set attibutes of watney and nasa instances to model the data:
       a. Mark, USA, 1969-07-21
       b. Nasa, USA, 1969-07-21
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Ustaw atrybuty instancji watney i nasa by zamodelować dane:
       a. Mark, USA, 1969-07-21
       b. Nasa, USA, 1969-07-21
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert isinstance(mark, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Mark' in vars(mark).values()
    >>> assert 'USA' in vars(mark).values()
    >>> assert '1969-07-21' in vars(mark).values()
    >>> assert 'Nasa' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1969-07-21' in vars(nasa).values()
"""


class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str


mark = Astronaut()
nasa = SpaceAgency()

# Mark, USA, 1969-07-21
# Nasa, USA, 1969-07-21


# Solution
mark.name = 'Mark'
mark.country = 'USA'
mark.date = '1969-07-21'

nasa.name = 'Nasa'
nasa.country = 'USA'
nasa.date = '1969-07-21'

"""
* Assignment: OOP Init SetAttrPositional
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Modify code below
    2. Create instances of an `Astronaut` and `SpaceAgency` classes
    3. Use positional arguments to pass values at the initialization
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Stwórz instancje klas `Astronaut` i `SpaceAgency`
    3. Użyj argumentów pozycyjnych do przekazania wartości przy inicjalizacji
    4. Uruchom doctesty - wszystkie muszą się powieść

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
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


# use positional arguments to create instance with: Mark, USA, 1969-07-21
# type: Astronaut
mark = ...

# use positional arguments to create instance with: Nasa, USA, 1969-07-21
# type: SpaceAgency
nasa = ...


# Solution
mark = Astronaut('Mark', 'USA', '1969-07-21')
nasa = SpaceAgency('Nasa', 'USA', '1969-07-21')

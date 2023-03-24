"""
* Assignment: OOP Init Define
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Modify code below
    2. Define `__init__()` method in both classes
    3. Signature should reflect class attributes
    4. Method `__init__()` raises exception `NotImplementedError`
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Zdefiniuj metodę `__init__()` w obu klasach
    3. Sygnaturą powinna odpowiadać atrybutom klasy
    4. Metoda `__init__()` ma podnosić wyjątek `NotImplementedError`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import ismethod, signature

    >>> mark = Astronaut('Mark', 'USA', '1969-07-21')
    Traceback (most recent call last):
    NotImplementedError

    >>> nasa = Astronaut('Nasa', 'USA', '1969-07-21')
    Traceback (most recent call last):
    NotImplementedError

    >>> signature(Astronaut.__init__)
    <Signature (self, name, country, date)>
    >>> signature(SpaceAgency.__init__)
    <Signature (self, name, country, date)>
"""


class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str


# Solution
class Astronaut:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        raise NotImplementedError


class SpaceAgency:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        raise NotImplementedError

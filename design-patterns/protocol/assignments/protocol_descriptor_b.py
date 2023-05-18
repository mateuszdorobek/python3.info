"""
* Assignment: Protocol Descriptor Number
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Define descriptor class `Number` with attributes:
        a. `min: float`
        b. `max: float`
    2. Modify class `Astronaut` and add attributes:
        a. `age: int = Number(min=30, max=50)`
        b. `height: float = Number(min=150, max=200)`
        c. `weight: float = Number(min=50, max=100)`
    3. Setting `Astronaut` attribute should invoke boundary check
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę-deskryptor `Number` z atrybutami:
        a. `min: float`
        b. `max: float`
    2. Zmodyfikuj klasę `Astronaut` i dodaj atrybuty:
        a. `age: int = Number(min=30, max=50)`
        b. `height: float = Number(min=150, max=200)`
        c. `weight: float = Number(min=50, max=100)`
    3. Ustawianie atrybutu `Astronaut` powinno wywołać sprawdzanie zakresu
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = Astronaut('Mark', 'Watney', age=42, height=178.0, weight=75.5)

    >>> melissa = Astronaut('Melissa', 'Lewis', age=60, height=178.0, weight=75.5)
    Traceback (most recent call last):
    ValueError: Age is not between 30 and 50

    >>> alex = Astronaut('Alex', 'Vogel', age=42, height=201, weight=75.5)
    Traceback (most recent call last):
    ValueError: Height is not between 150 and 200
"""
from dataclasses import dataclass, field


@dataclass
class Number:
    ...


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    age: int = ...
    height: float = ...
    weight: float = ...


# Solution
@dataclass
class Number:
    min: float
    max: float
    attrname: str = field(init=False)
    field: str = field(init=False)

    def __set_name__(self, owner, name):
        self.attrname = f'_{name}'
        self.field = name.capitalize()

    def __set__(self, instance, value):
        if not self.min <= value < self.max:
            error = f'{self.field} is not between {self.min} and {self.max}'
            raise ValueError(error)
        setattr(instance, self.attrname, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.attrname)


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    age: int = Number(min=30, max=50)
    height: float = Number(min=150, max=200)
    weight: float = Number(min=50, max=100)

"""
* Assignment: OOP AttributeMutability Dataclass Randint
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create dataclass `User`, with attributes:
        a. `name: str` (required)
        b. `health: int` (optional), default: randint(50, 100)
        c. `gold: int` (optional), default: randint(1, 100)
    2. Attributes must be set st the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Run doctests - all must succeed

Polish:
    1. Stwórz dataklasę `User`, z atrybutami:
        a. `name: str` (wymagane)
        b. `health: int` (opcjonalne), domyślnie: randint(50, 100)
        c. `gold: int` (opcjonalne), domyślnie: randint(1, 100)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu motowalnych parametrów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Hero)
    >>> assert hasattr(Hero, '__annotations__')

    >>> assert 'name' in Hero.__dataclass_fields__
    >>> assert 'health' in Hero.__dataclass_fields__
    >>> assert 'gold' in Hero.__dataclass_fields__
"""
from dataclasses import dataclass, field
from random import randint


# Create dataclass `User`, with attributes:
# - `name: str` (required)
# - `health: int` (optional), default: randint(50, 100)
# - `gold: int` (optional), default: randint(1, 100)
# type: type[User]
@dataclass
class Hero:
    ...


# Solution
@dataclass
class Hero:
    name: str
    health: int = field(default_factory=lambda: randint(50, 100))
    gold: int = field(default_factory=lambda: randint(1, 100))

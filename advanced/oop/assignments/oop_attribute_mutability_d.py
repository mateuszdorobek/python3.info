"""
* Assignment: OOP AttributeMutability Dataclass Randint
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create dataclass `User`, with attributes:
        a. `name: str` (required)
        b. `health: int` (optional), default: randint(50, 100)
    2. Attributes must be set st the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Użyj funkcji `randint()` z biblioteki `random`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz dataklasę `User`, z atrybutami:
        a. `name: str` (wymagane)
        b. `health: int` (opcjonalne), domyślnie: randint(50, 100)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu motowalnych parametrów
    4. Użyj funkcji `randint()` z biblioteki `random`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from random import seed; seed(0)

    >>> assert isclass(Hero)
    >>> assert hasattr(Hero, '__annotations__')

    >>> assert 'name' in Hero.__dataclass_fields__
    >>> assert 'health' in Hero.__dataclass_fields__

    >>> warrior = Hero('Warrior')
    >>> assert warrior.name == 'Warrior'
    >>> assert warrior.health == 74

    >>> mage = Hero('Mage')
    >>> assert mage.name == 'Mage'
    >>> assert mage.health == 98

    >>> rouge = Hero('Rouge')
    >>> assert rouge.name == 'Rouge'
    >>> assert rouge.health == 76

    >>> cleric = Hero('Cleric')
    >>> assert cleric.name == 'Cleric'
    >>> assert cleric.health == 52
"""
from dataclasses import dataclass, field
from random import randint


# Create dataclass `User`, with attributes:
# - `name: str` (required)
# - `health: int` (optional), default: randint(50, 100)
# type: type[Hero]
@dataclass
class Hero:
    ...


# Solution
@dataclass
class Hero:
    name: str
    health: int = field(default_factory=lambda: randint(50, 100))

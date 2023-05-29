"""
* Assignment: OOP AttributeMutability Dataclass list
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create dataclass `User`, with attributes:
        a. `firstname: str` (required)
        b. `lastname: str` (required)
        c. `groups: list[str]` (optional)
    2. Attributes must be set st the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Run doctests - all must succeed

Polish:
    1. Stwórz dataklasę `User`, z atrybutami:
        a. `firstname: str` (wymagane)
        b. `lastname: str` (wymagane)
        c. `groups: list[str]` (opcjonalne)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu motowalnych parametrów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> assert 'firstname' in User.__dataclass_fields__
    >>> assert 'lastname' in User.__dataclass_fields__
    >>> assert 'groups' in User.__dataclass_fields__

    >>> mark = User('Mark', 'Watney')
    >>> assert mark.firstname == 'Mark'
    >>> assert mark.lastname == 'Watney'
    >>> assert mark.groups == []

    >>> melissa = User('Melissa', 'Lewis', groups=['user', 'staff', 'admin'])
    >>> assert melissa.firstname == 'Melissa'
    >>> assert melissa.lastname == 'Lewis'
    >>> assert melissa.groups == ['user', 'staff', 'admin']

    >>> assert id(mark.groups) != id(melissa.groups)
"""
from dataclasses import dataclass, field


# Create class `User`, with attributes:
# - `firstname: str` (required)
# - `lastname: str` (required)
# - `groups: list[str]` (optional)
# type: type[User]
@dataclass
class User:
    ...


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[str] = field(default_factory=list)

"""
* Assignment: OOP AttributeAccessModifiers Dataclass
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Modify dataclass `User` to add attributes:
        a. Public: `firstname`, `lastname`
        b. Protected: `email`, `phone`
        c. Private: `username`, `password`
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dataclass `User` aby dodać atrybuty:
        a. Publiczne: `firstname`, `lastname`
        b. Chronione: `email`, `phone`
        c. Prywatne: `username`, `password`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> assert 'firstname' in User.__dataclass_fields__
    >>> assert 'lastname' in User.__dataclass_fields__
    >>> assert '_phone' in User.__dataclass_fields__
    >>> assert '_email' in User.__dataclass_fields__
    >>> assert '_User__username' in User.__dataclass_fields__
    >>> assert '_User__password' in User.__dataclass_fields__
"""
from dataclasses import dataclass


# Public attributes: `firstname`, `lastname`
# Protected attributes: `email`, `phone`
# Private attributes: `username`, `password`
# type: type[User]
@dataclass
class User:
    pass


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    _phone: str
    _email: str
    __username: str
    __password: str

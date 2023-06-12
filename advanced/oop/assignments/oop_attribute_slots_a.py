"""
* Assignment: OOP AttributeSlots Dataclass
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define dataclass `User` with slots:
       a. `firstname: str`
       b. `lastname: str`
       c. `email: str`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj dataklasę `User` z slotami:
       a. `firstname: str`
       b. `lastname: str`
       c. `email: str`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from dataclasses import is_dataclass

    >>> assert hasattr(User, '__slots__')
    >>> assert 'username' in User.__slots__
    >>> assert 'password' in User.__slots__
    >>> assert 'email' in User.__slots__

    >>> assert User is not Ellipsis, \
    'Assign result to variable: `User`'
    >>> assert type(User) is type, \
    'Result must be a type'
    >>> assert is_dataclass(User), \
    'Class User has to be dataclass'

    >>> result = User(
    ...     username='Mark',
    ...     password='Ares3',
    ...     email='mwatney@nasa.gov')

    >>> assert not hasattr(result, '__dict__')
    >>> assert not hasattr(result, '__weakref__')
"""
from dataclasses import dataclass


# Define dataclass `User` with slots:
# - `firstname: str`
# - `lastname: str`
# - `email: str`
# type: type[User]
@dataclass
class User:
    ...


# Solution
@dataclass(slots=True)
class User:
    username: str
    password: str
    email: str

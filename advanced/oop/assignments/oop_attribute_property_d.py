"""
* Assignment: Protocol Property Age
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define class `User` with attributes:
        a. `username: str`
        b. `password: str`
        c. `birthday: date`
    2. Define property `age`
    3. Accessing `age` should return user's age in full years
    4. Run doctests - all must succeed

Polish:
    1. Define class `User` with attributes:
        a. `username: str`
        b. `password: str`
        c. `birthday: date`
    2. Zdefiniuj property `age`
    3. Dostęp do `age` powinien zwrócić wiek użytkownika w pełnych latach
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * date.today()
    * timedelta.days
    * int()

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User(
    ...     username='Mark',
    ...     password='Ares3',
    ...     birthday=date(2000, 1, 1))

    >>> assert hasattr(mark, 'age'), \
    'Define property `age`'

    >>> mark.age
    23
"""

from dataclasses import dataclass
from datetime import date

YEAR = 365.25


# Define class `User` with attributes:
# - `username: str`
# - `password: str`
# - `birthday: date`
# Define property `age`
# Accessing `age` should return user's age in full years
# type: type[User]
@dataclass
class User:
    username: str
    password: str
    birthday: date


# Solution
@dataclass
class User:
    username: str
    password: str
    birthday: date

    @property
    def age(self):
        today = date.today()
        days = (today - self.birthday).days
        return int(days / YEAR)

"""
* Assignment: Protocol Property Age
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define class `User` with attributes:
        a. Attribute `username: str`
        b. Attribute `password: str`
        c. Attribute `birthday: date`
        d. Property `age`
    2. Accessing `age` should return user's age in full years
    3. Run doctests - all must succeed

Polish:
    1. Define class `User` with attributes:
        a. Atrybut `username: str`
        b. Atrybut `password: str`
        c. Atrybut `birthday: date`
        d. Property `age`
    2. Dostęp do `age` powinien zwrócić wiek użytkownika w pełnych latach
    3. Uruchom doctesty - wszystkie muszą się powieść

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


@dataclass
class User:
    username: str
    password: str
    birthday: date

    # Accessing `age` should return user's age in full years
    # type: Callable[[Self], int]
    def age():
        ...


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

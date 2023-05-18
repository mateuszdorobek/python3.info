"""
* Assignment: Pickle File Serialize
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Save `DATA` to `FILE`
    2. Use `pickle` module
    3. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do `FILE`
    2. Użyj modułu `pickle`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> with open(FILE, mode='rb') as file:
    ...     result = pickle.load(file)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Mark', lastname='Watney', groups=[Group(gid=1, name='users')]),
     User(firstname='Melissa', lastname='Lewis', groups=[Group(gid=1, name='users'), Group(gid=2, name='admins')]),
     User(firstname='Rick', lastname='Martinez', groups=[])]

    >>> remove(FILE)
"""

import pickle
from dataclasses import dataclass, field

FILE = r'_temporary.pkl'

@dataclass
class Group:
    gid: int
    name: str


@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group] | None


DATA = [
    User('Mark', 'Watney', groups=[
        Group(gid=1, name='users')]),
    User('Melissa', 'Lewis', groups=[
        Group(gid=1, name='users'),
        Group(gid=2, name='admins')]),
    User('Rick', 'Martinez', groups=[]),
]


# Solution
with open(FILE, mode='wb') as file:
    pickle.dump(DATA, file)

"""
* Assignment: Pickle File Deserialize
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result: list[Astronaut]` with data from `FILE`
    2. Use `pickle` module
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[Astronaut]` z danymi z `FILE`
    2. Użyj modułu `pickle`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Mark', lastname='Watney', groups=[Group(gid=1, name='users')]),
     User(firstname='Melissa', lastname='Lewis', groups=[Group(gid=1, name='users'), Group(gid=2, name='admins')]),
     User(firstname='Rick', lastname='Martinez', groups=[])]

    >>> remove(FILE)
"""

import pickle
from dataclasses import dataclass, field

FILE = r'_temporary.pkl'
DATA = (
    b'\x80\x04\x95\xf9\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\rpickle_file_a'
    b'\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04'
    b'Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x06groups\x94]\x94h'
    b'\x01\x8c\x05Group\x94\x93\x94)\x81\x94}\x94(\x8c\x03gid\x94K\x01\x8c'
    b'\x04name\x94\x8c\x05users\x94ubaubh\x03)\x81\x94}\x94(h\x06\x8c\x07'
    b'Melissa\x94h\x08\x8c\x05Lewis\x94h\n]\x94(h\r)\x81\x94}\x94(h\x10K'
    b'\x01h\x11h\x12ubh\r)\x81\x94}\x94(h\x10K\x02h\x11\x8c\x06admins\x94'
    b'ubeubh\x03)\x81\x94}\x94(h\x06\x8c\x04Rick\x94h\x08\x8c\x08Martinez'
    b'\x94h\n]\x94ube.'
)

with open(FILE, mode='wb') as file:
    file.write(DATA)


@dataclass
class Group:
    gid: int
    name: str


@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group] | None


# Solution
with open(FILE, mode='rb') as file:
    result = pickle.load(file)

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
    [Astronaut(name='Pan Twardowski', missions=[Mission(year=1969, name='Apollo 18'), Mission(year=2024, name='Artemis 3')]),
     Astronaut(name='Mark Watney', missions=[Mission(year=2035, name='Ares 3')]),
     Astronaut(name='Melissa Lewis', missions=[])]

    >>> remove(FILE)
"""

import pickle
from dataclasses import dataclass, field

FILE = r'_temporary.pkl'
DATA = (b'\x80\x04\x95\xf6\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\r'
        b'pickle_file_a\x94\x8c\tAstronaut\x94\x93\x94)\x81\x94}\x94'
        b'(\x8c\x04name\x94\x8c\x0ePan Twardowski\x94\x8c\x08missions'
        b'\x94]\x94(h\x01\x8c\x07Mission\x94\x93\x94)\x81\x94}\x94(\x8c'
        b'\x04year\x94M\xb1\x07h\x06\x8c\tApollo 18\x94ubh\x0b)\x81\x94}'
        b'\x94(h\x0eM\xe8\x07h\x06\x8c\tArtemis 3\x94ubeubh\x03)\x81\x94}'
        b'\x94(h\x06\x8c\x0bMark Watney\x94h\x08]\x94h\x0b)\x81\x94}\x94'
        b'(h\x0eM\xf3\x07h\x06\x8c\x06Ares 3\x94ubaubh\x03)\x81\x94}\x94'
        b'(h\x06\x8c\rMelissa Lewis\x94h\x08]\x94ube.')

with open(FILE, mode='wb') as file:
    file.write(DATA)


@dataclass
class Astronaut:
    name: str
    missions: list = field(default_factory=list)


@dataclass
class Mission:
    year: int
    name: str


# Solution
with open(FILE, mode='rb') as file:
    result = pickle.load(file)

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
    [Astronaut(name='Pan Twardowski', missions=[Mission(year=1969, name='Apollo 18'), Mission(year=2024, name='Artemis 3')]),
     Astronaut(name='Mark Watney', missions=[Mission(year=2035, name='Ares 3')]),
     Astronaut(name='Melissa Lewis', missions=[])]

    >>> remove(FILE)
"""

import pickle
from dataclasses import dataclass, field

FILE = r'_temporary.pkl'


@dataclass
class Astronaut:
    name: str
    missions: list = field(default_factory=list)


@dataclass
class Mission:
    year: int
    name: str


DATA = [
    Astronaut('Pan Twardowski', missions=[
        Mission(1969, 'Apollo 18'),
        Mission(2024, 'Artemis 3')]),

    Astronaut('Mark Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa Lewis'),
]


# Solution
with open(FILE, mode='wb') as file:
    pickle.dump(DATA, file)

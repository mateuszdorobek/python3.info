"""
* Assignment: Pandas Read PythonObj
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Non-functional requirements:
        a. Use `,` to separate mission fields
        b. Use `;` to separate missions
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Wymagania niefunkcjonalne:
        a. Użyj `,` do oddzielania pól mission
        b. Użyj `;` do oddzielenia missions
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * dict.pop()
    * Nested `for`
    * `str.join(';', sequence)`
    * `str.join(',', sequence)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` has invalid type, should be `pd.DataFrame`'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname                 missions
    0      Mark    Watney              2035,Ares 3
    1   Melissa     Lewis  2030,Ares 1;2035,Ares 3
    2      Rick  Martinez
"""

import pandas as pd


class Astronaut:
    def __init__(self, firstname, lastname, missions=None):
        self.firstname = firstname
        self.lastname = lastname
        self.missions = list(missions) if missions else []


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


DATA = [
    Astronaut('Mark', 'Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa', 'Lewis', missions=[
        Mission(2030, 'Ares 1'),
        Mission(2035, 'Ares 3')]),

    Astronaut('Rick', 'Martinez', missions=[]),
]


# Convert DATA to list[dict], then flatten
# type: list[dict]
data = ...

# Convert `data` to DataFrame
# type: pd.DataFrame
result = ...

# Solution
data = []

for astronaut in DATA:
    astronaut = vars(astronaut)
    missions = [','.join(str(x) for x in vars(mission).values())
                for mission in astronaut.pop('missions')]
    astronaut['missions'] = ';'.join(missions)
    data.append(astronaut)

result = pd.DataFrame(data)


# Alternative Solution
# data = []
# for astronaut in DATA:
#     astronaut = vars(astronaut)
#     missions = astronaut.pop('missions')
#     missions = [vars(x) for x in missions]
#     missions = [','.join(map(str,m.values())) for m in missions]
#     astronaut['missions'] = ';'.join(missions)
#     data.append(astronaut)
# result = pd.DataFrame(data)

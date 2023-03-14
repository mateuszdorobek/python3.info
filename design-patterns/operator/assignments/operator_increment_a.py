"""
* Assignment: Operator Increment Add
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Overload operator `+=`
    2. Make `Astronaut` objects able to add `Missions`, for example:
       a. `mark = Astronaut(firstname='Mark', lastname='Watney')`
       b. `mark += Mission(2035, 'Ares3')`
       c. `mark += Mission(2040, 'Ares5')`
    3. Run doctests - all must succeed

Polish:
    1. Przeciąż operator `+=`
    2. Spraw aby do obiektów klasy `Astronaut` można dodać `Mission`, przykład:
       a. `mark = Astronaut(firstname='Mark', lastname='Watney')`
       b. `mark += Mission(2035, 'Ares3')`
       c. `mark += Mission(2040, 'Ares5')`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `object.__iadd__() -> self`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> astro = Astronaut(firstname='Mark', lastname='Watney', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ... ])
    >>> astro += Mission(2024, 'Artemis 3')
    >>> astro += Mission(2035, 'Ares 3')

    >>> print(astro)  # doctest: +NORMALIZE_WHITESPACE
    Astronaut(firstname='Mark', lastname='Watney',
              missions=[Mission(year=1969, name='Apollo 11'),
                        Mission(year=2024, name='Artemis 3'),
                        Mission(year=2035, name='Ares 3')])
"""

from dataclasses import dataclass


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: list


@dataclass
class Mission:
    year: int
    name: str


# Solution
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __iadd__(self, other):
        self.missions.append(other)
        return self


@dataclass
class Mission:
    year: int
    name: str

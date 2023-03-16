"""
* Assignment: Protocol Iterator Implementation
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Modify classes to implement iterator protocol
    2. Iterator should return instances of `Mission`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasy aby zaimplementować protokół iterator
    2. Iterator powinien zwracać instancje `Mission`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Astronaut)

    >>> astro = Astronaut('Mark', 'Watney')
    >>> assert hasattr(astro, 'firstname')
    >>> assert hasattr(astro, 'lastname')
    >>> assert hasattr(astro, 'missions')
    >>> assert hasattr(astro, '__iter__')
    >>> assert hasattr(astro, '__next__')
    >>> assert ismethod(astro.__iter__)
    >>> assert ismethod(astro.__next__)

    >>> astro = Astronaut('Pan', 'Twardowski', missions=(
    ...     Mission(1969, 'Apollo 11'),
    ...     Mission(2024, 'Artemis 3'),
    ...     Mission(2035, 'Ares 3'),
    ... ))

    >>> for mission in astro:
    ...     print(mission)
    Mission(year=1969, name='Apollo 11')
    Mission(year=2024, name='Artemis 3')
    Mission(year=2035, name='Ares 3')
"""

from dataclasses import dataclass


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()


@dataclass
class Mission:
    year: int
    name: str


# Solution
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.missions):
            raise StopIteration
        result = self.missions[self._iter_index]
        self._iter_index += 1
        return result

"""
* Assignment: Operator Comparison Contains
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Override operators for code to work correctly
    2. Do not use `dataclasses`
    3. Run doctests - all must succeed

Polish:
    1. Nadpisz operatory aby poniższy kod zadziałał poprawnie
    2. Nie używaj `dataclasses`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `object.__contains__()`
    * `object.__eq__()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> astro = Astronaut(firstname='Mark', lastname='Watney', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ...     Mission(2024, 'Artemis 3'),
    ...     Mission(2035, 'Ares 3'),
    ... ])

    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Ares 3')
    True
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Ares 3')
    False

    >>> Mission(2024, 'Artemis 3') in astro
    True
    >>> Mission(1973, 'Apollo 18') in astro
    False
"""


class Mission:
    year: int
    name: str

    def __init__(self, year: int, name: str) -> None:
        self.year = year
        self.name = name


class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __init__(self, firstname: str, lastname: str, missions: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.missions = missions


# Solution
class Mission:
    year: int
    name: str

    def __init__(self, year: int, name: str) -> None:
        self.year = year
        self.name = name

    def __eq__(self, other):
        return (self.year == other.year) \
           and (self.name == other.name)


class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __init__(self, firstname: str, lastname: str, missions: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.missions = missions

    def __contains__(self, flight):
        return flight in self.missions

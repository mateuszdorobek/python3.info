"""
* Assignment: Operator String Nested
* Required: yes
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Overload `str` and `repr` to achieve desired printing output
    2. Run doctests - all must succeed

Polish:
    1. Przeciąż `str` i `repr` aby osiągnąć oczekiwany rezultat wypisywania
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Define `Crew.__str__()`
    * Define `Astronaut.__str__()` and `Astronaut.__repr__()`
    * Define `Mission.__repr__()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> melissa = Astronaut('Melissa Lewis')
    >>> print(f'Commander: \\n{melissa}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Commander:
    Melissa Lewis

    >>> mark = Astronaut('Mark Watney', missions=[
    ...     Mission(2035, 'Ares 3')])
    >>> print(f'Space Pirate: \\n{mark}\\n')  # doctest: +NORMALIZE_WHITESPACE
    Space Pirate:
    Mark Watney veteran of [
          2035: Ares 3]

    >>> crew = Crew([
    ...     Astronaut('Pan Twardowski', missions=[
    ...         Mission(1969, 'Apollo 11'),
    ...         Mission(2024, 'Artemis 3'),
    ...     ]),
    ...     Astronaut('José Jiménez'),
    ...     Astronaut('Mark Watney', missions=[
    ...         Mission(2035, 'Ares 3'),
    ...     ]),
    ... ])

    >>> print(f'Crew: \\n{crew}')  # doctest: +NORMALIZE_WHITESPACE
    Crew:
    Pan Twardowski veteran of [
          1969: Apollo 11,
          2024: Artemis 3]
    José Jiménez
    Mark Watney veteran of [
          2035: Ares 3]
"""


class Crew:
    def __init__(self, members):
        self.members = members


class Astronaut:
    def __init__(self, name, missions=None):
        self.name = name
        self.missions = missions if missions else []


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


# Solution
class Crew:
    def __init__(self, members):
        self.members = members

    def __str__(self):
        return '\n'.join(map(str, self.members))


class Astronaut:
    def __init__(self, name, missions=()):
        self.name = name
        self.missions = missions if missions else []

    def __str__(self):
        if self.missions:
            return f'{self.name} veteran of {self.missions}'
        else:
            return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\t{self.year}: {self.name}'

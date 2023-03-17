"""
* Assignment: DesignPatterns Behavioral Iterator
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Implement Iterator pattern
    2. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Iterator
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> crew = Crew()
    >>> crew += 'Mark Watney'
    >>> crew += 'Jose Jimenez'
    >>> crew += 'Melissa Lewis'
    >>>
    >>> for member in crew:
    ...     print(member)
    Mark Watney
    Jose Jimenez
    Melissa Lewis
"""


class Crew:
    def __init__(self):
        self.members = list()

    def __iadd__(self, other):
        self.members.append(other)
        return self


# Solution
class Crew:
    def __init__(self):
        self.members = list()

    def __iadd__(self, other):
        self.members.append(other)
        return self

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self.members):
            raise StopIteration
        result = self.members[self._current]
        self._current += 1
        return result

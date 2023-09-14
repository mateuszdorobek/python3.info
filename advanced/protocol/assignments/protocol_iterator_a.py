"""
* Assignment: Protocol Iterator Implementation
* Complexity: easy
* Lines of code: 9 lines
* Time: 3 min

English:
    1. Modify classes to implement iterator protocol
    2. Iterator should return instances of `Group`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasy aby zaimplementować protokół iterator
    2. Iterator powinien zwracać instancje `Group`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(User)

    >>> mark = User('Mark', 'Watney')
    >>> assert hasattr(mark, 'firstname')
    >>> assert hasattr(mark, 'lastname')
    >>> assert hasattr(mark, 'groups')
    >>> assert hasattr(mark, '__iter__')
    >>> assert hasattr(mark, '__next__')
    >>> assert ismethod(mark.__iter__)
    >>> assert ismethod(mark.__next__)

    >>> mark = User('Mark', 'Watney', groups=(
    ...     Group(gid=1, name='admins'),
    ...     Group(gid=2, name='staff'),
    ...     Group(gid=3, name='managers'),
    ... ))

    >>> for mission in mark:
    ...     print(mission)
    Group(gid=1, name='admins')
    Group(gid=2, name='staff')
    Group(gid=3, name='managers')
"""

from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    groups: tuple = ()


@dataclass
class Group:
    gid: int
    name: str


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group] | None = None

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.groups):
            raise StopIteration
        result = self.groups[self._iter_index]
        self._iter_index += 1
        return result

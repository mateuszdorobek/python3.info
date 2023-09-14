"""
* Assignment: Operator Comparison Contains
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

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

    >>> mark = User(firstname='Mark', lastname='Watney', groups=[
    ...     Group(gid=1, name='admins'),
    ...     Group(gid=2, name='staff'),
    ...     Group(gid=3, name='managers'),
    ... ])

    >>> Group(gid=1, name='admins') == Group(gid=1, name='admins')
    True
    >>> Group(gid=1, name='admins') == Group(gid=2, name='staff')
    False
    >>> Group(gid=1, name='admins') == Group(gid=3, name='managers')
    False
    >>> Group(gid=1, name='admins') == Group(gid=0, name='root')
    False

    >>> Group(gid=1, name='admins') in mark
    True
    >>> Group(gid=2, name='staff') in mark
    True
    >>> Group(gid=0, name='root') in mark
    False
"""


class Group:
    gid: int
    name: str

    def __init__(self, gid: int, name: str) -> None:
        self.gid = gid
        self.name = name


class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname: str, lastname: str, groups: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups


# Solution
class Group:
    gid: int
    name: str

    def __init__(self, gid: int, name: str) -> None:
        self.gid = gid
        self.name = name

    def __eq__(self, other):
        return (self.gid == other.gid) \
           and (self.name == other.name)


class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname: str, lastname: str, groups: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups

    def __contains__(self, flight):
        return flight in self.groups

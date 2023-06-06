"""
* Assignment: Operator Increment Add
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Overload operator `+=`
    2. Make `User` objects able to add `Groups`, for example:
       a. `mark = User(firstname='Mark', lastname='Watney')`
       b. `mark += Group(1, 'admins')`
       c. `mark += Group(2, 'staff')`
    3. Run doctests - all must succeed

Polish:
    1. Przeciąż operator `+=`
    2. Spraw aby do obiektów klasy `User` można dodać `Group`, przykład:
       a. `mark = User(firstname='Mark', lastname='Watney')`
       b. `mark += Group(1, 'admins')`
       c. `mark += Group(2, 'staff')`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `object.__iadd__() -> self`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> mark = User(firstname='Mark', lastname='Watney', groups=[])
    >>> mark += Group(1, 'admins')
    >>> mark += Group(2, 'staff')

    >>> pprint(mark, width=50)
    User(firstname='Mark',
         lastname='Watney',
         groups=[Group(gid=1, name='admins'),
                 Group(gid=2, name='staff')])
"""

from dataclasses import dataclass


@dataclass
class Group:
    gid: int
    name: str

# Make `User` objects able to add `Groups`, for example:
# a. `mark = User(firstname='Mark', lastname='Watney')`
# b. `mark += Group(1, 'admins')`
# c. `mark += Group(2, 'staff')`
# type: type[User]
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group]


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __iadd__(self, other):
        self.groups.append(other)
        return self

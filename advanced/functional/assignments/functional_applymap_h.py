"""
* Assignment: Functional ApplyMap FlattenClasses
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `Group1_year`, `Group2_year`,
       b. `Group1_name`, `Group2_name`
    2. Note, that enumeration starts with one
    3. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `Group1_year`, `Group2_year`,
       b. `Group1_name`, `Group2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * vars(obj) -> dict

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = list(result)
    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(x) is dict for x in result)

    >>> pprint(result, width=30, sort_dicts=False)
    [{'firstname': 'Mark',
      'lastname': 'Watney',
      'group1_gid': 1,
      'group1_name': 'staff'},
     {'firstname': 'Melissa',
      'lastname': 'Lewis',
      'group1_gid': 1,
      'group1_name': 'staff',
      'group2_gid': 2,
      'group2_name': 'admins'},
     {'firstname': 'Rick',
      'lastname': 'Martinez'}]
"""

class User:
    def __init__(self, firstname, lastname, groups=()):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = list(groups)


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

DATA = [
    User('Mark', 'Watney', groups=[
        Group(gid=1, name='staff')]),

    User('Melissa', 'Lewis', groups=[
        Group(gid=1, name='staff'),
        Group(gid=2, name='admins')]),

    User('Rick', 'Martinez'),
]


# Convert DATA
# type: list[dict]
result = ...


# Solution
def convert(user: User):
    user = vars(user)
    groups = map(vars, user.pop('groups'))
    for i, group in enumerate(groups, start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    return user


result = map(convert, DATA)

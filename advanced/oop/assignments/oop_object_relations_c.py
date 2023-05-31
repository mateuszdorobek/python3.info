"""
* Assignment: OOP ObjectRelations FlattenDicts
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `group1_gid`, `group2_gid`
       b. `group1_name`, `group2_name`
    2. Note, that enumeration starts with one
    3. Collect data to `result: map`
    4. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `group1_gid`, `group2_gid`
       b. `group1_name`, `group2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Zbierz dane do `result: map`
    4. Uruchom doctesty - wszystkie muszą się powieść

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

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "staff"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "staff"},
        {"gid": 2, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": []},
]

# Flatten data, each group field prefixed with group and number
# type: list[dict]
result = ...


# Solution
def convert(user: dict):
    for i, group in enumerate(user.pop('groups'), start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    return user


result = map(convert, DATA)

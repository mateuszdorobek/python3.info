"""
* Assignment: OOP ObjectRelations Nested
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Note, that enumeration starts with one
    3. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = list(result)
    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(x) is dict for x in result)

    >>> pprint(result, width=30)  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Mark',
      'lastname': 'Watney',
      'mission1_name': 'Ares3',
      'mission1_year': 2035},
     {'firstname': 'Melissa',
      'lastname': 'Lewis',
      'mission1_name': 'Ares1',
      'mission1_year': 2030,
      'mission2_name': 'Ares3',
      'mission2_year': 2035},
     {'firstname': 'Rick',
      'lastname': 'Martinez'}]
"""

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "missions": [
        {"name": "Ares3", "year": 2035}]},

    {"firstname": "Melissa", "lastname": "Lewis", "missions": [
        {"name": "Ares1", "year": 2030},
        {"name": "Ares3", "year": 2035}]},

    {"firstname": "Rick", "lastname": "Martinez", "missions": []}
]

# Flatten data, each mission field prefixed with mission and number
# type: list[dict]
result = ...


# Solution
def convert(astronaut: dict):
    for i, mission in enumerate(astronaut.pop('missions'), start=1):
        for field,value in mission.items():
            column_name = f'mission{i}_{field}'
            astronaut[column_name] = value
    return astronaut


result = map(convert, DATA)

"""
* Assignment: CSV Relations Nested
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Note, that enumeration starts with one
    3. Sort `fieldnames`
    4. Save data to `FILE`
    5. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Posortuj `fieldnames`
    4. Zapisz dane do `FILE`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "firstname","group1_gid","group1_name","group2_gid","group2_name","lastname"
    "Mark","1","staff","","","Watney"
    "Melissa","1","staff","2","admins","Lewis"
    "Rick","","","","","Martinez"
    <BLANKLINE>
"""

import csv

FILE = r'_temporary.csv'

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "staff"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "staff"},
        {"gid": 2, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": []},
]

# flatten data, each mission field prefixed with mission and number
# type: list[dict]
result = ...


# Solution
result = []

for user in DATA:
    for i, group in enumerate(user.pop('groups'), start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    result.append(user)

fieldnames = set()
for row in result:
    fieldnames.update(row.keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(fieldnames), quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)

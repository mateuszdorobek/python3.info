"""
* Assignment: Pandas Read PythonDict
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `group1_year`, `group2_year`,
       b. `group1_name`, `group2_name`
    2. Note, that enumeration starts with one
    3. Convert data to `result: pd.DataFrame`
    4. Convert data in `group1_gid` and `group2_gid` to `int`
    5. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `group1_year`, `group2_year`,
       b. `group1_name`, `group2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Przekonwertuj dane do `result: pd.DataFrame`
    4. Przekonwertuj dane w `group1_gid` i `group2_gid` do `int`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * dict.pop()
    * enumerate(..., start=1)
    * column_name = f'group{i}_{field}'

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` has invalid type, should be `pd.DataFrame`'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname  group1_gid group1_name  group2_gid group2_name
    0      Mark    Watney           1       staff        <NA>        <NA>
    1   Melissa     Lewis           1       staff           2      admins
    2      Rick  Martinez        <NA>        <NA>        <NA>        <NA>
"""
import pandas as pd


DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "staff"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "staff"},
        {"gid": 2, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": []},
]


# Define variable data with flatten ``DATA``
# Each group field prefixed with group and number
# type: list[dict]
data = ...

# Convert `data` to DataFrame
# type: pd.DataFrame
result = ...


# Solution
data = []
for user in DATA:
    for i, group in enumerate(user.pop('groups'), start=1):
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    data.append(user)


result = (
    pd
    .DataFrame(data)
    .convert_dtypes()
    .astype({
        'group1_gid': 'int',
        'group2_gid': 'int'
    }, errors='ignore')
)

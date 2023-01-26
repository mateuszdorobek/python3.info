"""
* Assignment: OOP ObjectRelations Nested
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attribute for example:
       a. `address1_street`, `address2_street`,
       b. `address1_city`, `address2_city`
       c. `address1_city`, `address2_city`
    2. Note, that enumeration starts with one
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `address1_street`, `address2_street`,
       b. `address1_city`, `address2_city`
       c. `address1_city`, `address2_city`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(x) is dict for x in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Mark',
      'lastname': 'Watney',
      'address1_street': '2101 E NASA Pkwy',
      'address1_city': 'Houston',
      'address1_post_code': 77058,
      'address1_region': 'Texas',
      'address1_country': 'USA',
      'address2_street': '',
      'address2_city': 'Kennedy Space Center',
      'address2_post_code': 32899,
      'address2_region': 'Florida',
      'address2_country': 'USA'},
     {'firstname': 'Melissa',
      'lastname': 'Lewis',
      'address1_street': '4800 Oak Grove Dr',
      'address1_city': 'Pasadena',
      'address1_post_code': 91109,
      'address1_region': 'California',
      'address1_country': 'USA',
      'address2_street': '2825 E Ave P',
      'address2_city': 'Palmdale',
      'address2_post_code': 93550,
      'address2_region': 'California',
      'address2_country': 'USA'},
     {'firstname': 'Rick',
      'lastname': 'Martinez'},
     {'firstname': 'Alex',
      'lastname': 'Vogel',
      'address1_street': 'Linder Hoehe',
      'address1_city': 'Cologne',
      'address1_post_code': 51147,
      'address1_region': 'North Rhine-Westphalia',
      'address1_country': 'Germany'}]
"""


import json

DATA = """[
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

    {"firstname": "Rick", "lastname": "Martinez", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]"""

# Flatten data, each address field prefixed with address and number
# type: list[dict]
result = ...


# Solution
result: list = []

for astronaut in json.loads(DATA):
    for i, address in enumerate(astronaut.pop('addresses'), start=1):
        for field,value in address.items():
            column_name = f'address{i}_{field}'
            astronaut[column_name] = value
    result.append(astronaut)

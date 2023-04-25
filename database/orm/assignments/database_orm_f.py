"""
* Assignment: OOP ObjectRelations Nested
* Complexity: medium
* Lines of code: 4 lines
* Time: 13 min

English:
    1. Write data with relations to CSV format
    2. Convert `DATA` to `resul: list[dict[str,str]]`
    3. Non-functional requirements:
        a. Use `,` to separate fields
        b. Use `;` to separate instances
    4. Contact has zero or many addresses
    5. Run doctests - all must succeed

Polish:
    1. Zapisz dane relacyjne do formatu CSV
    2. Przekonwertuj `DATA` do `result: list[dict[str,str]]`
    3. Wymagania niefunkcjonalne:
        b. Użyj `,` do oddzielenia pól
        b. Użyj `;` do oddzielenia instancji
    4. Kontakt ma zero lub wiele adresów
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = list(result)
    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(x) is dict for x in result)

    >>> pprint(result, width=112, sort_dicts=False)  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Mark',
      'lastname': 'Watney',
      'addresses': '2101 E NASA Pkwy,Houston,77058,Texas,USA;,Kennedy Space Center,32899,Florida,USA'},
     {'firstname': 'Melissa',
      'lastname': 'Lewis',
      'addresses': '4800 Oak Grove Dr,Pasadena,91109,California,USA;2825 E Ave P,Palmdale,93550,California,USA'},
     {'firstname': 'Rick', 'lastname': 'Martinez', 'addresses': ''},
     {'firstname': 'Alex',
      'lastname': 'Vogel',
      'addresses': 'Linder Hoehe,Cologne,51147,North Rhine-Westphalia,Germany'}]

"""


DATA = [
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "2101 E NASA Pkwy",
         "city": "Houston",
         "postcode": 77058,
         "region": "Texas",
         "country": "USA"},
        {"street": "",
         "city": "Kennedy Space Center",
         "postcode": 32899,
         "region": "Florida",
         "country": "USA"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": [
        {"street": "4800 Oak Grove Dr",
         "city": "Pasadena",
         "postcode": 91109,
         "region": "California",
         "country": "USA"},
        {"street": "2825 E Ave P",
         "city": "Palmdale",
         "postcode": 93550,
         "region": "California",
         "country": "USA"}]},

    {"firstname": "Rick", "lastname": "Martinez", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe",
         "city": "Cologne",
         "postcode": 51147,
         "region": "North Rhine-Westphalia",
         "country": "Germany"}]}
]

# Flatten data, each address field prefixed with address and number
# type: list[dict]
result = ...


# Solution
def convert(astronaut: dict):
    addresses = [','.join(map(str, x.values()))
                 for x in astronaut.pop('addresses')]
    return astronaut | {'addresses': ';'.join(addresses)}

result = map(convert, DATA)

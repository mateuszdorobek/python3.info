"""
* Assignment: OOP Relations Model
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. In `DATA` we have two classes
    2. Model data using classes and relations
    3. Create instances dynamically based on `DATA`
    4. Run doctests - all must succeed

Polish:
    1. W `DATA` mamy dwie klasy
    2. Zamodeluj problem wykorzystując klasy i relacje między nimi
    3. Twórz instancje dynamicznie na podstawie `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list

    >>> assert all(type(astro) is Astronaut
    ...            for astro in result)

    >>> assert all(type(addr) is Address
    ...            for astro in result
    ...            for addr in astro.addresses)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(firstname='José',
               lastname='Jiménez',
               addresses=[Address(street='2101 E NASA Pkwy', city='Houston', postcode=77058, region='Texas', country='USA'),
                          Address(street=None, city='Kennedy Space Center', postcode=32899, region='Florida', country='USA')]),
     Astronaut(firstname='Mark',
               lastname='Watney',
               addresses=[Address(street='4800 Oak Grove Dr', city='Pasadena', postcode=91109, region='California', country='USA'),
                          Address(street='2825 E Ave P', city='Palmdale', postcode=93550, region='California', country='USA')]),
     Astronaut(firstname='Иван',
               lastname='Иванович',
               addresses=[Address(street=None, city='Космодро́м Байкону́р', postcode=None, region='Кызылординская область', country='Қазақстан'),
                          Address(street=None, city='Звёздный городо́к', postcode=141160, region='Московская область', country='Россия')]),
     Astronaut(firstname='Melissa',
               lastname='Lewis',
               addresses=[]),
     Astronaut(firstname='Alex',
               lastname='Vogel',
               addresses=[Address(street='Linder Hoehe', city='Cologne', postcode=51147, region='North Rhine-Westphalia', country='Germany')])]
"""

from dataclasses import dataclass


DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": None, "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": None, "city": "Космодро́м Байкону́р", "postcode": None, "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": None, "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]

class Astronaut:
    ...

class Address:
    ...


# Iterate over `DATA` and create instances
# type: list[Astronaut]
result = ...


# Solution
@dataclass
class Address:
    street: str | None
    city: str
    postcode: int | float | None
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: list[Address] | None


result = []

for row in DATA:
    addresses = [Address(**addr) for addr in row.pop('addresses')]
    astro = Astronaut(**row, addresses=addresses)
    result.append(astro)

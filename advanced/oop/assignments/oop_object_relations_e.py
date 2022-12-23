"""
* Assignment: OOP ObjectRelations Model
* Complexity: easy
* Lines of code: 16 lines
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
    >>> from pprint import pprint

    >>> result = list(result)
    >>> assert type(result) is list
    >>> assert all(type(astro) is Astronaut for astro in result)

    >>> assert all(type(addr) is Address
    ...            for astro in result
    ...            for addr in astro.addresses)

    >>> pprint(result)  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(firstname='Pan',
               lastname='Twardowski',
               addresses=[Address(street='Kamienica Pod św. Janem Kapistranem',
                                  city='Kraków',
                                  postcode=31008,
                                  region='Małopolskie',
                                  country='Poland')]),
     Astronaut(firstname='Mark',
               lastname='Watney',
               addresses=[Address(street='2101 E NASA Pkwy',
                                  city='Houston',
                                  postcode=77058,
                                  region='Texas',
                                  country='USA'),
                          Address(street='',
                                  city='Kennedy Space Center',
                                  postcode=32899,
                                  region='Florida',
                                  country='USA')]),
     Astronaut(firstname='Melissa',
               lastname='Lewis',
               addresses=[Address(street='4800 Oak Grove Dr',
                                  city='Pasadena',
                                  postcode=91109,
                                  region='California',
                                  country='USA'),
                          Address(street='2825 E Ave P',
                                  city='Palmdale',
                                  postcode=93550,
                                  region='California',
                                  country='USA')]),
     Astronaut(firstname='Rick', lastname='Martinez', addresses=[]),
     Astronaut(firstname='Alex',
               lastname='Vogel',
               addresses=[Address(street='Linder Hoehe',
                                  city='Köln',
                                  postcode=51147,
                                  region='North Rhine-Westphalia',
                                  country='Germany')])]
"""

from dataclasses import dataclass


DATA = [
    {"firstname": "Pan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem",
         "city": "Kraków",
         "postcode": 31008,
         "region": "Małopolskie",
         "country": "Poland"}]},

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
         "city": "Köln",
         "postcode": 51147,
         "region": "North Rhine-Westphalia",
         "country": "Germany"}]}
]


@dataclass
class Address:
    ...

@dataclass
class Astronaut:
    ...



# Iterate over `DATA` and create instances
# type: list[Astronaut]
result = ...


# Solution
@dataclass
class Address:
    street: str
    city: str
    postcode: int
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: list[Address | None]


def convert(astronaut: dict) -> Astronaut:
    addresses = map(lambda x: Address(**x), astronaut.pop('addresses'))
    return Astronaut(**astronaut, addresses=list(addresses))

result = map(convert, DATA)

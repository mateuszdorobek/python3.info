"""
* Assignment: Dataclass Field Addressbook
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Model `DATA` using `dataclasses`
    2. Create class definition, fields and their types
    3. Do not write code converting `DATA` to your classes
    4. Run doctests - all must succeed

Polish:
    1. Zamodeluj `DATA` wykorzystując `dataclass`
    2. Stwórz definicję klas, pól i ich typów
    3. Nie pisz kodu konwertującego `DATA` do Twoich klas
    4. Uruchom doctesty - wszystkie muszą się powieść

Non-functional Requirements:
   * Use Python 3.10 syntax for Optionals, ie: `str | None`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass
    >>> from typing import get_type_hints

    >>> assert isclass(Astronaut)
    >>> assert isclass(Address)
    >>> assert is_dataclass(Astronaut)
    >>> assert is_dataclass(Address)

    >>> astronaut = get_type_hints(Astronaut)
    >>> address = get_type_hints(Address)

    >>> assert 'firstname' in astronaut, \
    'Class Astronaut is missing field: firstname'
    >>> assert 'lastname' in astronaut, \
    'Class Astronaut is missing field: lastname'
    >>> assert 'addresses' in astronaut, \
    'Class Astronaut is missing field: addresses'
    >>> assert 'street' in address, \
    'Class Address is missing field: street'
    >>> assert 'city' in address, \
    'Class Address is missing field: city'
    >>> assert 'post_code' in address, \
    'Class Address is missing field: post_code'
    >>> assert 'region' in address, \
    'Class Address is missing field: region'
    >>> assert 'country' in address, \
    'Class Address is missing field: country'
    >>> assert astronaut['firstname'] is str, \
    'Astronaut.firstname has invalid type annotation, expected: str'
    >>> assert astronaut['lastname'] is str, \
    'Astronaut.lastname has invalid type annotation, expected: str'
    >>> assert astronaut['addresses'] == list[Address] | None, \
    'Astronaut.addresses has invalid type annotation, expected: list[Address] | None'
    >>> assert address['street'] == str | None, \
    'Address.street has invalid type annotation, expected: str | None'
    >>> assert address['city'] is str, \
    'Address.city has invalid type annotation, expected: str'
    >>> assert address['post_code'] is int, \
    'Address.post_code has invalid type annotation, expected: int'
    >>> assert address['region'] is str, \
    'Address.region has invalid type annotation, expected: str'
    >>> assert address['country'] is str, \
    'Address.country has invalid type annotation, expected: str'
"""
from dataclasses import dataclass


DATA = [
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058,
         "region": "Texas", "country": "USA"},
        {"street": None, "city": "Kennedy Space Center", "post_code": 32899,
         "region": "Florida", "country": "USA"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109,
         "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550,
         "region": "California", "country": "USA"}]},

    {"firstname": "Rick", "lastname": "Martinez"},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "post_code": 51147,
         "region": "North Rhine-Westphalia", "country": "Germany"}]}
]


# Model `DATA` using `dataclasses`
# Use new optional `str | None` syntax
# type: Type
@dataclass
class Address:
    ...


# Model `DATA` using `dataclasses`
# Use new optional `str | None` syntax
# type: Type
@dataclass
class Astronaut:
    ...


# Solution
@dataclass
class Address:
    street: str | None
    city: str
    post_code: int
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: list[Address] | None

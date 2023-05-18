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

    >>> assert isclass(User)
    >>> assert isclass(Address)
    >>> assert is_dataclass(User)
    >>> assert is_dataclass(Address)

    >>> user = get_type_hints(User)
    >>> address = get_type_hints(Address)

    >>> assert 'firstname' in user, \
    'Class User is missing field: firstname'
    >>> assert 'lastname' in user, \
    'Class User is missing field: lastname'
    >>> assert 'addresses' in user, \
    'Class User is missing field: addresses'
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
    >>> assert user['firstname'] is str, \
    'User.firstname has invalid type annotation, expected: str'
    >>> assert user['lastname'] is str, \
    'User.lastname has invalid type annotation, expected: str'
    >>> assert user['addresses'] == list[Address] | None, \
    'User.addresses has invalid type annotation, expected: list[Address] | None'
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


# Model `DATA` using `dataclass`
# type: type
@dataclass
class Address:
    ...


# Model `DATA` using `dataclass`
# type: type
@dataclass
class User:
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
class User:
    firstname: str
    lastname: str
    addresses: list[Address] | None

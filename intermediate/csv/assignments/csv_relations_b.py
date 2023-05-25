"""
* Assignment: CSV Relations Join
* Complexity: hard
* Lines of code: 11 lines
* Time: 21 min

English:
    1. Using `csv.DictWriter()` save `CREW` to `FILE`
    2. Non-functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate mission fields
        c. Use `;` to separate missions
        d. Use Unix `\n` newline
        e. Sort `fieldnames` using `sorted()`
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz `CREW` do `FILE`
    2. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielania pól mission
        c. Użyj `;` do oddzielenia missions
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj `fieldnames` używając `sorted()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * Nested `for`
    * `str.join(';', sequence)`
    * `str.join(',', sequence)`

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
    "firstname","groups","lastname"
    "Mark","1,users","Watney"
    "Melissa","1,users;2,admins","Lewis"
    "Rick","","Martinez"
    <BLANKLINE>
"""

import csv


class Group:
    gid: int
    name: str

    def __init__(self, gid, name):
        self.gid = gid
        self.name = name


class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = list(groups) if groups else []



DATA = [
    User('Mark', 'Watney', groups=[
        Group(gid=1, name='users')]),
    User('Melissa', 'Lewis', groups=[
        Group(gid=1, name='users'),
        Group(gid=2, name='admins')]),
    User('Rick', 'Martinez', groups=[]),
]

FILE = r'_temporary.csv'


# Using `csv.DictWriter()` save CREW to CSV file
# type: list[dict]
result = ...

# Solution
result = []

for user in DATA:
    user = vars(user)
    groups = [','.join(str(x) for x in vars(group).values())
              for group in user.pop('groups')]
    user['groups'] = ';'.join(groups)
    result.append(user)


fieldnames = sorted(result[0].keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)

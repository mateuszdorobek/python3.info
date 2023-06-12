"""
* Assignment: OOP AttributeSlots Init
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `dump(obj) -> dict` accepting instance with slots
    2. Function should return similar output to `vars()`, i.e.:
       {'username': 'Mark', 'password': 'Ares3', 'email': 'mwatney@nasa.gov'}
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dump(obj) -> dict` przyjmującą instancję ze slotami
    2. Funkcja powinna zwracać podobny wynik do `vars()`, np:
       {'username': 'Mark', 'password': 'Ares3', 'email': 'mwatney@nasa.gov'}
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from dataclasses import is_dataclass

    >>> class User:
    ...     __slots__ = ('username', 'password', 'email')
    ...
    ...     def __init__(self, username, password, email):
    ...         self.username = username
    ...         self.password = password
    ...         self.email = email
    >>>
    >>>
    >>> mark = User(
    ...     username='Mark',
    ...     password='Ares3',
    ...     email='mwatney@nasa.gov')

    >>> result = dump(mark)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Result must be a type'
    >>> assert len(result) == 3, \
    'Result length must be 3'
    >>> assert all(type(x) is str for x in result.keys()), \
    'All keys in result must be a str'
    >>> assert all(type(x) is str for x in result.values()), \
    'All values in result must be a str'

    >>> result
    {'username': 'Mark', 'password': 'Ares3', 'email': 'mwatney@nasa.gov'}
"""

# Define function `dump(obj) -> dict` accepting instance with slots
# Function should return similar output to `vars()`
# type: Callable[[object], dict]
def dump(obj) -> dict:
    ...


# Solution
def dump(obj) -> dict:
    return {attrname: getattr(obj, attrname)
            for attrname in obj.__slots__}

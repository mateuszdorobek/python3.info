"""
* Assignment: OOP AttributeMutability Class list
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create class `User`, with attributes:
        a. `username: str` (required)
        b. `password: str` (required)
        c. `groups: list[str]` (optional)
    2. Attributes must be set at the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `User`, z atrybutami:
        a. `username: str` (wymagane)
        b. `password: str` (wymagane)
        c. `groups: list[str]` (opcjonalne)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu mutowalnych parametrów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> mark = User('mwatney', 'Ares3')
    >>> melissa = User('mlewis', 'Nasa1')
    >>> assert 'username' in vars(mark)
    >>> assert 'password' in vars(mark)
    >>> assert 'groups' in vars(mark)
    >>> assert 'username' in vars(melissa)
    >>> assert 'password' in vars(melissa)
    >>> assert 'groups' in vars(melissa)
    >>> assert mark.groups is not melissa.groups
"""

# Create class `User`, with attributes:
# - `username: str` (required)
# - `password: str` (required)
# - `groups: list[str]` (optional)
# type: type[User]
class User:
    ...


# Solution
class User:
    def __init__(self, username, password, groups=None):
        self.username = username
        self.password = password
        self.groups = groups if groups else []

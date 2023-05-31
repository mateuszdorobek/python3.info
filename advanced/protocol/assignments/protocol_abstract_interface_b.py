"""
* Assignment: OOP AbstractInterface Implement
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Define class `User` implementing `Account`
    2. Implement methods:
        a. `login()` returns 'User logged-in'
        b. `logout()` returns 'User logged-out'
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `User` implementującą `Account`
    2. Zaimplementuj metody:
        a. `login()` zwraca 'User logged-in'
        b. `logout()` zwraca 'User logged-out'
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(self).values()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert issubclass(User, Account)
    >>> assert hasattr(User, '__init__')
    >>> assert hasattr(User, 'login')
    >>> assert hasattr(User, 'logout')

    >>> assert isfunction(User.__init__)
    >>> assert isfunction(User.login)
    >>> assert isfunction(User.logout)

    >>> User.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'username': <class 'str'>,
     'password': <class 'str'>}

    >>> mark = User(username='mwatney', password='Ares3')
    >>> mark.login()
    'User logged-in'
    >>> mark.logout()
    'User logged-out'
"""

class Account:
    username: str
    password: str

    def __init__(self, username: str, password: str):
        raise NotImplementedError

    def login(self):
        raise NotImplementedError

    def logout(self):
        raise NotImplementedError


# Define class `User` implementing `Account`
# Implement methods:
# - `login()` returns 'User logged-in'
# - `logout()` returns 'User logged-out'
class User:
    ...


# Solution
class User(Account):
    username: str
    password: str

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self):
        return 'User logged-in'

    def logout(self):
        return 'User logged-out'

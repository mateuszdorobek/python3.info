"""
* Assignment: OOP AbstractInterface Define
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define interface `Account` with:
        a. Attributes: `username`, `password`
        b. Methods: `__init__()`, `login()`, `logout()`
    2. All methods must raise exception `NotImplementedError`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj interfejs `Account` z:
        a. Atrybuty: `username`, `password`
        b. Metody: `__init__()`, `login()`, `logout()`
    2. Wszystkie metody muszą podnosić wyjątek `NotImplementedError`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert hasattr(Account, '__init__')
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')

    >>> assert isfunction(Account.__init__)
    >>> assert isfunction(Account.login)
    >>> assert isfunction(Account.logout)

    >>> Account.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'username': <class 'str'>,
     'password': <class 'str'>}

    >>> mark = Account(username='mwatney', password='Ares3')
    Traceback (most recent call last):
    NotImplementedError
"""


# Solution
class Account:
    username: str
    password: str

    def __init__(self, username, password) -> None:
        raise NotImplementedError

    def login(self) -> None:
        raise NotImplementedError

    def logout(self) -> None:
        raise NotImplementedError

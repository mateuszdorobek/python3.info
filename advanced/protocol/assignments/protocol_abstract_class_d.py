"""
* Assignment: OOP AbstractClass Implement
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define class `User` implementing `Account`
    2. Overwrite all abstract methods, leave `pass` as content
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` implementującą `Account`
    2. Nadpisz wszystkie metody abstrakcyjne, pozostaw `pass` jako treść
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract, isclass, ismethod, signature

    >>> assert isclass(Account)
    >>> assert isabstract(Account)
    >>> assert hasattr(Account, '__init__')
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')
    >>> assert hasattr(Account.__init__, '__isabstractmethod__')
    >>> assert hasattr(Account.login, '__isabstractmethod__')
    >>> assert hasattr(Account.logout, '__isabstractmethod__')
    >>> assert Account.__init__.__isabstractmethod__ == True
    >>> assert Account.login.__isabstractmethod__ == True
    >>> assert Account.logout.__isabstractmethod__ == True

    >>> Account.__annotations__
    {'username': <class 'str'>, 'password': <class 'str'>}

    >>> Account.__init__.__annotations__
    {'username': <class 'str'>, 'password': <class 'str'>, 'return': None}

    >>> Account.login.__annotations__
    {'return': None}

    >>> Account.logout.__annotations__
    {'return': None}

    >>> assert isclass(User)
    >>> result = User(username='mwatney', password='Ares3')

    >>> result.__annotations__
    {'username': <class 'str'>, 'password': <class 'str'>}

    >>> assert hasattr(result, '__init__')
    >>> assert hasattr(result, 'logout')
    >>> assert hasattr(result, 'login')

    >>> assert ismethod(result.__init__)
    >>> assert ismethod(result.logout)
    >>> assert ismethod(result.login)

    >>> signature(result.__init__)  # doctest: +NORMALIZE_WHITESPACE
    <Signature (username: str, password: str) -> None>
    >>> signature(result.logout)
    <Signature () -> None>
    >>> signature(result.login)
    <Signature () -> None>

    >>> assert vars(result) == {}, 'Do not implement __init__() method'
    >>> assert result.login() is None, 'Do not implement login() method'
    >>> assert result.logout() is None, 'Do not implement logout() method'
"""

from abc import ABC, abstractmethod


class Account(ABC):
    username: str
    password: str

    @abstractmethod
    def __init__(self, username: str, password: str) -> None:
        ...

    @abstractmethod
    def login(self) -> None:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...


# Define class `User` implementing `Account`
# Overwrite all abstract methods, leave `pass` as content
class User:
    ...


# Solution
class User(Account):
    def __init__(self, username: str, password: str) -> None:
        pass

    def login(self) -> None:
        pass

    def logout(self) -> None:
        pass

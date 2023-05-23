"""
* Assignment: OOP AbstractClass Implement
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define class `User` implementing `Account`
    2. All method signatures must be identical to `Account`
    3. Don't implement methods, leave `...` or `pass` as content
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` implementującą `Account`
    2. Sygnatury wszystkich metod muszą być identyczne do `Account`
    3. Nie implementuj metod, pozostaw `...` or `pass` jako zawartość
    4. Uruchom doctesty - wszystkie muszą się powieść

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
    {'firstname': <class 'str'>, 'lastname': <class 'str'>}

    >>> Account.__init__.__annotations__
    {'firstname': <class 'str'>, 'lastname': <class 'str'>, 'return': None}

    >>> Account.login.__annotations__
    {'return': None}

    >>> Account.logout.__annotations__
    {'return': None}

    >>> assert isclass(User)
    >>> result = User(firstname='Mark', lastname='Watney')

    >>> result.__annotations__
    {'firstname': <class 'str'>, 'lastname': <class 'str'>}

    >>> assert hasattr(result, '__init__')
    >>> assert hasattr(result, 'logout')
    >>> assert hasattr(result, 'login')

    >>> assert ismethod(result.__init__)
    >>> assert ismethod(result.logout)
    >>> assert ismethod(result.login)

    >>> signature(result.__init__)  # doctest: +NORMALIZE_WHITESPACE
    <Signature (firstname: str, lastname: str) -> None>
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
    firstname: str
    lastname: str

    @abstractmethod
    def __init__(self, firstname: str, lastname: str) -> None:
        ...

    @abstractmethod
    def login(self) -> None:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...


# Define class `User` implementing `Account`
# Don't implement methods, leave `...` or `pass` as content


# Solution
class User(Account):
    def __init__(self, firstname: str, lastname: str) -> None:
        ...

    def login(self) -> None:
        ...

    def logout(self) -> None:
        ...

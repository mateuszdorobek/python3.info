"""
* Assignment: OOP AbstractClass Implementation
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Create class `User` inheriting from `Account`
    2. Overwrite all abstract methods, leave `pass` as content
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `User` dziedziczące po `Account`
    2. Nadpisz wszystkie metody abstrakcyjne, pozostaw `pass` jako treść
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, isabstract, ismethod

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isabstract(Account)
    >>> assert not isabstract(User)
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')
    >>> assert hasattr(User, 'login')
    >>> assert hasattr(User, 'logout')
    >>> assert not hasattr(User.login, '__isabstractmethod__')
    >>> assert not hasattr(User.logout, '__isabstractmethod__')
    >>> assert hasattr(Account.login, '__isabstractmethod__')
    >>> assert hasattr(Account.logout, '__isabstractmethod__')
    >>> assert Account.login.__isabstractmethod__ == True
    >>> assert Account.logout.__isabstractmethod__ == True

    >>> result = Account()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Account with abstract methods login, logout
    >>> result = User()
    >>> assert ismethod(result.login)
"""
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


# Create class `User` inheriting from `Account`
# Overwrite all abstract methods, leave `pass` as content
class User:
    ...


# Solution
class User(Account):
    def login(self):
        pass

    def logout(self):
        pass

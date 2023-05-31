"""
* Assignment: OOP AbstractClass Syntax
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Create abstract class `Account`
    2. Define abstract methods `login()` and `logout()`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę abstrakcyjną `Account`
    2. Zdefiniuj metody abstrakcyjne `login()` i `logout()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, isabstract, ismethod

    >>> assert isclass(Account)
    >>> assert isabstract(Account)
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')
    >>> assert hasattr(Account.login, '__isabstractmethod__')
    >>> assert hasattr(Account.logout, '__isabstractmethod__')
    >>> assert Account.login.__isabstractmethod__ == True
    >>> assert Account.logout.__isabstractmethod__ == True

    >>> result = Account()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Account with abstract methods login, logout
"""

# Define abstract class `Account`
# With abstract methods `login()` and `logout()`
class Account:
    pass


# Solution
from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

"""
* Assignment: OOP AbstractClass Syntax
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Create abstract class `Account` with abstract method `login()`
    2. Create class `User` inheriting from `Account`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę abstrakcyjną `Account` z metodą abstrakcyjną `login()`
    2. Stwórz klasę `User` dziedziczące po `Account`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, isabstract, ismethod

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isabstract(Account)
    >>> assert not isabstract(User)
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(User, 'login')
    >>> assert not hasattr(User.login, '__isabstractmethod__')
    >>> assert hasattr(Account.login, '__isabstractmethod__')
    >>> assert Account.login.__isabstractmethod__ == True

    >>> result = Account()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Account with abstract method login
    >>> result = User()
    >>> assert ismethod(result.login)

Warning:
    * Last line of doctest, second to last word of `TypeError` message
    * In Python 3.7, 3.8 there is "methods" word in doctest
    * In Python 3.9, 3.10, 3.11 there is "method" word in doctest
    * So it differs by "s" at the end of "method" word
"""

# Solution
from abc import ABC, abstractmethod


# Abstract class `Account` with abstract method `login()`
# Create class `User` inheriting from `Account`
class Account(ABC):
    @abstractmethod
    def login(self):
        pass


class User(Account):
    def login(self):
        pass

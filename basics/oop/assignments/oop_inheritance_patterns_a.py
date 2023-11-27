"""
* Assignment: OOP InheritancePatterns Simple
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create class `Account`
    2. Create class `User` which inherits from `Account`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Account`
    2. Stwórz klasę `User`, która dziedziczy po `Account`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert issubclass(User, Account)
"""


# Solution
class Account:
    pass


class User(Account):
    pass

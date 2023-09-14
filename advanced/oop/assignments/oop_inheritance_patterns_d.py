"""
* Assignment: OOP InheritancePatterns Multiple
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create class `MyAccount` from classes `Account`, `User`, `Admin`
    2. Use mixins classes
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `MyAccount` z klas `Account`, `User`, `Admin`
    2. Użyj klas domieszkowych (mixin)
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert isclass(MyAccount)
    >>> assert issubclass(MyAccount, Account)
    >>> assert issubclass(MyAccount, User)
    >>> assert issubclass(MyAccount, Admin)

    >>> assert len(Account.__subclasses__()) == 1
    >>> assert len(User.__subclasses__()) == 1
    >>> assert len(Admin.__subclasses__()) == 1
    >>> assert len(MyAccount.__subclasses__()) == 0
"""

# Create classes `MyAccount`, `Account`, `User`,  `Admin`
# Use mixins classes, do not define attributes
class Account:
    pass


class User:
    pass


class Admin:
    pass


class MyAccount:
    pass


# Solution
class Account:
    pass


class User:
    pass


class Admin:
    pass


class MyAccount(Account, User, Admin):
    pass

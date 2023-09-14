"""
* Assignment: OOP InheritancePatterns Composition
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define class `MyAccount` with attribute `type: Account`
    2. Use composition
    3. Allow for setting type `User` or `Admin` in `__init__()` method
    4. Assignment demonstrates syntax
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `MyAccount` z atrybutem `type: Account`
    2. Użyj kompozycji
    3. Pozwól na ustawianie typu `User` or `Admin` w metodzie `__init__()`
    4. Zadanie demonstruje składnię
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert isclass(Account)
    >>> assert isclass(MyAccount)

    >>> result = MyAccount()
    >>> assert hasattr(result, 'type')

    >>> result = MyAccount()
    >>> assert hasattr(result, 'type')
    >>> assert not isclass(result.type)
    >>> assert isinstance(result.type, Account)
    >>> assert not isinstance(result.type, User)
    >>> assert not isinstance(result.type, Admin)

    >>> result = MyAccount(type=Account)
    >>> assert hasattr(result, 'type')
    >>> assert not isclass(result.type)
    >>> assert isinstance(result.type, Account)
    >>> assert not isinstance(result.type, User)
    >>> assert not isinstance(result.type, Admin)

    >>> result = MyAccount(type=User)
    >>> assert hasattr(result, 'type')
    >>> assert not isclass(result.type)
    >>> assert isinstance(result.type, Account)
    >>> assert isinstance(result.type, User)
    >>> assert not isinstance(result.type, Admin)

    >>> result = MyAccount(type=Admin)
    >>> assert hasattr(result, 'type')
    >>> assert not isclass(result.type)
    >>> assert isinstance(result.type, Account)
    >>> assert not isinstance(result.type, User)
    >>> assert isinstance(result.type, Admin)
"""

class Account:
    pass


class User(Account):
    pass


class Admin(Account):
    pass


# Use composition
# Define class `MyAccount` with attribute `type: Account`
# Allow for setting type `User` or `Admin` in `__init__()` method
class MyAccount:
    pass



# Solution
class Account:
    pass


class User(Account):
    pass


class Admin(Account):
    pass


class MyAccount:
    type: Account

    def __init__(self, type: Account = Account):
        self.type = type()

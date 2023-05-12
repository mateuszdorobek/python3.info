"""
* Assignment: OOP InheritancePatterns Composition
* Complexity: easy
* Lines of code: 10 lines
* Time: 3 min

English:
    1. Create class `MyAccount` from classes `Account`, `User`, `Admin`
    2. Use composition
    3. Assignment demonstrates syntax, so do not add any attributes and methods (only type annotations)
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `MyAccount` z klas `Account`, `User`, `Admin`
    2. Użyj kompozycji
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod (tylko anotacje typów)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert isclass(Account)
    >>> assert isclass(MyAccount)
    >>> assert hasattr(MyAccount, 'account')
    >>> assert hasattr(MyAccount, 'user')
    >>> assert hasattr(MyAccount, 'admin')
    >>> assert isinstance(MyAccount.account, Account)
    >>> assert isinstance(MyAccount.user, User)
    >>> assert isinstance(MyAccount.admin, Admin)
"""


# Solution
class Account:
    pass


class User:
    pass


class Admin:
    pass


class MyAccount:
    account = Account()
    user = User()
    admin = Admin()

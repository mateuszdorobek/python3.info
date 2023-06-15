"""
* Assignment: OOP InheritancePatterns Composition
* Complexity: easy
* Lines of code: 10 lines
* Time: 3 min

English:
    1. Define class `MyAccount` from classes `Account`, `User`, `Admin`
    2. Use composition
    3. Initialize attributes in `__init__()` method
    4. Assignment demonstrates syntax
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `MyAccount` z klas `Account`, `User`, `Admin`
    2. Użyj kompozycji
    3. Zainicjalizuj atrybuty w metodzie `__init__()`
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
    >>> assert hasattr(result, 'account')
    >>> assert hasattr(result, 'user')
    >>> assert hasattr(result, 'admin')
    >>> assert isinstance(result.account, Account)
    >>> assert isinstance(result.user, User)
    >>> assert isinstance(result.admin, Admin)

    >>> result = MyAccount(account=Account())
    >>> assert isinstance(result.account, Account)
    >>> assert isinstance(result.user, User)
    >>> assert isinstance(result.admin, Admin)

    >>> result = MyAccount(user=User())
    >>> assert isinstance(result.account, Account)
    >>> assert isinstance(result.user, User)
    >>> assert isinstance(result.admin, Admin)

    >>> result = MyAccount(admin=Admin())
    >>> assert isinstance(result.account, Account)
    >>> assert isinstance(result.user, User)
    >>> assert isinstance(result.admin, Admin)

    >>> result = MyAccount(account=Account(), user=User(), admin=Admin())
    >>> assert isinstance(result.account, Account)
    >>> assert isinstance(result.user, User)
    >>> assert isinstance(result.admin, Admin)
"""

# Create classes `MyAccount`, `Account`, `User`,  `Admin`
# Use composition
# Initialize attributes in `__init__()` method
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


class MyAccount:
    account: Account
    user: User
    admin: Admin

    def __init__(self, account=Account(), user=User(), admin=Admin()):
        self.account = account
        self.user = user
        self.admin = admin

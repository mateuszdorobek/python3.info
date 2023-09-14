"""
* Assignment: OOP InheritancePatterns SingleInheritance
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Create class `Account`
    2. Create class `User` which inherits from `Account`
    3. Create class `Admin` which inherits from `Account`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Account`
    2. Stwórz klasę `User`, która dziedziczy po `Account`
    3. Stwórz klasę `Admin`, która dziedziczy po `Account`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert issubclass(User, Account)
    >>> assert issubclass(Admin, Account)
    >>> assert not issubclass(User, Admin)
    >>> assert not issubclass(Admin, User)
"""

# Create class `Account`
# type: type[Account]
class Account:
    pass

# Create class `User` which inherits from `Account`
# type: type[Account]
class User:
    pass

# Create class `Admin` which inherits from `Account`
# type: type[Account]
class Admin:
    pass


# Solution
class Account:
    pass


class User(Account):
    pass


class Admin(Account):
    pass

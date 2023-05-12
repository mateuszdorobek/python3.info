"""
* Assignment: OOP InheritancePatterns NoInheritance
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Create classes `MyAccount`, `Account`, `User`,  `Admin`
    2. Do not use inheritance
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasy `MyAccount`, `Account`, `User`,  `Admin`
    2. Nie używaj dziedziczenia
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert isclass(MyAccount)
"""


# Solution
class Account:
    pass


class User:
    pass


class Admin:
    pass


class MyAccount:
    pass

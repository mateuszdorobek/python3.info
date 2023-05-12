"""
* Assignment: OOP AttributeAccessModifiers Init
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Modify dataclass `User` to add attributes:
        a. Public: `firstname`, `lastname`
        b. Protected: `email`, `phone`
        c. Private: `username`, `password`
    2. Do not use `dataclass`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dataclass `User` aby dodać atrybuty:
        a. Publiczne: `firstname`, `lastname`
        b. Chronione: `email`, `phone`
        c. Prywatne: `username`, `password`
    2. Nie używaj `dataclass`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)

    >>> result = User(
    ...     firstname='Mark',
    ...     lastname='Watney',
    ...     email='mwatney@nasa.gov',
    ...     phone='+1 234 567 8910',
    ...     username='mwatney',
    ...     password='Ares3',
    ... )

    >>> assert hasattr(result, 'firstname')
    >>> assert hasattr(result, 'lastname')
    >>> assert hasattr(result, '_email')
    >>> assert hasattr(result, '_phone')
    >>> assert hasattr(result, '_User__username')
    >>> assert hasattr(result, '_User__password')
"""

# Public attributes: `firstname`, `lastname`
# Protected attributes: `email`, `phone`
# Private attributes: `username`, `password`
# type: type[User]
class User:
    pass


# Solution
class User:
    def __init__(self, firstname, lastname, email, phone, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self._email = email
        self._phone = phone
        self.__username = username
        self.__password = password

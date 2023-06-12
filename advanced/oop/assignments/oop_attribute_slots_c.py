"""
* Assignment: OOP AttributeSlots Init
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define class `User` with slots:
       a. `username: str`
       b. `password: str`
       c. `email: str`
    2. Define `__init__()` method
    3. Add type annotation for attributes
    4. Do not use dataclass
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` z slotami:
       a. `username: str`
       b. `password: str`
       c. `email: str`
    2. Zdefiniuj metodę `__init__()`
    3. Dodaj type annotation dla atrybutów
    4. Nie używaj dataclass
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from dataclasses import is_dataclass

    >>> assert hasattr(User, '__slots__')
    >>> assert 'username' in User.__slots__
    >>> assert 'password' in User.__slots__
    >>> assert 'email' in User.__slots__

    >>> assert User is not Ellipsis, \
    'Assign result to variable: `User`'
    >>> assert type(User) is type, \
    'Result must be a type'
    >>> assert not is_dataclass(User), \
    'Class User cannot be dataclass'

    >>> result = User(
    ...     username='Mark',
    ...     password='Ares3',
    ...     email='mwatney@nasa.gov')

    >>> assert not hasattr(result, '__dict__')
    >>> assert not hasattr(result, '__weakref__')

    >>> assert 'username' in result.__annotations__
    >>> assert 'password' in result.__annotations__
    >>> assert 'email' in result.__annotations__
"""

# Define class `User` with slots:
# - `username: str`
# - `password: str`
# - `email: str`
# Define `__init__()` method
# Add type annotation for attributes
# type: type[User]
class User:
    __slots__ = ('username', 'password', 'email')


# Solution
class User:
    __slots__ = ('username', 'password', 'email')
    username: str
    password: str
    email: str

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

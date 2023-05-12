"""
* Assignment: OOP AttributeSlots Define
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define class `User` with attributes:
       'firstname', 'lastname', 'email', 'phone'
    2. All attributes must be in `__slots__`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` z atrybutami:
       'firstname', 'lastname', 'email', 'phone'
    2. Wszystkie atrybuty muszą być w `__slots__`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert hasattr(User, '__slots__')
    >>> assert 'firstname' in User.__slots__
    >>> assert 'lastname' in User.__slots__
    >>> assert 'email' in User.__slots__
    >>> assert 'phone' in User.__slots__

    >>> result = User()
    >>> assert not hasattr(result, '__dict__')
    >>> assert not hasattr(result, '__weakref__')
"""

class User:
    ...


# Solution
class User:
    __slots__ = ('firstname', 'lastname', 'email', 'phone')

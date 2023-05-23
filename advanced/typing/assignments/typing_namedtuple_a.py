"""
* Assignment: Typing Annotations NamedTuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Declare proper types for variables
    2. Use `NamedTuple`
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj `NamedTuple`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data == User('Mark', 'Watney', 42), \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare proper types for variables
class User:
    ...

# Do not modify lines below
data: User = ('Mark', 'Watney', 42)

# Solution
from typing import NamedTuple

class User(NamedTuple):
    firstname: str
    lastname: str
    age: 42

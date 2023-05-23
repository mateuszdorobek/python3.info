"""
* Assignment: Typing Annotations Mapping
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Use `TypedDict`
    3. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Użyj `TypedDict`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data == {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}, \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare proper types for variables
class User:
    ...

# Do not modify lines below
data: User = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

# Solution
from typing import TypedDict

class User(TypedDict):
    firstname: str
    lastname: str
    age: int

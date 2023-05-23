"""
* Assignment: Typing Annotations Mapping
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == {}, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == {'firstname': 'Mark', 'lastname': 'Watney'}, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}, \
    'Do not modify variable `c` value, just add type annotation'
"""

# Declare proper types for variables
a: ...
b: ...
c: ...

# Do not modify lines below
a = {}
b = {'firstname': 'Mark', 'lastname': 'Watney'}
c = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

# Solution
a: dict = {}
b: dict[str,str] = {'firstname': 'Mark', 'lastname': 'Watney'}
c: dict[str,str|int] = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

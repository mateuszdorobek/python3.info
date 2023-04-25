"""
* Assignment: Typing Annotations List of Tuple
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `a` with value {}
       b. Variable `b` with value {'firstname': 'Mark', 'lastname': 'Watney'}
       c. Variable `c` with value {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `a` z wartością {}
       b. Zmienna `b` z wartością {'firstname': 'Mark', 'lastname': 'Watney'}
       c. Zmienna `c` z wartością {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
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


# add proper type annotation for following values
a = {}

# add proper type annotation for following values
b = {'firstname': 'Mark', 'lastname': 'Watney'}

# add proper type annotation for following values
c = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}


# Solution
a: set = {}
b: dict[str,str] = {'firstname': 'Mark', 'lastname': 'Watney'}
c: dict[str,str|int] = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

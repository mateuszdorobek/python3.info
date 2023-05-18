"""
* Assignment: Typing Basic Logic
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variables:
       a. Variable `a` with value True
       b. Variable `b` with value False
       c. Variable `c` with value None
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj zmienne z odpowiednim typem:
       a. Zmienna `a` z wartością True
       b. Zmienna `b` z wartością False
       c. Zmienna `c` z wartością None
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a == True, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == False, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == None, \
    'Do not modify variable `c` value, just add type annotation'

"""


# add proper type annotation for following values
a = True

# add proper type annotation for following values
b = False

# add proper type annotation for following values
c = None


# Solution
a: bool = True
b: bool = False
c: None = None

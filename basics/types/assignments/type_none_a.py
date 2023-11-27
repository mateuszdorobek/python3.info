"""
* Assignment: Type None
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. What you need to put in expressions to get the expected outcome?
    2. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert type(a) is type(None), \
    'Variable `a` has invalid type, should be NoneType'
    >>> assert type(b) is type(None), \
    'Variable `b` has invalid type, should be NoneType'
    >>> assert type(c) is type(None), \
    'Variable `c` has invalid type, should be NoneType'

    >>> a is None
    True
    >>> b is not None
    False
    >>> bool(c) is not bool(c) == False
    False
"""

# Result of `... is None` must be True
# type: bool
a = ...

# Result of `... is not None` must be False
# type: bool
b = ...

# Result of `bool(...) is not bool(...) == False` must be True
# type: bool
c = ...


# Solution
a = None
b = None
c = None

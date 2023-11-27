"""
* Assignment: Type Bool True or False
* Type: class assignment
* Complexity: easy
* Lines of code: 14 lines
* Time: 8 min

English:
    1. What you need to put in expressions to get the expected outcome?
    2. In place of ellipsis (`...`) insert only `True` or `False`
    3. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. W miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, 'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, 'Assign your result to variable `c`'
    >>> assert d is not Ellipsis, 'Assign your result to variable `d`'
    >>> assert e is not Ellipsis, 'Assign your result to variable `e`'
    >>> assert f is not Ellipsis, 'Assign your result to variable `f`'
    >>> assert g is not Ellipsis, 'Assign your result to variable `g`'
    >>> assert h is not Ellipsis, 'Assign your result to variable `h`'
    >>> assert i is not Ellipsis, 'Assign your result to variable `i`'
    >>> assert j is not Ellipsis, 'Assign your result to variable `j`'
    >>> assert k is not Ellipsis, 'Assign your result to variable `k`'
    >>> assert l is not Ellipsis, 'Assign your result to variable `l`'
    >>> assert m is not Ellipsis, 'Assign your result to variable `m`'
    >>> assert n is not Ellipsis, 'Assign your result to variable `n`'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'
    >>> assert type(j) is bool, 'Variable `j` has invalid type, should be bool'
    >>> assert type(k) is bool, 'Variable `k` has invalid type, should be bool'
    >>> assert type(l) is bool, 'Variable `l` has invalid type, should be bool'
    >>> assert type(m) is bool, 'Variable `m` has invalid type, should be bool'
    >>> assert type(n) is bool, 'Variable `n` has invalid type, should be bool'

    >>> a
    True
    >>> b
    False
    >>> c
    True
    >>> d
    False
    >>> e
    True
    >>> f
    False
    >>> g
    True
    >>> h
    False
    >>> i
    True
    >>> j
    True
    >>> k
    False
    >>> l
    False
    >>> m
    True
    >>> n
    False
"""

# Result of bool(True)
# type: bool
example = True

# Result of bool(True)
# type: bool
a = ...

# Result of bool(False)
# type: bool
b = ...

# Result of bool(1)
# type: bool
c = ...

# Result of bool(0)
# type: bool
d = ...

# Result of bool(-1)
# type: bool
e = ...

# Result of bool(0.0)
# type: bool
f = ...

# Result of bool('a')
# type: bool
g = ...

# Result of bool('')
# type: bool
h = ...

# Result of bool(' ')
# type: bool
i = ...

# Result of bool('0')
# type: bool
j = ...

# Result of bool(int('0'))
# type: bool
k = ...

# Result of bool(-0.0+0.0j)
# type: bool
l = ...

# Result of bool('-0.0+0.0j')
# type: bool
m = ...

# Result of bool(complex('-0.0+0.0j'))
# type: bool
n = ...

# Solution
a = True
b = False
c = True
d = False
e = True
f = False
g = True
h = False
i = True
j = True
k = False
l = False
m = True
n = False

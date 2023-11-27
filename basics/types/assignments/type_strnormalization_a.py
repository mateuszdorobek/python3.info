"""
* Assignment: String Normalization Address
* Type: class assignment
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Expected value is `Pana Twardowskiego III`
    2. Use only `str` methods to clean each variable
    3. Discuss how to create generic solution which fit all cases
    4. Implementation of such generic function will be in
       `Function Arguments Clean` chapter
    5. Run doctests - all must succeed

Polish:
    1. Oczekiwana wartość `Pana Twardowskiego III`
    2. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    3. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące
       do wszystkich przypadków
    4. Implementacja takiej generycznej funkcji będzie w rozdziale
       `Function Arguments Clean`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert example is not Ellipsis, \
    'Assign your result to variable `example`'
    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert d is not Ellipsis, \
    'Assign your result to variable `d`'
    >>> assert e is not Ellipsis, \
    'Assign your result to variable `e`'
    >>> assert f is not Ellipsis, \
    'Assign your result to variable `f`'
    >>> assert g is not Ellipsis, \
    'Assign your result to variable `g`'
    >>> assert h is not Ellipsis, \
    'Assign your result to variable `h`'
    >>> assert i is not Ellipsis, \
    'Assign your result to variable `i`'
    >>> assert type(example) is str, \
    'Variable `example` has invalid type, should be str'
    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, \
    'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, \
    'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, \
    'Variable `g` has invalid type, should be str'
    >>> assert type(h) is str, \
    'Variable `h` has invalid type, should be str'
    >>> assert type(i) is str, \
    'Variable `i` has invalid type, should be str'

    >>> example
    'Pana Twardowskiego III'
    >>> a
    'Pana Twardowskiego III'
    >>> b
    'Pana Twardowskiego III'
    >>> c
    'Pana Twardowskiego III'
    >>> d
    'Pana Twardowskiego III'
    >>> e
    'Pana Twardowskiego III'
    >>> f
    'Pana Twardowskiego III'
    >>> g
    'Pana Twardowskiego III'
    >>> h
    'Pana Twardowskiego III'
    >>> i
    'Pana Twardowskiego III'
"""

EXAMPLE = 'UL. Pana \tTWArdoWskIEGO 3'
A = 'ul Pana TwaRDOWSkiego III'
B = '\tul. Pana Twardowskiego trzeciego'
C = 'ulicaPana Twardowskiego III'
D = 'Pana \nTWARDOWSKIEGO 3'
E = 'UL. Pana TWARDowsKIEGO III'
F = 'ULICA Pana TWARDOWSKIEGO III '
G = 'ULICA. Pana TWARDowsKIEGO III'
H = ' Pana Twardowskiego 3 '
I = 'Pana\tTwardowskiego III '

example = EXAMPLE.upper().replace('UL. ', '').replace('\t', '') \
    .strip().title().replace('3', 'III')

# Expected result: 'Pana Twardowskiego III'
# type: str
a = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
b = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
c = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
d = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
e = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
f = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
g = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
h = ...

# Expected result: 'Pana Twardowskiego III'
# type: str
i = ...

# Solution
a = A.upper().replace('UL', '').strip().title().replace('Iii', 'III')
b = B.upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
c = C.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
d = D.upper().replace('\n', '').strip().title().replace('3', 'III')
e = E.upper().replace('UL.', '').strip().title().replace('Iii', 'III')
f = F.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
g = G.upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
h = H.upper().replace('3', 'III').strip().title().replace('Iii', 'III')
i = I.upper().replace('\t', ' ').strip().title().replace('Iii', 'III')

"""
* Assignment: Type Int Bits
* Required: no
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. File size is 1337 megabits [Mb]
    2. Calculate size in bits [b]
    3. Calculate size in kilobits [kb]
    4. In Calculations use floordiv (`//`)
    5. Run doctests - all must succeed

Polish:
    1. Wielkość pliku to 1337 megabits [Mb]
    2. Oblicz wielkość w bitach [b]
    3. Oblicz wielkość w kilobitach [kb]
    4. W obliczeniach użyj floordiv (`//`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 kb = 1024 b
    * 1 Mb = 1024 Kb
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert size_bits is not Ellipsis, \
    'Assign your result to variable `size_bits`'
    >>> assert size_kilobits is not Ellipsis, \
    'Assign your result to variable `size_kilobits`'
    >>> assert size_megabits is not Ellipsis, \
    'Assign your result to variable `size_megabits`'
    >>> assert type(size_bits) is int, \
    'Variable `size_bits` has invalid type, should be int'
    >>> assert type(size_kilobits) is int, \
    'Variable `size_kilobits` has invalid type, should be int'
    >>> assert type(size_megabits) is int, \
    'Variable `size_megabits` has invalid type, should be int'

    >>> assert size_bits == 1_401_946_112, \
    'Invalid value for `size_bits`. Check you calculation'
    >>> assert size_kilobits == 1_369_088, \
    'Invalid value for `size_kilobits`. Check you calculation'
    >>> assert size_megabits == 1337, \
    'Invalid value for `size_megabits`. Check you calculation'
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

SIZE = 1337 * Mb

# SIZE in bits
# type: int
size_bits = ...

# SIZE in kilobits
# type: int
size_kilobits = ...

# SIZE in megabits
# type: int
size_megabits = ...

# Solution
size_bits = SIZE // b
size_kilobits = SIZE // kb
size_megabits = SIZE // Mb

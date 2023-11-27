"""
* Assignment: Type Int Bytes
* Type: homework
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. File size is 100 megabytes
    2. Calculate size in kilobytes
    2. Calculate size in megabits
    3. Run doctests - all must succeed

Polish:
    1. Wielkość pliku to 100 megabajtów
    2. Oblicz wielkość w kilobajtach
    2. Oblicz wielkość w megabitach
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB
    * Use // to get floor division as int

Tests:
    >>> import sys; sys.tracebacklimit = 0


    >>> assert size_kilobytes is not Ellipsis, \
    'Assign your result to variable `size_kilobytes`'
    >>> assert size_megabits is not Ellipsis, \
    'Assign your result to variable `size_megabits`'
    >>> assert type(size_kilobytes) is int, \
    'Variable `size_kilobytes` has invalid type, should be int'
    >>> assert type(size_megabits) is int, \
    'Variable `size_megabits` has invalid type, should be int'

    >>> assert size_kilobytes == 102_400, \
    'Invalid value for `size_kilobytes`. Check you calculation'
    >>> assert size_megabits == 800, \
    'Invalid value for `size_megabits`. Check you calculation'
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

SIZE = 100 * MB

# SIZE in kilobytes
# type: int
size_kilobytes = ...

# SIZE in megabits
# type: int
size_megabits = ...

# Solution
size_kilobytes = SIZE // kB
size_megabits = SIZE // Mb

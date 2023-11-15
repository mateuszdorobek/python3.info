"""
* Assignment: Idiom Filter Apply
* Required: yes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Filter-out lines from `DATA` when:
        a. line is empty
        b. line has only spaces
        c. starts with # (comment)
    2. Use `filter()` to apply function `valid()` to DATA
    3. Define `result: filter` with result
    4. Run doctests - all must succeed

Polish:
    1. Odfiltruj linie z `DATA` gdy:
        a. linia jest pusta
        b. linia ma tylko spacje
        c. zaczyna się od # (komentarz)
    2. Użyj `filter()` aby zaaplikować funkcję `valid()` do DATA
    3. Zdefiniuj `result: filter` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * filter()
    * str.splitlines()
    * str.startswith()
    * len()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(valid), \
    'Object `valid` must be a function'

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is filter, \
    'Variable `result` has invalid type, should be filter'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    ['127.0.0.1       localhost',
     '127.0.0.1       astromatt',
     '10.13.37.1      nasa.gov esa.int',
     '255.255.255.255 broadcasthost',
     '::1             localhost']
"""

DATA = """##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

# Filter-out lines from `DATA` when:
# - line is empty
# - line has only spaces
# - starts with # (comment)
# type: Callable[[str], bool]
def valid(line):
    ...

# Use `filter()` to apply function `valid()` to DATA
# type: filter
result = ...

# Solution
def valid(line: str) -> bool:
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


result = filter(valid, DATA.splitlines())

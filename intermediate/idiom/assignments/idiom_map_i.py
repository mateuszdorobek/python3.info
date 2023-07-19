"""
* Assignment: Idiom Filter Apply
* Required: yes
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

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

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(parse), \
    'Object `parse` must be a function'

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hosts': ['localhost']},
     {'ip': '127.0.0.1', 'hosts': ['astromatt']},
     {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
     {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
     {'ip': '::1', 'hosts': ['localhost']}]
"""

DATA = """127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

def parse(line):
    ...

result = ...

# Solution
def parse(line):
    ip, *hosts = line.split()
    return {'ip':ip, 'hosts':hosts}


result = map(parse, DATA.splitlines())

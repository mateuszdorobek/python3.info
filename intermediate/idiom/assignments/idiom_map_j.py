"""
* Assignment: Idiom Map Parse
* Type: class assignment
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Use `map()` to apply function `convert()` to DATA
    2. Function `convert()`:
        a. Takes string
        b. Splits string
        c. Returns `dict` with `ip` and `hosts` as keys, example:
           {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
    2. Define `result: map` with result
    3. Run doctests - all must succeed

Polish:
    1. Użyj `map()` aby zaaplikować funkcję `convert()` do DATA
    2. Funkcja `convert()`:
        a. Przyjmuje stringa
        b. Dzieli stringa
        c. Zwraca `dict` z `ip` i `hosts` jako klucze, przykład:
           {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
    2. Zdefiniuj `result: map` z wynikiem
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * map()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(convert), \
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

def convert(line):
    ...

result = ...

# Solution
def convert(line):
    ip, *hosts = line.split()
    return {'ip':ip, 'hosts':hosts}


result = map(convert, DATA.splitlines())

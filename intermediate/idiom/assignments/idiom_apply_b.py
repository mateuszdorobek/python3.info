"""
* Assignment: Idiom MapFilter Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Define `result: list[dict]`, where each dict has keys:
       * ip: str
       * hosts: list[str]
    2. Skip comments (`#`) and empty lines
    3. Extract from each line: `ip` and `hosts`
    4. Add `ip` and `hosts` to `result` as a dict, example:
       {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Each line must be a separate dict
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
       * ip: str
       * hosts: list[str]
    2. Pomiń komentarze (`#`) i puste linie
    3. Wyciągnij z każdej linii: `ip` i `hosts`
    4. Dodaj `ip` i `hosts` do `result` jako słownik, przykład:
       {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Każda linia ma być osobnym słownikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * filter()
    * map()
    * len()
    * str.split()
    * str.startswith()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(valid), \
    'Object `valid` must be a function'

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> assert all(type(key) is str
    ...            for row in result
    ...            for key in row.keys()), \
    'All rows in `result` should be dict'

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']},
     {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
     {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
     {'ip': '::1', 'hosts': ['localhost']}]
"""

DATA = """##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
##

127.0.0.1       localhost astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

def valid(line: str) -> bool:
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


def parse(line: str) -> dict:
    ip, *hosts = line.split()
    return {'ip': ip, 'hosts': hosts}


# type: list[dict]
result = ...

# Solution
result = DATA.splitlines()
result = filter(valid, result)
result = map(parse, result)

"""
* Assignment: About EntryTest ListDict
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Define `result: list[dict]`, where each dict has keys:
       * ip: str
       * hosts: list[str]
    2. Iterate over lines in `DATA` skipping comments (`#`) and empty lines
    3. Extract from each line: `ip` and `hosts`
    4. Add `ip` and `hosts` to `result` as a dict, example:
       {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Each line must be a separate dict
    6. Merge host names with the same IP (important!)
    7. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
       * ip: str
       * hosts: list[str]
    2. Iteruj po liniach w `DATA` pomijając komentarze (`#`) i puste linie
    3. Wyciągnij z każdej linii: `ip` i `hosts`
    4. Dodaj `ip` i `hosts` do `result` jako słownik, przykład:
       {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Każda linia ma być osobnym słownikiem
    6. Scal nazwy hostów dla tego samego IP (ważne)
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All keys in `result` should be dict'
    >>> assert [x['ip'] for x in result].count('127.0.0.1') == 1, \
    'You did not merge hostnames for the same ip (127.0.0.1)'

    >>> pprint(result, width=120, sort_dicts=False)
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

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

# Dict keys: ip, hosts
# Merge hosts for the same ip
# type: list[dict]
result = ...


# Solution
result = []
for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue

    ip, *hosts = line.split()

    for row in result:
        if row['ip'] == ip:
            row['hosts'] += hosts
            break
    else:
        row = {'ip': ip, 'hosts': hosts}
        result.append(row)

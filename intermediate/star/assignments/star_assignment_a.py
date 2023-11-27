"""
* Assignment: Star Assignment List
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate ip address from host names
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj adres ip od nazwy hostów
    2. Skorzystaj z notacji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign your result to variable `ip`'
    >>> assert hosts is not Ellipsis, \
    'Assign your result to variable: `hosts`'
    >>> assert type(ip) is str, \
    'Variable `ip` has invalid type, should be str'
    >>> assert type(hosts) is list, \
    'Variable `hosts` has invalid type, should be list'
    >>> assert all(type(x) is str for x in hosts), \
    'All rows in `hosts` should be str'
    >>> assert '' not in hosts, \
    'Do not pass any arguments to str.split() method'

    >>> ip
    '10.13.37.1'

    >>> hosts
    ['nasa.gov', 'esa.int', 'polsa.gov.pl']
"""

DATA = ['10.13.37.1', 'nasa.gov', 'esa.int', 'polsa.gov.pl']

# String with IP address
# example: '10.13.37.1'
# type: str
ip = ...

# List of hosts
# example: ['nasa.gov', 'esa.int', 'polsa.gov.pl']
# type: list[str]
hosts = ...

# Solution
ip, *hosts = DATA

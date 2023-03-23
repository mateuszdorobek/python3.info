"""
* Assignment: Unpack Assignment Split
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Split input data
    2. Separate ip address and host name
    3. Run doctests - all must succeed

Polish:
    1. Podziel dane wejściowe
    2. Odseparuj adres ip i nazwę hosta
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign your result to variable `ip`'
    >>> assert host is not Ellipsis, \
    'Assign your result to variable `host`'
    >>> assert type(ip) is str, \
    'Variable `ip` has invalid type, should be str'
    >>> assert type(host) is str, \
    'Variable `hosts` has invalid type, should be str'

    >>> ip
    '10.13.37.1'

    >>> host
    'nasa.gov'
"""

DATA = '10.13.37.1 nasa.gov'

# IP address:
# example: 10.13.37.1
# type: str
ip = ...

# host name
# example: nasa.gov
# type: str
host = ...

# Solution
ip, host = DATA.split()

"""
* Assignment: File Read List of Dicts
* Type: homework
* Complexity: hard
* Lines of code: 19 lines
* Time: 21 min

English:
    1. Read file and for each line:
        a. Skip line if it's empty, is whitespace or starts with comment `#`
        b. Remove leading and trailing whitespaces
        c. Split line by whitespace
        d. Separate IP address and hosts names
        e. Use one line `if` to check whether dot `.` is in the IP address
        f. If is present then protocol is IPv4 otherwise IPv6
        g. Append IP address and hosts names to `result`
    3. Run doctests - all must succeed

Polish:
    1. Przeczytaj plik i dla każdej linii:
        a. Pomiń linię jeżeli jest pusta, jest białym znakiem
           lub zaczyna się od komentarza `#`
        b. Usuń białe znaki na początku i końcu linii
        c. Podziel linię po białych znakach
        d. Odseparuj adres IP i nazwy hostów
        e. Wykorzystaj jednolinikowego `if` do sprawdzenia czy jest
           kropka `.` w adresie IP
        f. Jeżeli jest obecna to protokół  jest IPv4,
           w przeciwnym przypadku IPv6
        g. Dodaj adres IP i nazwy hostów do `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`
    * `str.strip()`
    * `str.split()` - without an argument
    * `len()`
    * `str.startswith()`
    * `result = True if ... else False`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All keys in `result` should be dict'
    >>> assert [x['ip'] for x in result].count('127.0.0.1') == 1, \
    'You did not merge hostnames for the same ip (127.0.0.1)'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hostnames': ['localhost', 'astromatt'], 'protocol': 'IPv4'},
     {'ip': '10.13.37.1', 'hostnames': ['nasa.gov', 'esa.int'], 'protocol': 'IPv4'},
     {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'IPv4'},
     {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'IPv6'}]
"""

FILE = '_temporary.txt'

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Example [{'ip': '127.0.0.1', 'hostnames': ['localhost', 'astromatt'], 'protocol': 'IPv4'}, ...]
# type: list[dict]
result = []

with open(FILE) as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue
        ip, *hosts = line.split()



# Solution
result = []

with open(FILE) as file:
    for line in file:
        line = line.strip()

        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue

        ip, *hostnames = line.split()
        found = False

        for host in result:
            if host['ip'] == ip:
                host['hostnames'] += hostnames
                found = True
                break

        if not found:
            result.append({
                'ip': ip,
                'hostnames': list(hostnames),
                'protocol': 'IPv4' if '.' in ip else 'IPv6'
            })

# # Alternative solution
# for record in result:
#     if record['ip'] == ip:
#         record['hostnames'].update(hostnames)
#         break
# else:
#     result.append({
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6',
#         'ip': ip,
#     })

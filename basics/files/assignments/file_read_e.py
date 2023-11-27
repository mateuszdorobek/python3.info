"""
* Assignment: File Read DirtyFile
* Type: homework
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Modify code below:
        a. Remove leading and trailing whitespaces
        b. Skip line if it's empty, is whitespace or starts with comment `#`
        c. Split line by whitespace
        d. Separate IP address and hosts names
        e. Append IP address and hosts names to `result`
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej:
        a. Usuń białe znaki na początku i końcu linii
        b. Pomiń linię jeżeli jest pusta, jest białym znakiem
           lub zaczyna się od komentarza `#`
        c. Podziel linię po białych znakach
        d. Odseparuj adres IP i nazwy hostów
        e. Dodaj adres IP i nazwy hostów do `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

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
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'
    >>> assert all(type(x) is str for x in result.keys()), \
    'All keys in `result` should be str'
    >>> assert all(type(x) is list for x in result.values()), \
    'All values in `result` should be list'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'127.0.0.1': ['localhost'],
     '10.13.37.1': ['nasa.gov', 'esa.int'],
     '255.255.255.255': ['broadcasthost'],
     '::1': ['localhost']}
"""

FILE = '_temporary.txt'

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


# Example {'10.13.37.1': ['nasa.gov', 'esa.int'], ...}
# type: dict[str,list[str]]
result = {}

with open(FILE) as file:
    for line in file:
        ...


# Solution
result = {}

with open(FILE) as file:
    for line in file:
        line = line.strip()

        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue

        ip, *hostnames = line.split()

        if ip in result:
            result[ip] += hostnames
        else:
            result[ip] = hostnames

"""
* Assignment: File Read CleanFile
* Type: homework
* Complexity: medium
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Read `FILE` and for each line:
        a. Remove leading and trailing whitespaces
        b. Split line by whitespace
        c. Separate IP address and hosts names
        d. Append IP address and hosts names to `result`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` i dla każdej linii:
        a. Usuń białe znaki na początku i końcu linii
        b. Podziel linię po białych znakach
        c. Odseparuj adres IP i nazwy hostów
        d. Dodaj adres IP i nazwy hostów do `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.isspace()`
    * `str.split()`
    * `str.strip()`
    * `with`
    * `open()`

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

DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Example {'10.13.37.1': ['nasa.gov', 'esa.int'], ...}
# type: dict[str,list[str]]
result = ...

# Solution
result = {}

with open(FILE) as file:
    for line in file:
        ip, *hosts = line.strip().split()
        result[ip] = hosts

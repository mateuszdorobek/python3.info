"""
* Assignment: File Read CSV
* Type: class assignment
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Read `FILE`
    2. Separate header from data
    3. Write header (first line) to `header`
    4. Read file and for each line:
        a. Strip whitespaces
        b. Split line by coma `,`
        c. Convert measurements do `tuple[float]`
        d. Append measurements to `features`
        e. Append species name to `labels`
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE`
    2. Odseparuj nagłówek od danych
    3. Zapisz nagłówek (pierwsza linia) do `header`
    4. Zaczytaj plik i dla każdej linii:
        a. Usuń białe znaki z początku i końca linii
        b. Podziel linię po przecinku `,`
        c. Przekonwertuj pomiary do `tuple[float]`
        d. Dodaj pomiary do `features`
        e. Dodaj gatunek do `labels`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `tuple(float(x) for x in X)`
    * `str.split()`
    * `str.strip()`
    * `with`
    * `open()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove; remove(FILE)

    >>> assert header is not Ellipsis, \
    'Assign your result to variable `header`'
    >>> assert features is not Ellipsis, \
    'Assign your result to variable `features`'
    >>> assert labels is not Ellipsis, \
    'Assign your result to variable `labels`'
    >>> assert type(header) is list, \
    'Variable `header` has invalid type, should be list'
    >>> assert type(features) is list, \
    'Variable `features` has invalid type, should be list'
    >>> assert type(labels) is list, \
    'Variable `labels` has invalid type, should be list'
    >>> assert all(type(x) is str for x in header), \
    'All rows in `header` should be str'
    >>> assert all(type(x) is tuple for x in features), \
    'All rows in `features` should be tuple'
    >>> assert all(type(x) is str for x in labels), \
    'All rows in `labels` should be str'

    >>> header
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.4, 3.9, 1.3, 0.4),
     (5.9, 3.0, 5.1, 1.8),
     (6.0, 3.4, 4.5, 1.6),
     (7.3, 2.9, 6.3, 1.8),
     (5.6, 2.5, 3.9, 1.1),
     (5.4, 3.9, 1.3, 0.4)]

    >>> labels
    ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor', 'setosa']
"""

FILE = '_temporary.csv'

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""

header = []
features = []
labels = []

with open(FILE, mode='w') as file:
    file.write(DATA)

# Solution
with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *values, species = line.strip().split(',')
        values = tuple(float(x) for x in values)
        features.append(values)
        labels.append(species)

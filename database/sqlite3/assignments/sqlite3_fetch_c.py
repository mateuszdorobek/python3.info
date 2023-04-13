"""
* Assignment: SQLite3 Fetch CSV
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Read data from `FILE` (don't use `csv` or `pandas` library)
    2. Replace species from `int` to `str` according to `SPECIES`
       conversion table
    3. Connect to the `sqlite3` using context manager (`with`)
    4. Create table `iris` and write data to it
    5. Select data and add them to `result: list[dict]`
    6. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `FILE` (nie używaj biblioteki `csv` lub `pandas`)
    2. Podmień gatunki z `int` na `str` zgodnie z tabelą podstawień `SPECIES`
    3. Połącz się do bazy danych `sqlite3` używając context managera (`with`)
    4. Stwórz tabelę `iris` i zapisz do niej dane
    5. Wybierz dane i dodaj je do `result: list[dict]`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is not Ellipsis
    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(row) is dict for row in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'id': 4, 'species': 'virginica', 'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4},
     {'id': 3, 'species': 'versicolor', 'sepal_length': 5.7, 'sepal_width': 4.4, 'petal_length': 1.5, 'petal_width': 0.4},
     {'id': 5, 'species': 'versicolor', 'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.3},
     {'id': 8, 'species': 'versicolor', 'sepal_length': 5.4, 'sepal_width': 3.4, 'petal_length': 1.7, 'petal_width': 0.2},
     {'id': 1, 'species': 'setosa', 'sepal_length': 4.3, 'sepal_width': 3.0, 'petal_length': 1.1, 'petal_width': 0.1},
     {'id': 2, 'species': 'setosa', 'sepal_length': 5.8, 'sepal_width': 4.0, 'petal_length': 1.2, 'petal_width': 0.2},
     {'id': 6, 'species': 'setosa', 'sepal_length': 5.7, 'sepal_width': 3.8, 'petal_length': 1.7, 'petal_width': 0.3},
     {'id': 7, 'species': 'setosa', 'sepal_length': 5.1, 'sepal_width': 3.8, 'petal_length': 1.5, 'petal_width': 0.3},
     {'id': 9, 'species': 'setosa', 'sepal_length': 5.1, 'sepal_width': 3.7, 'petal_length': 1.5, 'petal_width': 0.4},
     {'id': 10, 'species': 'setosa', 'sepal_length': 4.6, 'sepal_width': 3.6, 'petal_length': 1.0, 'petal_width': 0.2}]

    >>> from pathlib import Path
    >>> Path(FILE).unlink(missing_ok=True)
"""

import sqlite3

DATABASE = ':memory:'
FILE = '_temporary.csv'

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'}

DATA = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species TEXT,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL);"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :species,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width);"""

SQL_SELECT = """
    SELECT *
    FROM iris
    ORDER BY species DESC, id ASC;"""

with open(FILE, mode='w') as file:
    file.write(DATA)


# Select all results from database in list[dict] format
# Example [{'id': 4,
#           'species': 'virginica',
#           'sepal_length': 5.4,
#           'sepal_width': 3.9,
#           'petal_length': 1.3,
#           'petal_width': 0.4}, ...]
# type: list[tuple]
result = ...

# Solution
data = []
with open(FILE) as file:
    for line in file:
        line = line.strip().split(',')
        data.append({
            'sepal_length': float(line[0]),
            'sepal_width': float(line[1]),
            'petal_length': float(line[2]),
            'petal_width': float(line[3]),
            'species': SPECIES[int(line[4])],
        })

with sqlite3.connect(DATABASE) as db:
    db.row_factory = sqlite3.Row
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, data)
    result = [dict(x) for x in db.execute(SQL_SELECT)]

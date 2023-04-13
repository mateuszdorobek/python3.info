"""
* Assignment: SQLite3 Join Relations
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Connect to database:
        a. Set returned result type to `sqlite3.Row`
        b. Get cursor and next things execute on it
        c. Execute `SQL_CREATE_TABLE_ASTRONAUTS` to create table `astronauts`
        d. Execute `SQL_CREATE_TABLE_ADDRESSES` to create table `addresses`
        e. Execute `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` to create index
    2. Iterate over `DATA`:
        a. Seprate `crew` from other values
        b. Execute `SQL_INSERT_ASTRONAUT` to insert astroanut to database
        c. Get `id` of the last inserted row (`cursor.lastrowid`)
        d. Add `id` to each address
        e. Executing `SQL_INSERT_ADDRESS` insert `addresses` to database
    3. Executing `SQL_SELECT` select data from database:
        a. Join data from both tables
        b. Append each row to `result: list[dict]`
    4. Run doctests - all must succeed

Polish:
    1. Połącz się do bazy danych:
        a. Ustaw typ zwracanych wyników na `sqlite3.Row`
        b. Pobierz kursor i następne polecenia wykonuj na nim
        c. Wykonując `SQL_CREATE_TABLE_ASTRONAUTS` stwórz tabelę `astronauts`
        d. Wykonując `SQL_CREATE_TABLE_ADDRESSES` stwórz tabelę `addresses`
        e. Wykonując `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` stwórz indeks
    2. Iteruj po `DATA`:
        a. Oddziel `crew` od pozostałych wartości
        b. Wykonując `SQL_INSERT_ASTRONAUT` wstaw astronautę do bazy
        c. Pobierz `id` ostatniego wstawianego wiersza (`cursor.lastrowid`)
        d. Dodaj to `id` do każdego adresu
        e. Wykonując `SQL_INSERT_ADDRESS` wstaw adresy do bazy danych
    3. Wykonując `SQL_SELECT` wybierz dane z bazy:
        a. Połącz dane z obu tabel
        b. Dodaj każdy rekord do `result: list[dict]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `cursor = db.cursor()`
    * `astronaut_id = cursor.lastrowid`

Tests:
    TODO: import sys; sys.tracebacklimit = 0

    TODO: assert type(result) is not Ellipsis
    TODO: assert type(result) is list
    TODO: assert len(result) > 0
    TODO: assert all(type(row) is dict for row in result)

    TODO: result  # doctest: +NORMALIZE_WHITESPACE
"""

import sqlite3

DATABASE = ':memory:'

DATA = {"mission": "Ares 3",
        "launch_date": "2035-06-29T00:00:00",
        "destination": "Mars",
        "destination_landing": "2035-11-07T00:00:00",
        "destination_location": "Acidalia Planitia",
        "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"},
                 {"name": "Rick Martinez", "born": "1996-01-21"},
                 {"name": "Alex Vogel", "born": "1994-11-15"},
                 {"name": "Chris Beck", "born": "1999-08-02"},
                 {"name": "Beth Johanssen", "born": "2006-05-09"},
                 {"name": "Mark Watney", "born": "1994-10-12"}]}


# Select all results from database in list[dict] format
# Example [{'id': 1, 'firstname': 'José', 'lastname': 'Jiménez',
#           'astronaut_id': 1, 'street': '2101 E NASA Pkwy', 'city':
#           'Houston', 'state': 'Texas', 'code': 77058, 'country': 'USA'}, ...]
# type: list[tuple]
result = ...


# Solution


SQL_CREATE_TABLE = """

    CREATE TABLE

"""

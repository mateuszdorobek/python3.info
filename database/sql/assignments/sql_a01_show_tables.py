"""
* Assignment: Database Show Tables
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show all tables in database
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić wszystkie tabele w bazie danych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

SELECT name
FROM sqlite_master
WHERE type='table'

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for table in db.execute(SQL):
        print(table['name'])

# Solution

SQL = """

SELECT name
FROM sqlite_master
WHERE type='table'

"""

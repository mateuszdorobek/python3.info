"""
* Assignment: Database Select Limit
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. columns: datetime, category, event
       c. limit: 30
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumny: datetime, category, event
       c. limit: 30
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

SELECT datetime, category, event
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(SQL)):
        print(result)


# Solution

SQL = """

SELECT datetime, category, event
FROM apollo11
LIMIT 30

"""

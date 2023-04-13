"""
* Assignment: Database Delete All
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete all records:
       a. table: contacts
       b. record: all
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować wszystkie rekordy:
       a. tabela: contacts
       b. rekord: wszystkie
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to delete all records:
# - table: contacts
# - record: all
# type: str
result = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(result)


# Solution
result = """

DELETE FROM contacts

"""

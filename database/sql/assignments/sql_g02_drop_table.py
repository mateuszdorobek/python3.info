"""
* Assignment: Database Drop Table
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete:
       a. table: contacts
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować:
       a. tabela: contacts
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to delete:
# - table: contacts
# type: str
result = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(result)


# Solution
result = """

DROP TABLE contacts

"""

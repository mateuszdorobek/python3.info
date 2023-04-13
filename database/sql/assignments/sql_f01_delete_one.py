"""
* Assignment: Database Delete One
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete one record:
       a. table: contacts
       b. where: id == 1
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować rekord:
       a. tabela: contacts
       b. gdzie: id == 1
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to delete one record:
# - table: contacts
# - where: id == 1
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
WHERE id == 1

"""

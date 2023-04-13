"""
* Assignment: Database Delete Many
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete many records:
       a. table: contacts
       b. where: lastname == 'Watney'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować wiele rekordów:
       a. tabela: contacts
       b. gdzie: lastname == 'Watney'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to delete many records:
# - table: contacts
# - where: lastname == 'Watney'
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
WHERE lastname == 'Watney'

"""

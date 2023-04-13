"""
* Assignment: Database Update One
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to update one record:
       a. table: contacts
       b. where: id == 1
       c. column: mission
       d. value: Ares3
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby zaktualizować jeden rekord:
       a. tabela: contacts
       b. gdzie: id == 1
       c. kolumna: mission
       d. wartość: Ares3
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to update one record:
# - table: contacts
# - where: id == 1
# - column: mission
# - value: Ares3
# type: str
result = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(result)


# Solution
result = """

UPDATE contacts SET
    mission = 'Ares3'
WHERE id == 1

"""

"""
* Assignment: Database Update All
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to update all records:
       a. table: contacts
       b. where: all
       c. column: mission
       d. value: Ares3
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby zaktualizować wszystkie rekordy:
       a. tabela: contacts
       b. gdzie: wszystkie
       c. kolumna: mission
       d. wartość: Ares3
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to update all records:
# - table: contacts
# - where: all
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

"""

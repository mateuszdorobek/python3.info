"""
* Assignment: Database Insert Raw
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data:
       a. table: contacts
       b. firstname: 'Mark'
       c. lastname: 'Watney'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane:
       a. tabela: contacts
       b. firstname: 'Mark'
       c. lastname: 'Watney'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to insert data:
# - table: contacts
# - firstname: 'Mark'
# - lastname: 'Watney'
# type: str
result = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(result)


# Solution
result = """

INSERT INTO contacts (firstname, lastname)
VALUES ('Mark', 'Watney')

"""

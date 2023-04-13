"""
* Assignment: Database Insert Dict
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data:
       a. table: contacts
       b. data: `DATA: dict`
       c. use: prepared statement (with `:column`)
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane:
       a. tabela: contacts
       b. dane: `DATA: dict`
       c. użyj: przygotowanego zapytania (z `:column`)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to insert data:
# - table: contacts
# - data: `DATA: dict`
# - use: prepared statement (with `:column`)
# type: str
result = """

INSERT INTO contacts (firstname, lastname)
VALUES ()

"""


DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
}

with sqlite3.connect('sql.db') as db:
    db.execute(result, DATA)


# Solution
result = """

INSERT INTO contacts (firstname, lastname)
VALUES (:firstname, :lastname)

"""

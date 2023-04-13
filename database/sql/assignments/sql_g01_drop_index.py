"""
* Assignment: Database Drop Index
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to delete index:
       a. table: contacts
       b. name: idx_contacts_lastname
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby skasować indeks:
       a. tabela: contacts
       b. nazwa: idx_contacts_lastname
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to delete index:
# - table: contacts
# - name: idx_contacts_lastname
# type: str
result = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(result)


# Solution
result = """

DROP INDEX idx_contacts_lastname

"""

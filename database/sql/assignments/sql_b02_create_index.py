"""
* Assignment: Database Create Index
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to create index:
       a. name: idx_contacts_lastname
       b. table: contacts
       c. column: lastname
       d. use: IF NOT EXISTS
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć indeks:
       a. nazwa: idx_contacts_lastname
       b. tabela: contacts
       c. kolumna: lastname
       d. użyj: IF NOT EXISTS
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     _ = db.execute(result)
    ...     sql = 'SELECT name FROM sqlite_master WHERE type="index"'
    ...     for table in db.execute(sql):
    ...         print(table['name'])
    ix_apollo11_datetime
    lastname_index
    missions_name_uindex
    idx_contacts_lastname

    TODO: unify index names
"""


# Write SQL query to create index:
# - name: idx_contacts_lastname
# - table: contacts
# - column: lastname
# - use: IF NOT EXISTS
# type: str
result = """

-- replace this comment
-- with your sql query

"""

# Solution
result = """

CREATE INDEX IF NOT EXISTS idx_contacts_lastname
ON contacts(lastname)

"""

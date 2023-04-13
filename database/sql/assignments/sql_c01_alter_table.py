"""
* Assignment: Database Alter Table
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to add column:
       a. table: contacts
       b. column: mission
       c. type: text
       d. default: null
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby dodać kolumnę:
       a. tabela: contacts
       b. kolumna: mission
       c. type: text
       d. wartość domyślna: null
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     try:
    ...         _ = db.execute(result)
    ...     except sqlite3.OperationalError:
    ...         pass
    ...     sql = 'SELECT sql FROM sqlite_master WHERE tbl_name="contacts"'
    ...     for schema in db.execute(sql):
    ...         print(schema['sql'], sep='')  # doctest: +NORMALIZE_WHITESPACE
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        birthday DATE DEFAULT NULL
    , mission TEXT DEFAULT NULL)
    CREATE INDEX idx_contacts_lastname
    ON contacts(lastname)
    <BLANKLINE>
    <BLANKLINE>
"""


# Write SQL query to add column:
# - table: contacts
# - column: mission
# - type: text
# - default: null
# type: str
result = """

-- replace this comment
-- with your sql query

"""

# Solution
result = """

ALTER TABLE contacts
ADD COLUMN mission TEXT DEFAULT NULL

"""

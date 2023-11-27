"""
* Assignment: Database Show Schema
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show schema for a table:
       a. table: apollo11
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić schemat tabeli:
       a. table: apollo11
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     table = db.execute(result).fetchall()
    ...     result = [column['sql'] for column in table]

    >>> print(result[0])  # doctest: +NORMALIZE_WHITESPACE
    CREATE TABLE "apollo11" (
      "datetime" TIMESTAMP,
      "date" DATE,
      "time" TIME,
      "met" INTEGER,
      "category" TEXT,
      "event" TEXT
    )

    >>> print(result[1])
    CREATE INDEX "ix_apollo11_datetime"ON "apollo11" ("datetime")
"""


# Show schema for a table `apollo11`
# type: str
result = """

SELECT sql
FROM sqlite_master
WHERE tbl_name = 'apollo11'

"""

# Solution
result = """

SELECT sql
FROM sqlite_master
WHERE tbl_name = 'apollo11'

"""

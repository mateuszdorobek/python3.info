"""
* Assignment: Database Show Data
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show all data in a table:
       a. table: apollo11
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić wszystkie dane w tabeli:
       b. table: apollo11
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> from pprint import pprint
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     table = db.execute(result)
    ...     result = list(map(dict, table))

    >>> len(result)
    250

    >>> pprint(result[0], width=72, sort_dicts=False)
    {'datetime': '1969-07-14 21:00:00',
     'date': '1969-07-14',
     'time': '21:00:00.000000',
     'met': -100800000000000,
     'category': 'DEBUG',
     'event': 'Terminal countdown started.'}

    >>> pprint(result[145], width=72, sort_dicts=False)
    {'datetime': '1969-07-21 02:56:15',
     'date': '1969-07-21',
     'time': '02:56:15.000000',
     'met': 393855000000000,
     'category': 'CRITICAL',
     'event': '1st step taken lunar surface (CDR). “That’s one small step '
              'for a man…one giant leap for mankind.”'}

    >>> pprint(result[249], width=72, sort_dicts=False)
    {'datetime': '1969-08-27 00:00:00',
     'date': '1969-08-27',
     'time': '00:00:00.000000',
     'met': -9223372036854775808,
     'category': 'DEBUG',
     'event': 'EASEP turned off by ground command.'}
"""


# Show all data in `apollo11` table
# type: str
result = """

SELECT *
FROM apollo11

"""

# Solution
result = """

SELECT *
FROM apollo11

"""

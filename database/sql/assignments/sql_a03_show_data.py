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
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     for result in map(dict, db.execute(result)):
    ...         print(result)  # doctest: +ELLIPSIS
    {'datetime': '1969-07-14 21:00:00', 'date': '1969-07-14', 'time': '21:00:00.000000', 'met': -100800000000000, 'category': 'DEBUG', 'event': 'Terminal countdown started.'}
    {'datetime': '1969-07-15 16:00:00', 'date': '1969-07-15', 'time': '16:00:00.000000', 'met': -32400000000000, 'category': 'DEBUG', 'event': 'Scheduled 11-hour hold at T-9 hours.'}
    {'datetime': '1969-07-16 03:00:00', 'date': '1969-07-16', 'time': '03:00:00.000000', 'met': -32400000000000, 'category': 'DEBUG', 'event': 'Countdown resumed at T-9 hours.'}
    {'datetime': '1969-07-16 08:30:00', 'date': '1969-07-16', 'time': '08:30:00.000000', 'met': -12600000000000, 'category': 'DEBUG', 'event': 'Scheduled 1-hour 32-minute hold at T-3 hours 30 minutes.'}
    {'datetime': '1969-07-16 10:02:00', 'date': '1969-07-16', 'time': '10:02:00.000000', 'met': -12600000000000, 'category': 'DEBUG', 'event': 'Countdown resumed at T-3 hours 30 minutes.'}
    {'datetime': '1969-07-16 13:31:43', 'date': '1969-07-16', 'time': '13:31:43.000000', 'met': -16000000000, 'category': 'DEBUG', 'event': 'Guidance reference release.'}
    {'datetime': '1969-07-16 13:31:51', 'date': '1969-07-16', 'time': '13:31:51.000000', 'met': -8000000000, 'category': 'DEBUG', 'event': 'S-IC engine start command.'}
    ...
    {'datetime': '1969-08-10 00:00:00', 'date': '1969-08-10', 'time': '00:00:00.000000', 'met': -9223372036854775808, 'category': 'DEBUG', 'event': 'Crew released from quarantine.'}
    {'datetime': '1969-08-14 00:00:00', 'date': '1969-08-14', 'time': '00:00:00.000000', 'met': -9223372036854775808, 'category': 'DEBUG', 'event': 'CM delivered to contractor’s facility in Downey, CA.'}
    {'datetime': '1969-08-27 00:00:00', 'date': '1969-08-27', 'time': '00:00:00.000000', 'met': -9223372036854775808, 'category': 'DEBUG', 'event': 'EASEP turned off by ground command.'}
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

"""
* Assignment: SQLite3 Fetch Logs
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Extract date, time, log level and message from each line
    2. Parse date and time as date and time objects
    3. Combine date and time into datetime object
    4. Define datetime, level and message as tuple
    5. Connect to database:
       a. Execute `SQL_CREATE_TABLE` to create database table
       b. Execute `SQL_INSERT` to insert logs to in `list[tuple]` format
       c. Execute `SQL_SELECT` to select data
       d. Iterate over rows and append each to `result: list[tuple]`
    6. Run doctests - all must succeed

Polish:
    1. Wyciągnij datę, czas, poziom logowania i teść z każdej linii
    2. Rozczytaj datę i czas jako obiekty date and time
    3. Połącz datę i czas w obiekt datetime
    4. Zdefiniuj datetime, level i message jako tuplę
    5. Połącz się do bazy danych:
       a. Wykonaj `SQL_CREATE_TABLE` aby stworzyć tabelę w bazie danych
       b. Wykonaj `SQL_INSERT` aby wstawić logi w formacie `list[tuple]`
       c. Wykonaj `SQL_SELECT` aby wybrać dane
       d. Iterując po wierszach dopisuj je do `result: list[tuple]`
    6. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] National Aeronautics and Space Administration.
        Apollo 11 timeline.
        Year: 1969. Retrieved: 2021-03-25.
        URL: https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

Hints:
    * `datetime.fromisoformat(str)`
    * `datetime.combine(date, time)`
    * `datetime.strptime(str, format)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is not Ellipsis
    >>> assert type(result) is list
    >>> assert len(result) > 0
    >>> assert all(type(row) is tuple for row in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [(28, '1969-07-24 17:29:00', 'INFO', 'Crew egress'),
     (27, '1969-07-24 16:50:35', 'WARNING', 'Splashdown (went to apex-down)'),
     (26, '1969-07-24 16:35:05', 'WARNING', 'Entry'),
     (25, '1969-07-24 16:21:12', 'INFO', 'CM/SM separation'),
     (24, '1969-07-22 04:55:42', 'WARNING', 'Transearth injection ignition (SPS)'),
     (23, '1969-07-21 21:35:00', 'INFO', 'CSM/LM docked'),
     (22, '1969-07-21 17:54:00', 'WARNING', 'LM lunar liftoff ignition (LM APS)'),
     (21, '1969-07-21 05:11:13', 'DEBUG', 'EVA ended (hatch closed)'),
     (20, '1969-07-21 03:15:16', 'INFO', 'LMP on lunar surface'),
     (19, '1969-07-21 03:05:58', 'DEBUG', 'Contingency sample collection started (CDR)'),
     (18, '1969-07-21 02:56:16', 'WARNING', 'Neil Armstrong first words on the Moon'),
     (17, '1969-07-21 02:56:15', 'WARNING', '1st step taken lunar surface (CDR)'),
     (16, '1969-07-21 02:39:33', 'DEBUG', 'EVA started (hatch open)'),
     (15, '1969-07-20 20:17:39', 'WARNING', 'LM lunar landing'),
     (14, '1969-07-20 20:14:18', 'ERROR', 'LM 1201 alarm'),
     (13, '1969-07-20 20:10:22', 'ERROR', 'LM 1202 alarm'),
     (12, '1969-07-20 20:05:05', 'WARNING', 'LM powered descent engine ignition'),
     (11, '1969-07-20 17:44:00', 'INFO', 'CSM/LM undocked'),
     (10, '1969-07-16 21:43:36', 'INFO', 'Lunar orbit circularization ignition'),
     (9, '1969-07-16 17:21:50', 'INFO', 'Lunar orbit insertion ignition'),
     (8, '1969-07-16 16:56:03', 'INFO', 'CSM docked with LM/S-IVB'),
     (7, '1969-07-16 16:22:13', 'INFO', 'Translunar injection'),
     (6, '1969-07-16 13:39:40', 'DEBUG', 'S-II center engine cutoff'),
     (5, '1969-07-16 13:35:17', 'DEBUG', 'Launch escape tower jettisoned'),
     (4, '1969-07-16 13:34:44', 'WARNING', 'S-II ignition'),
     (3, '1969-07-16 13:33:23', 'DEBUG', 'Maximum dynamic pressure (735.17 lb/ft^2)'),
     (2, '1969-07-16 13:31:53', 'WARNING', 'S-IC engine ignition (#5)'),
     (1, '1969-07-14 21:00:00', 'INFO', 'Terminal countdown started')]
"""

import sqlite3
from datetime import date, datetime, time

DATABASE = ':memory:'

DATA = [
    ('1969-07-14 21:00:00', 'INFO', 'Terminal countdown started'),
    ('1969-07-16 13:31:53', 'WARNING', 'S-IC engine ignition (#5)'),
    ('1969-07-16 13:33:23', 'DEBUG', 'Maximum dynamic pressure (735.17 lb/ft^2)'),
    ('1969-07-16 13:34:44', 'WARNING', 'S-II ignition'),
    ('1969-07-16 13:35:17', 'DEBUG', 'Launch escape tower jettisoned'),
    ('1969-07-16 13:39:40', 'DEBUG', 'S-II center engine cutoff'),
    ('1969-07-16 16:22:13', 'INFO', 'Translunar injection'),
    ('1969-07-16 16:56:03', 'INFO', 'CSM docked with LM/S-IVB'),
    ('1969-07-16 17:21:50', 'INFO', 'Lunar orbit insertion ignition'),
    ('1969-07-16 21:43:36', 'INFO', 'Lunar orbit circularization ignition'),
    ('1969-07-20 17:44:00', 'INFO', 'CSM/LM undocked'),
    ('1969-07-20 20:05:05', 'WARNING', 'LM powered descent engine ignition'),
    ('1969-07-20 20:10:22', 'ERROR', 'LM 1202 alarm'),
    ('1969-07-20 20:14:18', 'ERROR', 'LM 1201 alarm'),
    ('1969-07-20 20:17:39', 'WARNING', 'LM lunar landing'),
    ('1969-07-21 02:39:33', 'DEBUG', 'EVA started (hatch open)'),
    ('1969-07-21 02:56:15', 'WARNING', '1st step taken lunar surface (CDR)'),
    ('1969-07-21 02:56:16', 'WARNING', 'Neil Armstrong first words on the Moon'),
    ('1969-07-21 03:05:58', 'DEBUG', 'Contingency sample collection started (CDR)'),
    ('1969-07-21 03:15:16', 'INFO', 'LMP on lunar surface'),
    ('1969-07-21 05:11:13', 'DEBUG', 'EVA ended (hatch closed)'),
    ('1969-07-21 17:54:00', 'WARNING', 'LM lunar liftoff ignition (LM APS)'),
    ('1969-07-21 21:35:00', 'INFO', 'CSM/LM docked'),
    ('1969-07-22 04:55:42', 'WARNING', 'Transearth injection ignition (SPS)'),
    ('1969-07-24 16:21:12', 'INFO', 'CM/SM separation'),
    ('1969-07-24 16:35:05', 'WARNING', 'Entry'),
    ('1969-07-24 16:50:35', 'WARNING', 'Splashdown (went to apex-down)'),
    ('1969-07-24 17:29:00', 'INFO', 'Crew egress'),
]


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        level TEXT,
        message TEXT);"""

SQL_INSERT = 'INSERT INTO logs VALUES (NULL, ?, ?, ?);'
SQL_SELECT = 'SELECT * FROM logs ORDER BY datetime DESC;'

# Select all results from database in list[tuple] format
# Example [(28, '1969-07-24 17:29:00', 'INFO', 'Crew egress'), ...]
# type: list[tuple]
result = ...

# Solution
with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, DATA)
    result = list(db.execute(SQL_SELECT))

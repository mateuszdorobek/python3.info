"""
* Assignment: Database Connection Test
* Complexity: easy
* Lines of code: 0 lines
* Time: 2 min

English:
    1. Run file to check database connection
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby sprawdzić połączenie do bazy danych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3
from urllib.request import urlopen
from pathlib import Path


DATA = 'https://python3.info/_static/space.db'
database = Path('sql.db')


# Download database from server
with urlopen(DATA) as db:
    content = db.read()
    database.write_bytes(content)


if not database.exists():
    print('Error with database!')
    print(f'Check if `{database}` is present in current directory')
    print('Please notify instructor')
    exit(1)


try:
    db = sqlite3.connect(database)
except Exception:
    print('Error with connection')
    print('Check if you have SQLite3 installed with your Python')
    print('Please notify instructor')
    exit(1)


try:
    result = db.execute('SELECT name FROM sqlite_master')
    tables = {row[0] for row in result}
except Exception:
    print('Error with database')
    print(f'Check if `{database}` is valid SQLite3 database')
    print('Please notify instructor')
    exit(1)


if 'apollo11' not in tables:
    print('Error with table')
    print('Check if database file is not corrupted')
    print('Please notify instructor')
    exit(1)


print('Everything is ok')
print('Please notify instructor')


# Solution

SQLite3 Insert Constraints
==========================


Unique
------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         login INTEGER UNIQUE,
...         firstname TEXT,
...         lastname TEXT);"""
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts
...     VALUES (NULL, :login, :firstname, :lastname);"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts;"""
>>>
>>> data = [
...     {'login': 'mwatney', 'firstname': 'Mark', 'lastname': 'Watney'},
...     {'login': 'mwatney', 'firstname': 'Melissa', 'lastname': 'Lewis'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.executemany(SQL_INSERT, data)
Traceback (most recent call last):
sqlite3.IntegrityError: UNIQUE constraint failed: astronauts.login
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     _ = db.execute(SQL_CREATE_TABLE)
...     try:
...         db.executemany(SQL_INSERT, data)
...     except sqlite3.IntegrityError:
...         print('Login need to be UNIQUE')
Login need to be UNIQUE


Programming Error
-----------------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         firstname TEXT,
...         lastname TEXT);"""
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts
...     VALUES (NULL, ?, ?);"""
>>>
>>>
>>> data = [{'firstname': 'Mark', 'lastname': 'Watney'},
...         {'firstname': 'Melissa', 'lastname': 'Lewis'},
...         {'firstname': 'Rick', 'lastname': 'Martinez'},
...         {'firstname': 'Alex', 'lastname': 'Vogel'},
...         {'firstname': 'Beth', 'lastname': 'Johanssen'},
...         {'firstname': 'Chris', 'lastname': 'Beck'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor = db.cursor()
...     cursor.execute(SQL_CREATE_TABLE)
...     cursor.executemany(SQL_INSERT, data)
Traceback (most recent call last):
sqlite3.ProgrammingError: Binding 1 has no name, but you supplied a dictionary (which has only names).


Operational Error
-----------------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         firstname TEXT,
...         lastname TEXT);"""
>>>
>>> SQL_CREATE_INDEX = """
...     CREATE INDEX
...     IF NOT EXISTS
...     astronauts_lastname_index
...     ON astronaut (lastname);"""
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     db.execute(SQL_CREATE_TABLE)
...     db.execute(SQL_CREATE_INDEX)
Traceback (most recent call last):
sqlite3.OperationalError: no such table: main.astronaut

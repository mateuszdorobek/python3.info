SQLite3 Cursor
==============
* ``db.cursor() -> cursor``
* ``cursor.lastrowid``


Create Cursor
-------------
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
...     VALUES (NULL, :firstname, :lastname);"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts;"""
>>>
>>> data = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
...     {'firstname': 'Alex', 'lastname': 'Vogel'},
...     {'firstname': 'Beth', 'lastname': 'Johanssen'},
...     {'firstname': 'Chris', 'lastname': 'Beck'},
... ]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor = db.cursor()
...     _ = cursor.execute(SQL_CREATE_TABLE)
...     _ = cursor.executemany(SQL_INSERT, data)
...     for row in cursor.execute(SQL_SELECT):
...         print(row)
(1, 'Mark', 'Watney')
(2, 'Melissa', 'Lewis')
(3, 'Rick', 'Martinez')
(4, 'Alex', 'Vogel')
(5, 'Beth', 'Johanssen')
(6, 'Chris', 'Beck')


Last Row ID
-----------
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
...     VALUES (NULL, :firstname, :lastname);"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts;"""
>>>
>>> data = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor = db.cursor()
...     _ = cursor.execute(SQL_CREATE_TABLE)
...     _ = cursor.execute(SQL_INSERT, data)
...     print(cursor.lastrowid)
1

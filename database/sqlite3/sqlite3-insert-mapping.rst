SQLite3 Insert Mapping
======================


Insert One
----------
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
>>>
>>> data = {'firstname': 'Mark',
...         'lastname': 'Watney'}
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.execute(SQL_INSERT, data)


Insert Many
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
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.executemany(SQL_INSERT, data)

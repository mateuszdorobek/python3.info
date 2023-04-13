SQLite3 Insert Sequence
=======================


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
...     VALUES (NULL, ?, ?);"""
>>>
>>> data = ('Mark', 'Watney')
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
...     VALUES (NULL, ?, ?);"""
>>>
>>> data = [
...     ('Mark', 'Watney'),
...     ('Melissa', 'Lewis'),
...     ('Rick', 'Martinez'),
...     ('Alex', 'Vogel'),
...     ('Beth', 'Johanssen'),
...     ('Chris', 'Beck')]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.executemany(SQL_INSERT, data)

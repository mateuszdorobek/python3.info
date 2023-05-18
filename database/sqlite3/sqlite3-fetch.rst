SQLite3 Fetch
=============
* Fetch as `list[tuple]` / `list[list]`
* Fetch as `list[Row]` / `list[dict]`
* `sqlite3.row_factory`

.. figure:: img/sqlite3-fetch-rowfactory-tuple.png
.. figure:: img/sqlite3-fetch-rowfactory-row.png


Fetch Sequences
---------------
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
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.executemany(SQL_INSERT, data)
...     for row in db.execute(SQL_SELECT):
...         print(row)
(1, 'Mark', 'Watney')
(2, 'Melissa', 'Lewis')
(3, 'Rick', 'Martinez')
(4, 'Alex', 'Vogel')
(5, 'Beth', 'Johanssen')
(6, 'Chris', 'Beck')


Fetch Mappings
--------------
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
...     db.row_factory = sqlite3.Row
...     _ = db.execute(SQL_CREATE_TABLE)
...     _ = db.executemany(SQL_INSERT, data)
...     for row in db.execute(SQL_SELECT):
...         print(dict(row))
{'id': 1, 'firstname': 'Mark', 'lastname': 'Watney'}
{'id': 2, 'firstname': 'Melissa', 'lastname': 'Lewis'}
{'id': 3, 'firstname': 'Rick', 'lastname': 'Martinez'}
{'id': 4, 'firstname': 'Alex', 'lastname': 'Vogel'}
{'id': 5, 'firstname': 'Beth', 'lastname': 'Johanssen'}
{'id': 6, 'firstname': 'Chris', 'lastname': 'Beck'}


Assignments
-----------
.. literalinclude:: assignments/sqlite3_fetch_a.py
    :caption: :download:`Solution <assignments/sqlite3_fetch_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sqlite3_fetch_b.py
    :caption: :download:`Solution <assignments/sqlite3_fetch_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sqlite3_fetch_c.py
    :caption: :download:`Solution <assignments/sqlite3_fetch_c.py>`
    :end-before: # Solution

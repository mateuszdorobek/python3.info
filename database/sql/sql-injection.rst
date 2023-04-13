SQL Injection
=============

.. warning:: This is to demonstrate a serious problem.
             Do not that statements in your code!

SetUp
-----
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>>
>>> IN1 = "' OR 1=1; DROP TABLE users --"
>>> IN2 = "whatever"
>>> input = MagicMock(side_effect=[IN1, IN2])


Scenario
--------
Ask user for credentials:

>>> username = input('Username: ')
>>> password = input('Password: ')

System uses SQL query with variable substitution:

>>> SQL_QUERY = f"""
...     SELECT * FROM users
...     WHERE username='{username}'
...     AND password='{password}';
... """

System executes query on database:

>>> print(SQL_QUERY)
<BLANKLINE>
    SELECT * FROM users
    WHERE username='' OR 1=1; DROP TABLE users --'
    AND password='whatever';
<BLANKLINE>

Exploited SQL injection, will SELECT all users with their data and then
DROP all data from table users!

Why this happened? Because user input:

>>> print(username)
' OR 1=1; DROP TABLE users --
>>>
>>> print(password)
whatever

.. warning:: This is to demonstrate a serious problem.
             Do not that statements in your code!

.. figure:: img/sql-injection.jpg

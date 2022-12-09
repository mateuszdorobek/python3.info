"""
* Assignment: Database Where LessOrEqual
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


result = """

SELECT datetime, category, event
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)


# Solution
result = """

SELECT datetime, category, event
FROM apollo11
WHERE date <= '1969-07-22'

"""

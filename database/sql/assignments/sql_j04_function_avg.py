"""
* Assignment: Database Function Avg
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
    TODO: add column which can be averaged
    TODO: assignment content
    TODO: helper comment
"""

import sqlite3


result = """

SELECT met
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)


# Solution
result = """

SELECT AVG(met)
FROM apollo11

"""

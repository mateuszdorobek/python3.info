"""
* Assignment: Database Where NotIn
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. columns: datetime, category, event
       c. where: date is not: July 20th, 21st or 22nd, 1969
       d. use: NOT IN
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumny: datetime, category, event
       c. gdzie: data to nie 20, 21 lub 22 lipca 1969
       d. użyj: NOT IN
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to select data:
# - table: apollo11
# - columns: datetime, category, event
# - where: date is not: July 20th, 21st or 22nd, 1969
# - use: NOT IN
# type: str
result = """

SELECT datetime, category, event
FROM apollo11
WHERE date

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)


# Solution
result = """

SELECT datetime, category, event
FROM apollo11
WHERE date NOT IN ('1969-07-20', '1969-07-21', '1969-07-22')

"""

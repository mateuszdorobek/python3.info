"""
* Assignment: Database Where Or
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. columns: datetime, category, event
       c. where: date is July 20 or 21, 1969
       d. use: OR
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumny: datetime, category, event
       c. gdzie: data to 20 lub 21 lipca 1969
       d. użyj: OR
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to select data:
# - table: apollo11
# - columns: datetime, category, event
# - where: date is July 20 or 21, 1969
# - use: OR
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
WHERE date == '1969-07-20'
   OR date == '1969-07-21'

"""

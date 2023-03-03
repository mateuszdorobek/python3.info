"""
* Assignment: Database Select OrderByNulls
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. columns: datetime, category, event
       c. order1: category descending empty values first
       d. order2: datetime ascending empty values last
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumny: datetime, category, event
       c. kolejność1: category malejąco wartości puste na początku
       d. kolejność2: datetime rosnąco wartości puste na końcu
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to select data:
# - table: apollo11
# - columns: datetime, category, event
# - order1: category descending empty values first
# - order2: datetime ascending empty values last
# type: str
result = """

SELECT datetime, category, event
FROM apollo11
ORDER BY category DESC,
         datetime ASC

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)


# Solution
result = """

SELECT datetime, category, event
FROM apollo11
ORDER BY category DESC NULLS FIRST,
         datetime ASC NULLS LAST

"""

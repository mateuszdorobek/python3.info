"""
* Assignment: Database Subquery CTE
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. columns: datetime, category, event
       c. where: category is has less than 50 occurrences
       d. use: CTE - Common Table Expression
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumny: datetime, category, event
       c. gdzie: kategoria ma mniej niż 50 wystąpień
       d. użyj: CTE - Common Table Expression
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


# Write SQL query to select data:
# - table: apollo11
# - columns: datetime, category, event
# - where: category is has less than 50 occurrences
# - use: CTE - Common Table Expression
# type: str
result = """

SELECT datetime, category, event
FROM apollo11
WHERE category IN (
    SELECT category
    FROM apollo11
    GROUP BY category
    HAVING COUNT(event) < 50
)

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)


# Solution
result = """

WITH important_categories AS (
    SELECT category
    FROM apollo11
    GROUP BY category
    HAVING COUNT(event) < 50
)

SELECT datetime, category, event
FROM apollo11
WHERE category IN important_categories

"""

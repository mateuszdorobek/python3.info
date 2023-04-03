"""
* Assignment: Model Data Iris
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    TODO: English translation

Polish:
    1. Użyj bazy danych `space.db`
       Pobieranie: https://python3.info/_static/space.db
    2. Użyj SQLAlchemy Core do wykonania zapytań
"""

# Solution

from sqlalchemy import create_engine
from sqlalchemy import text, select
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:////Users/matt/Developer/book-python/database/sqlalchemy/assignments/space.db')

Model = declarative_base()


query = text("""
    SELECT *
    FROM apollo11
""")


with engine.connect() as db:
    result = db.execute(query).all()
    print(result)

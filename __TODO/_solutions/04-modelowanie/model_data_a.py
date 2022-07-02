"""
* Assignment: Model Data Iris
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    TODO: English translation

Polish:
    1. Zamodeluj dane w `DATA`
        a. Jak nazywa się model?
        b. Jak nazywają się pola?
        c. Jakie typy mają pola?
    2. Użyj SQLAlchemy ORM do stworzenia modeli
    3. Wymagania niefunkcjonalne:
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów

TODO: Automated tests
"""

from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, Float, String


Model = MetaData()


DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa')]


flower = Table('flowers', Model,
    Column('id', Integer, primary_key=True),
    Column('sepal_length', Float),
    Column('sepal_width', Float),
    Column('petal_length', Float),
    Column('petal_width', Float),
    Column('species', String(20), index=True),
)

"""
* Assignment: JSON Object Factory
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Convert from JSON format to Python using decoder function
    2. Create instances of `Setosa`, `Virginica`, `Versicolor`
       classes based on value in field "species"
    3. Add instances to `result: list[Setosa|Virginica|Versicolor]`
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj dane z JSON do Python używając dekodera funkcyjnego
    2. Twórz obiekty klas `Setosa`, `Virginica`, `Versicolor`
       w zależności od wartości pola "species"
    3. Dodawaj instancje do `result: list[Setosa|Virginica|Versicolor]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `dict.pop()`
    * `globals()`
    * Assignment Expression

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result)
    >>> assert len(result) == 9

    >>> classes = (Setosa, Virginica, Versicolor)
    >>> assert all(type(row) in classes for row in result)

    >>> result[0]
    Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9)

    >>> result[1]
    Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2)
"""

import json
from dataclasses import dataclass

FILE = r'_temporary.json'

DATA = (
    '[{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_widt'
    'h":1.9,"species":"virginica"},{"sepal_length":5.1,"sepal_width":3.5,"'
    'petal_length":1.4,"petal_width":0.2,"species":"setosa"},{"sepal_lengt'
    'h":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"specie'
    's":"versicolor"},{"sepal_length":6.3,"sepal_width":2.9,"petal_length"'
    ':5.6,"petal_width":1.8,"species":"virginica"},{"sepal_length":6.4,"se'
    'pal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versic'
    'olor"},{"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"peta'
    'l_width":0.2,"species":"setosa"},{"sepal_length":7.0,"sepal_width":3.'
    '2,"petal_length":4.7,"petal_width":1.4,"species":"versicolor"},{"sepa'
    'l_length":7.6,"sepal_width":3.0,"petal_length":6.6,"petal_width":2.1,'
    '"species":"virginica"},{"sepal_length":4.9,"sepal_width":3.0,"petal_l'
    'ength":1.4,"petal_width":0.2,"species":"setosa"}]'
)

@dataclass
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass



# JSON decoded DATA
result = ...


# Solution
def decoder(obj: dict) -> dict:
    clsname = obj.pop('species').capitalize()
    cls = globals()[clsname]
    return cls(**obj)


result = json.loads(DATA, object_hook=decoder)

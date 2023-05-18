JSON String
===========


SetUp
-----
>>> import json


Mapping
-------
* ``json.dumps(DATA: dict) -> str`` - dict to JSON
* ``json.loads(DATA: str) -> dict`` - JSON to dict

Serialize mapping to JSON:

>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
... }
>>>
>>> result = json.dumps(DATA)
>>> print(result)
{"firstname": "Mark", "lastname": "Watney"}

Deserialize JSON to mapping:

>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney"
... }"""
>>>
>>> result = json.loads(DATA)
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney'}


List of Mappings to JSON
------------------------
* ``json.dumps(data: Iterable[dict]) -> str`` - list[dict] to JSON
* ``json.loads(data: str) -> list[dict]`` - JSON to list[dict]

Serialize list of mappings to JSON:

>>> DATA = [
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
...     {'firstname': 'Mark', 'lastname': 'Watney'},
... ]
>>>
>>> result = json.dumps(DATA)
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{"firstname": "Melissa", "lastname": "Lewis"},
 {"firstname": "Rick", "lastname": "Martinez"},
 {"firstname": "Mark", "lastname": "Watney"}]

Deserialize JSON to list of mappings:

>>> DATA = """[
...     {"firstname": "Melissa", "lastname": "Lewis"},
...     {"firstname": "Rick", "lastname": "Martinez"},
...     {"firstname": "Mark", "lastname": "Watney"}
... ]"""
>>>
>>> result = json.loads(DATA)
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]


List of Iterable
----------------
* ``json.dumps(data: list[Iterable]) -> str`` - list[Iterable] to JSON
* ``json.loads(data: str) -> list[list]`` - JSON to list[Iterable]

Serialize list of iterables to JSON:

>>> DATA = [
...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor')
... ]
>>>
>>> result = json.dumps(DATA)
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
 [5.8, 2.7, 5.1, 1.9, "virginica"],
 [5.1, 3.5, 1.4, 0.2, "setosa"],
 [5.7, 2.8, 4.1, 1.3, "versicolor"]]

Deserialize JSON to list of iterables:

>>> DATA = """[
...     ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
...     [5.8, 2.7, 5.1, 1.9, "virginica"],
...     [5.1, 3.5, 1.4, 0.2, "setosa"],
...     [5.7, 2.8, 4.1, 1.3, "versicolor"]
... ]"""
>>>
>>> result = json.loads(DATA)
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
 [5.8, 2.7, 5.1, 1.9, 'virginica'],
 [5.1, 3.5, 1.4, 0.2, 'setosa'],
 [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Assignments
-----------
.. literalinclude:: assignments/json_string_a.py
    :caption: :download:`Solution <assignments/json_string_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_string_b.py
    :caption: :download:`Solution <assignments/json_string_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_string_c.py
    :caption: :download:`Solution <assignments/json_string_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_string_d.py
    :caption: :download:`Solution <assignments/json_string_d.py>`
    :end-before: # Solution

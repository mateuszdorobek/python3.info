JSON File
=========
* ``json.load(file) -> dict``
* ``json.dump(data, file) -> None``
* file extension ``.json``


SetUp
-----
>>> import json


Write Data to JSON File
-----------------------
* ``json.dump(data, file) -> None``
* file extension ``.json``

.. code-block:: text

    def dump(obj: Any,
             fp: IO[str],
             *,
             skipkeys: bool = ...,
             ensure_ascii: bool = ...,
             check_circular: bool = ...,
             allow_nan: bool = ...,
             cls: Type[JSONEncoder] | None = ...,
             indent: None | int | str = ...,
             separators: tuple[str, str] | None = ...,
             default: (Any) -> Any | None = ...,
             sort_keys: bool = ...,
             **kwds: Any) -> None

SetUp:

>>> FILE = r'/tmp/myfile.json'
>>>
>>> DATA = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
... }

Usage:

>>> with open(FILE, mode='w') as file:
...     json.dump(DATA, file)

Result:

>>> print(open(FILE).read())
{"firstname": "Mark", "lastname": "Watney"}


Read Data From JSON File
------------------------
* ``json.load(file) -> dict``
* file extension ``.json``

.. code-block:: text

    def load(fp: SupportsRead[str | bytes],
             *,
             cls: Type[JSONDecoder] | None = ...,
             object_hook: (dict) -> Any | None = ...,
             parse_float: (str) -> Any | None = ...,
             parse_int: (str) -> Any | None = ...,
             parse_constant: (str) -> Any | None = ...,
             object_pairs_hook: (list[tuple[Any, Any]]) -> Any | None = ...,
             **kwds: Any) -> Any

SetUp:

>>> FILE = r'/tmp/myfile.json'
>>> DATA = """{
...     "firstname": "Mark",
...     "lastname": "Watney"
... }"""
>>>
>>> _ = open(FILE, mode='w').write(DATA)

Usage:

>>> with open(FILE) as file:
...     result = json.load(file)
>>>
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/json_file_a.py
    :caption: :download:`Solution <assignments/json_file_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_file_b.py
    :caption: :download:`Solution <assignments/json_file_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_file_c.py
    :caption: :download:`Solution <assignments/json_file_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_file_d.py
    :caption: :download:`Solution <assignments/json_file_d.py>`
    :end-before: # Solution

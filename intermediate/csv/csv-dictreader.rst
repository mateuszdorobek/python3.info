CSV DictReader
==============
* * Reads CSV file to list[dict]
* ``csv.DictReader()``


SetUp
-----
>>> import csv
>>> from pathlib import Path
>>> from pprint import pprint


Minimal
-------
Data:

.. code-block:: text

    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

SetUp:

>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

>>> with open('/tmp/myfile.csv') as file:
...     reader = csv.DictReader(file)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'sepal_length': '5.8',
  'sepal_width': '2.7',
  'petal_length': '5.1',
  'petal_width': '1.9',
  'species': 'virginica'},
 {'sepal_length': '5.1',
  'sepal_width': '3.5',
  'petal_length': '1.4',
  'petal_width': '0.2',
  'species': 'setosa'},
 {'sepal_length': '5.7',
  'sepal_width': '2.8',
  'petal_length': '4.1',
  'petal_width': '1.3',
  'species': 'versicolor'}]


Parametrized
------------
Data:

.. code-block:: text

    "sepal_length";"sepal_width";"petal_length";"petal_width";"species"
    "5.8";"2.7";"5.1";"1.9";"virginica"
    "5.1";"3.5";"1.4";"0.2";"setosa"
    "5.7";"2.8";"4.1";"1.3";"versicolor"

SetUp:

>>> DATA = '''"sepal_length";"sepal_width";"petal_length";"petal_width";"species"
... "5.8";"2.7";"5.1";"1.9";"virginica"
... "5.1";"3.5";"1.4";"0.2";"setosa"
... "5.7";"2.8";"4.1";"1.3";"versicolor"
... '''
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

>>> with open('/tmp/myfile.csv', mode='r', encoding='utf-8') as file:
...     reader = csv.DictReader(file, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'sepal_length': '5.8',
  'sepal_width': '2.7',
  'petal_length': '5.1',
  'petal_width': '1.9',
  'species': 'virginica'},
 {'sepal_length': '5.1',
  'sepal_width': '3.5',
  'petal_length': '1.4',
  'petal_width': '0.2',
  'species': 'setosa'},
 {'sepal_length': '5.7',
  'sepal_width': '2.8',
  'petal_length': '4.1',
  'petal_width': '1.3',
  'species': 'versicolor'}]


Custom Header
-------------
Read data from CSV file using ``csv.DictReader()``. While giving custom names
note, that first line (typically a header) will be treated like normal data.
Therefore we skip it using ``header = file.readline()``:

Data:

.. code-block:: text

    sl,sw,pl,pw,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

SetUp:

>>> DATA = """sl,sw,pl,pw,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

>>> FIELDNAMES = [
...     'sepal_length',
...     'sepal_width',
...     'petal_length',
...     'petal_width',
...     'species',
... ]
>>>
>>> with open('/tmp/myfile.csv') as file:
...     old_header = file.readline()  # skip the first line (old header)
...     reader = csv.DictReader(file, fieldnames=FIELDNAMES)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'sepal_length': '5.8',
  'sepal_width': '2.7',
  'petal_length': '5.1',
  'petal_width': '1.9',
  'species': 'virginica'},
 {'sepal_length': '5.1',
  'sepal_width': '3.5',
  'petal_length': '1.4',
  'petal_width': '0.2',
  'species': 'setosa'},
 {'sepal_length': '5.7',
  'sepal_width': '2.8',
  'petal_length': '4.1',
  'petal_width': '1.3',
  'species': 'versicolor'}]


Use Case - 0x01
---------------
.. code-block:: text

    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

>>> import csv
>>> from pathlib import Path
>>> from pprint import pprint
>>>
>>>
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)
>>>
>>>
>>> def clean(row: dict) -> dict:
...     return {
...         'sepal_length': float(row['sepal_length']),
...         'sepal_width': float(row['sepal_width']),
...         'petal_length': float(row['petal_length']),
...         'petal_width': float(row['petal_width']),
...         'species': row['species']
...     }
>>>
>>>
>>> with open('/tmp/myfile.csv') as file:
...     reader = csv.DictReader(file)
...     result = map(clean, reader)
...     result = list(result)
>>>
>>> pprint(result, sort_dicts=False)
[{'sepal_length': 5.8,
  'sepal_width': 2.7,
  'petal_length': 5.1,
  'petal_width': 1.9,
  'species': 'virginica'},
 {'sepal_length': 5.1,
  'sepal_width': 3.5,
  'petal_length': 1.4,
  'petal_width': 0.2,
  'species': 'setosa'},
 {'sepal_length': 5.7,
  'sepal_width': 2.8,
  'petal_length': 4.1,
  'petal_width': 1.3,
  'species': 'versicolor'}]


Assignments
-----------
.. literalinclude:: assignments/csv_dictreader_a.py
    :caption: :download:`Solution <assignments/csv_dictreader_a.py>`
    :end-before: # Solution

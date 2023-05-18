CSV Reader
==========
* Reads CSV file to list[list]
* ``csv.reader()``
* Default encoding is ``encoding='utf-8'``


SetUp
-----
>>> import csv
>>> from pprint import pprint
>>> from pathlib import Path


Minimal
-------
* Default mode is ``mode='r'``

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
...     reader = csv.reader(file)
...     result = list(reader)
>>>
>>>
>>> pprint(result)
[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
 ['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]


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
...     reader = csv.reader(file, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result = list(reader)
>>>
>>>
>>> pprint(result)
[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
 ['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]


Assignments
-----------
.. literalinclude:: assignments/csv_reader_a.py
    :caption: :download:`Solution <assignments/csv_reader_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_reader_b.py
    :caption: :download:`Solution <assignments/csv_reader_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_reader_c.py
    :caption: :download:`Solution <assignments/csv_reader_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_reader_d.py
    :caption: :download:`Solution <assignments/csv_reader_d.py>`
    :end-before: # Solution

CSV DictWriter
==============
* Writes iterable of dicts (eg. list[dict]) to CSV file
* ``csv.DictWriter()``
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``


SetUp
-----
>>> import csv
>>> from pathlib import Path


Minimal
----------
>>> DATA = [
...     {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
...     {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
...     {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
... ]
>>>
>>> header = DATA[0].keys()
>>>
>>> with open('/tmp/myfile.csv', mode='w') as file:
...     result = csv.DictWriter(file, fieldnames=header)
...     result.writeheader()
...     result.writerows(DATA)
59

Result:

>>> print(Path('/tmp/myfile.csv').read_text())
sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
<BLANKLINE>


Parametrized
------------
>>> DATA = [
...     {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
...     {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
...     {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
... ]
>>>
>>>
>>> header = DATA[0].keys()
>>>
>>> with open('/tmp/myfile.csv', mode='w', encoding='utf-8') as file:
...     result = csv.DictWriter(file, fieldnames=header, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result.writeheader()
...     result.writerows(DATA)
69

Result:

>>> print(Path('/tmp/myfile.csv').read_text())
"sepal_length";"sepal_width";"petal_length";"petal_width";"species"
"5.4";"3.9";"1.3";"0.4";"setosa"
"5.9";"3.0";"5.1";"1.8";"virginica"
"6.0";"3.4";"4.5";"1.6";"versicolor"
<BLANKLINE>


Assignments
-----------
.. literalinclude:: assignments/csv_dictwriter_a.py
    :caption: :download:`Solution <assignments/csv_dictwriter_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_dictwriter_b.py
    :caption: :download:`Solution <assignments/csv_dictwriter_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_dictwriter_c.py
    :caption: :download:`Solution <assignments/csv_dictwriter_c.py>`
    :end-before: # Solution

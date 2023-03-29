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
SetUp:

>>> DATA = """SepalLength,SepalWidth,PetalLength,PetalWidth,Species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

.. code-block:: text

    SepalLength,SepalWidth,PetalLength,PetalWidth,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

>>> with open('/tmp/myfile.csv') as file:
...     reader = csv.DictReader(file)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'SepalLength': '5.8',
  'SepalWidth': '2.7',
  'PetalLength': '5.1',
  'PetalWidth': '1.9',
  'Species': 'virginica'},
 {'SepalLength': '5.1',
  'SepalWidth': '3.5',
  'PetalLength': '1.4',
  'PetalWidth': '0.2',
  'Species': 'setosa'},
 {'SepalLength': '5.7',
  'SepalWidth': '2.8',
  'PetalLength': '4.1',
  'PetalWidth': '1.3',
  'Species': 'versicolor'}]


Parametrized
------------
SetUp:

>>> DATA = '''"SepalLength";"SepalWidth";"PetalLength";"PetalWidth";"Species"
... "5.8";"2.7";"5.1";"1.9";"virginica"
... "5.1";"3.5";"1.4";"0.2";"setosa"
... "5.7";"2.8";"4.1";"1.3";"versicolor"
... '''
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

.. code-block:: text

    "SepalLength";"SepalWidth";"PetalLength";"PetalWidth";"Species"
    "5.8";"2.7";"5.1";"1.9";"virginica"
    "5.1";"3.5";"1.4";"0.2";"setosa"
    "5.7";"2.8";"4.1";"1.3";"versicolor"

>>> with open('/tmp/myfile.csv', mode='r', encoding='utf-8') as file:
...     reader = csv.DictReader(file, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'SepalLength': '5.8',
  'SepalWidth': '2.7',
  'PetalLength': '5.1',
  'PetalWidth': '1.9',
  'Species': 'virginica'},
 {'SepalLength': '5.1',
  'SepalWidth': '3.5',
  'PetalLength': '1.4',
  'PetalWidth': '0.2',
  'Species': 'setosa'},
 {'SepalLength': '5.7',
  'SepalWidth': '2.8',
  'PetalLength': '4.1',
  'PetalWidth': '1.3',
  'Species': 'versicolor'}]

Custom Header
-------------
Read data from CSV file using ``csv.DictReader()``. While giving custom names
note, that first line (typically a header) will be treated like normal data.
Therefore we skip it using ``header = file.readline()``:

SetUp:

>>> DATA = """sl,sw,pl,pw,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

Usage:

.. code-block:: text

    sl,sw,pl,pw,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

>>> FIELDNAMES = [
...     'SepalLength',
...     'SepalWidth',
...     'PetalLength',
...     'PetalWidth',
...     'Species',
... ]
>>>
>>> with open('/tmp/myfile.csv') as file:
...     old_header = file.readline()  # skip the first line (old header)
...     reader = csv.DictReader(file, fieldnames=FIELDNAMES)
...     result = list(reader)
>>>
>>> pprint(result, sort_dicts=False)
[{'SepalLength': '5.8',
  'SepalWidth': '2.7',
  'PetalLength': '5.1',
  'PetalWidth': '1.9',
  'Species': 'virginica'},
 {'SepalLength': '5.1',
  'SepalWidth': '3.5',
  'PetalLength': '1.4',
  'PetalWidth': '0.2',
  'Species': 'setosa'},
 {'SepalLength': '5.7',
  'SepalWidth': '2.8',
  'PetalLength': '4.1',
  'PetalWidth': '1.3',
  'Species': 'versicolor'}]


Use Case - 0x01
---------------
>>> import csv
>>> from pathlib import Path
>>> from pprint import pprint
>>>
>>>
>>> DATA = """SepalLength,SepalWidth,PetalLength,PetalWidth,Species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... """
>>>
>>> _ = Path('/tmp/myfile.csv').write_text(DATA)

.. code-block:: text

    SepalLength,SepalWidth,PetalLength,PetalWidth,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

>>> def clean(row: dict) -> dict:
...     return {
...         'SepalLength': float(row['SepalLength']),
...         'SepalWidth': float(row['SepalWidth']),
...         'PetalLength': float(row['PetalLength']),
...         'PetalWidth': float(row['PetalWidth']),
...         'Species': row['Species']
...     }
>>>
>>>
>>> with open('/tmp/myfile.csv') as file:
...     reader = csv.DictReader(file)
...     result = map(clean, reader)
...     result = list(result)
>>>
>>> pprint(result, sort_dicts=False)
[{'SepalLength': 5.8,
  'SepalWidth': 2.7,
  'PetalLength': 5.1,
  'PetalWidth': 1.9,
  'Species': 'virginica'},
 {'SepalLength': 5.1,
  'SepalWidth': 3.5,
  'PetalLength': 1.4,
  'PetalWidth': 0.2,
  'Species': 'setosa'},
 {'SepalLength': 5.7,
  'SepalWidth': 2.8,
  'PetalLength': 4.1,
  'PetalWidth': 1.3,
  'Species': 'versicolor'}]


Assignments
-----------
.. literalinclude:: assignments/csv_dictreader_a.py
    :caption: :download:`Solution <assignments/csv_dictreader_a.py>`
    :end-before: # Solution

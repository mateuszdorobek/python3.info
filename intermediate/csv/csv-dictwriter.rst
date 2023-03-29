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
...     {'SepalLength': 5.4, 'SepalWidth': 3.9, 'PetalLength': 1.3, 'PetalWidth': 0.4, 'Species': 'setosa'},
...     {'SepalLength': 5.9, 'SepalWidth': 3.0, 'PetalLength': 5.1, 'PetalWidth': 1.8, 'Species': 'virginica'},
...     {'SepalLength': 6.0, 'SepalWidth': 3.4, 'PetalLength': 4.5, 'PetalWidth': 1.6, 'Species': 'versicolor'},
... ]
>>>
>>> header = DATA[0].keys()
>>>
>>> with open('/tmp/myfile.csv', mode='w') as file:
...     result = csv.DictWriter(file, fieldnames=header)
...     result.writeheader()
...     result.writerows(DATA)
55

Result:

>>> print(Path('/tmp/myfile.csv').read_text())
SepalLength,SepalWidth,PetalLength,PetalWidth,Species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
<BLANKLINE>


Parametrized
------------
>>> DATA = [
...     {'SepalLength': 5.4, 'SepalWidth': 3.9, 'PetalLength': 1.3, 'PetalWidth': 0.4, 'Species': 'setosa'},
...     {'SepalLength': 5.9, 'SepalWidth': 3.0, 'PetalLength': 5.1, 'PetalWidth': 1.8, 'Species': 'virginica'},
...     {'SepalLength': 6.0, 'SepalWidth': 3.4, 'PetalLength': 4.5, 'PetalWidth': 1.6, 'Species': 'versicolor'},
... ]
>>>
>>>
>>> header = DATA[0].keys()
>>>
>>> with open('/tmp/myfile.csv', mode='w', encoding='utf-8') as file:
...     result = csv.DictWriter(file, fieldnames=header, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result.writeheader()
...     result.writerows(DATA)
65

Result:

>>> print(Path('/tmp/myfile.csv').read_text())
"SepalLength";"SepalWidth";"PetalLength";"PetalWidth";"Species"
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

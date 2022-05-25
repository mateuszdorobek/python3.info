CSV DictWriter
==============
* csv.DictWriter: list[dict]


Conversion
----------
* list[tuple] to list[dict]

>>> DATA = [
...     ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> header, *rows = DATA
>>> result = []
>>>
>>> for row in rows:
...     pairs = zip(header, row)
...     result.append(dict(pairs))
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'SepalLength': 5.8, 'SepalWidth': 2.7, 'PetalLength': 5.1, 'PetalWidth': 1.9, 'Species': 'virginica'},
 {'SepalLength': 5.1, 'SepalWidth': 3.5, 'PetalLength': 1.4, 'PetalWidth': 0.2, 'Species': 'setosa'},
 {'SepalLength': 5.7, 'SepalWidth': 2.8, 'PetalLength': 4.1, 'PetalWidth': 1.3, 'Species': 'versicolor'}]


DictWriter
----------
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``

>>> import csv
>>>
>>> FILE = r'/tmp/myfile.csv'
>>>
>>> DATA = [{'Sepal Length': 5.4, 'Sepal Width': 3.9,
...          'Petal Length': 1.3, 'Petal Width': 0.4,
...          'Species': 'setosa'},
...
...         {'Sepal Length': 5.9, 'Sepal Width': 3.0,
...          'Petal Length': 5.1, 'Petal Width': 1.8,
...          'Species': 'virginica'},
...
...         {'Sepal Length': 6.0, 'Sepal Width': 3.4,
...          'Petal Length': 4.5, 'Petal Width': 1.6,
...          'Species': 'versicolor'}]
>>>
>>>
>>> header = DATA[0].keys()
>>>
>>> with open(FILE, mode='w') as file:
...     result = csv.DictWriter(file, fieldnames=header)
...     result.writeheader()
...     result.writerows(DATA)
59
>>>
>>> with open(FILE) as file:
...     print(file.read())
Sepal Length,Sepal Width,Petal Length,Petal Width,Species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
<BLANKLINE>

Write data to CSV file using ``csv.DictWriter()``:

>>> import csv
>>>
>>> FILE = r'/tmp/myfile.csv'
>>>
>>> DATA = [{'Sepal Length': 5.4, 'Sepal Width': 3.9,
...          'Petal Length': 1.3, 'Petal Width': 0.4,
...          'Species': 'setosa'},
...
...         {'Sepal Length': 5.9, 'Sepal Width': 3.0,
...          'Petal Length': 5.1, 'Petal Width': 1.8,
...          'Species': 'virginica'},
...
...         {'Sepal Length': 6.0, 'Sepal Width': 3.4,
...          'Petal Length': 4.5, 'Petal Width': 1.6,
...          'Species': 'versicolor'}]
>>>
>>> FIELDNAMES = ['Sepal Length', 'Sepal Width',
...               'Petal Length', 'Petal Width', 'Species']
>>>
>>> with open(FILE, mode='w', encoding='utf-8') as file:
...     result = csv.DictWriter(f=file,
...                             fieldnames=FIELDNAMES,
...                             delimiter=',',
...                             quotechar='"',
...                             quoting=csv.QUOTE_ALL,
...                             lineterminator='\n')
...
...     result.writeheader()
...     result.writerows(DATA)
68
>>>
>>> with open(FILE) as file:
...     print(file.read())
"Sepal Length","Sepal Width","Petal Length","Petal Width","Species"
"5.4","3.9","1.3","0.4","setosa"
"5.9","3.0","5.1","1.8","virginica"
"6.0","3.4","4.5","1.6","versicolor"
<BLANKLINE>


Recap
-----
* ``csv.DictWriter()`` writes `list[dict]`
* Schema and schemaless data
* ``fieldname`` parameter
* ``sorted(...)`` - sorts data
* ``set(...)`` - deduplicates data
* ``dict.keys()`` - get keys from ``dict``


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

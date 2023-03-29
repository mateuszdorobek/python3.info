CSV Writer
==========
* Writes iterable of iterables (eg. list[list], list[tuple]) to CSV file
* ``csv.writer()``
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``


SetUp
-----
>>> import csv


Minimal
-------
>>> DATA = [
...     ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>> with open('/tmp/myfile.csv', mode='w') as file:
...     result = csv.writer(file)
...     result.writerows(DATA)

Result:

>>> print(open('/tmp/myfile.csv').read())
SepalLength,SepalWidth,PetalLength,PetalWidth,Species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor
<BLANKLINE>


Parametrized
------------
>>> DATA = [
...     ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>> with open('/tmp/myfile.csv', mode='w', encoding='utf-8') as file:
...     result = csv.writer(file, quotechar='"', delimiter=';', quoting=csv.QUOTE_ALL)
...     result.writerows(DATA)

Result:

>>> print(open('/tmp/myfile.csv').read())
"SepalLength";"SepalWidth";"PetalLength";"PetalWidth";"Species"
"5.8";"2.7";"5.1";"1.9";"virginica"
"5.1";"3.5";"1.4";"0.2";"setosa"
"5.7";"2.8";"4.1";"1.3";"versicolor"
<BLANKLINE>


Assignments
-----------
.. literalinclude:: assignments/csv_writer_a.py
    :caption: :download:`Solution <assignments/csv_writer_a.py>`
    :end-before: # Solution

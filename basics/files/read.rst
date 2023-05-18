File Read
=========
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* Fails when file cannot be accessed
* Uses context manager
* ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='rt'``)


SetUp
-----
>>> from pathlib import Path
>>> Path('/tmp/myfile.txt').unlink(missing_ok=True)
>>> Path('/tmp/myfile.txt').touch()
>>>
>>>
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... 6.3,2.9,5.6,1.8,virginica
... 6.4,3.2,4.5,1.5,versicolor
... 4.7,3.2,1.3,0.2,setosa
... """
>>>
>>> with open('/tmp/myfile.txt', mode='w') as file:
...     _ = file.write(DATA)


Read From File
--------------
* Always remember to close file

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> file = open(FILE)
>>> data = file.read()
>>> file.close()


Read Using Context Manager
--------------------------
* Context managers use ``with ... as ...:`` syntax
* It closes file automatically upon block exit (dedent)
* Using context manager is best practice
* More information in `Protocol Context Manager`

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     data = file.read()


Read File at Once
-----------------
* Note, that whole file must fit into memory

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     data = file.read()


Read File as List of Lines
--------------------------
 * Note, that whole file must fit into memory

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     data = file.readlines()

Read selected (1-30) lines from file:

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     lines = file.readlines()[1:30]

Read selected (1-30) lines from file:

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     for line in file.readlines()[1:30]:
...         line = line.strip()

Read whole file and split by lines, separate header from content:

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> # doctest: +SKIP
... with open(FILE) as file:
...     header, *content = file.readlines()
...
...     for line in content:
...         line = line.strip()


Reading File as Generator
-------------------------
* Use generator to iterate over other lines
* In those examples, ``file`` is a generator

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     for line in file:
...         line = line.strip()

>>> FILE = r'/tmp/myfile.txt'
>>>
>>> with open(FILE) as file:
...     header = file.readline()
...
...     for line in file:
...         line = line.strip()


Examples
--------
>>> FILE = r'/tmp/myfile.txt'
... # sepal_length,sepal_width,petal_length,petal_width,species
... # 5.8,2.7,5.1,1.9,virginica
... # 5.1,3.5,1.4,0.2,setosa
... # 5.7,2.8,4.1,1.3,versicolor
... # 6.3,2.9,5.6,1.8,virginica
... # 6.4,3.2,4.5,1.5,versicolor
... # 4.7,3.2,1.3,0.2,setosa
>>>
>>>
>>> result = []
>>>
>>> with open(FILE) as file:
...     header = file.readline().strip().split(',')
...
...     for line in file:
...         *features,label = line.strip().split(',')
...         features = [float(x) for x in features]
...         row = features + [label]
...         pairs = zip(header, row)
...         result.append(dict(pairs))
>>>
>>> result
[{'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'}, {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'}, {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'}, {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'}, {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'}, {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'}]


StringIO
--------
>>> from io import StringIO
>>>
>>>
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... 6.3,2.9,5.6,1.8,virginica
... 6.4,3.2,4.5,1.5,versicolor
... 4.7,3.2,1.3,0.2,setosa
... """
>>>
>>>
>>> with StringIO(DATA) as file:
...     result = file.readline()
...
>>> result
'sepal_length,sepal_width,petal_length,petal_width,species\n'

>>> from io import StringIO
>>>
>>>
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.8,2.7,5.1,1.9,virginica
... 5.1,3.5,1.4,0.2,setosa
... 5.7,2.8,4.1,1.3,versicolor
... 6.3,2.9,5.6,1.8,virginica
... 6.4,3.2,4.5,1.5,versicolor
... 4.7,3.2,1.3,0.2,setosa
... """
>>>
>>>
>>> file = StringIO(DATA)
>>>
>>> file.read(50)
'sepal_length,sepal_width,petal_length,petal_width,'
>>> file.seek(0)
0
>>> file.readline()
'sepal_length,sepal_width,petal_length,petal_width,species\n'
>>> file.close()


Use Case - 0x01
---------------
>>> DATA = """A,B,C,red,green,blue
... 1,2,3,0
... 4,5,6,1
... 7,8,9,2"""
>>>
>>> header, *lines = DATA.splitlines()
>>> colors = header.strip().split(',')[3:]
>>> colors = dict(enumerate(colors))
>>> result = []
>>>
>>> for line in lines:
...     line = line.strip().split(',')
...     *numbers, color = map(int, line)
...     line = numbers + [colors.get(color)]
...     result.append(tuple(line))


Assignments
-----------
.. literalinclude:: assignments/file_read_a.py
    :caption: :download:`Solution <assignments/file_read_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_b.py
    :caption: :download:`Solution <assignments/file_read_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_c.py
    :caption: :download:`Solution <assignments/file_read_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_d.py
    :caption: :download:`Solution <assignments/file_read_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_e.py
    :caption: :download:`Solution <assignments/file_read_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_f.py
    :caption: :download:`Solution <assignments/file_read_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_g.py
    :caption: :download:`Solution <assignments/file_read_g.py>`
    :end-before: # Solution

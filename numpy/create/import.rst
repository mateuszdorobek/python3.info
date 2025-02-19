Array Import
============



SetUp
-----
>>> import numpy as np


np.loadtxt()
------------
>>> DATA = 'https://python3.info/_static/iris.csv'

>>> a = np.loadtxt(DATA)
Traceback (most recent call last):
ValueError: could not convert string 'sepal_length,sepal_width,petal_length,petal_width,species' to float64 at row 0, column 1.

>>> a = np.loadtxt(DATA, skiprows=1)
Traceback (most recent call last):
ValueError: could not convert string '5.4,3.9,1.3,0.4,setosa' to float64 at row 0, column 1.

>>> a = np.loadtxt(DATA, skiprows=1, delimiter=',')
Traceback (most recent call last):
ValueError: could not convert string 'setosa' to float64 at row 0, column 5.

>>> a = np.loadtxt(DATA, skiprows=1, delimiter=',', max_rows=5, usecols=(0,1,2,3))
>>> a
array([[5.4, 3.9, 1.3, 0.4],
       [5.9, 3. , 5.1, 1.8],
       [6. , 3.4, 4.5, 1.6],
       [7.3, 2.9, 6.3, 1.8],
       [5.6, 2.5, 3.9, 1.1]])

>>> header = np.loadtxt(DATA, max_rows=1, delimiter=',', dtype=str, usecols=(0,1,2,3))
>>> data = np.loadtxt(DATA, skiprows=1, max_rows=3, delimiter=',', usecols=(0,1,2,3))
>>>
>>> header  # doctest: +NORMALIZE_WHITESPACE
array(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], dtype='<U12')
>>>
>>> data
array([[5.4, 3.9, 1.3, 0.4],
       [5.9, 3. , 5.1, 1.8],
       [6. , 3.4, 4.5, 1.6]])


Other
-----
.. csv-table:: NumPy Import methods
    :header: "Method", "Data Type", "Description"
    :widths: 15, 5, 85

    ``np.loadtxt()``, "Text", "Load data from text file such as ``.csv``"
    ``np.load()``, "Binary", "Load data from ``.npy`` file"
    ``np.loads()``, "Binary", "Load binary data from ``pickle`` string"
    ``np.fromstring()``, "Text", "Load data from string"
    ``np.fromregex()``, "Text", "Load data from file using regex to parse"
    ``np.genfromtxt()``, "Text", "Load data with missing values handled as specified"
    ``scipy.io.loadmat()``, "Binary", "reads MATLAB data files"

>>> # doctest: +SKIP
... data = np.loadtxt('myfile.csv', delimiter=',', usecols=1, skiprows=1, dtype=np.float16)
...
... small = (data < 1)
... medium = (data < 1) & (data < 2.0)
... large = (data < 2)
...
... np.save('/tmp/small', data[small])
... np.save('/tmp/medium', data[medium])
... np.save('/tmp/large', data[large])


Use Case - 0x01
---------------
>>> header = np.loadtxt(DATA, max_rows=1, dtype='str', delimiter=',', usecols=(0,1,2,3))
>>> values = np.loadtxt(DATA, skiprows=1, dtype='float', delimiter=',', usecols=(0,1,2,3))
>>> species = np.loadtxt(DATA, skiprows=1, dtype='str', delimiter=',', usecols=4)
>>>
>>> sepal_length = (header == 'sepal_length')
>>> sepal_width = (header == 'sepal_width')
>>> petal_length = (header == 'petal_length')
>>> petal_width = (header == 'petal_width')
>>>
>>> setosa = (species == 'setosa')
>>> versicolor = (species == 'versicolor')
>>> virginica = (species == 'virginica')

Then you can query your data using previously defined identifiers (queries):

>>> values[setosa, sepal_length]
array([5.4, 5.4, 4.9, 5.1, 4.6, 5.2, 5.2, 5.1, 4.8, 4.9, 4.3, 5. , 5.4,
       5.1, 4.8, 4.8, 4.4, 5.1, 4.6, 5.5, 5. , 5.7, 5.4, 4.8, 5. , 5.1,
       4.9, 5. , 4.6, 4.9, 5.1, 4.7, 5.7, 4.4, 5.4, 4.5, 5. , 5.3, 5.1,
       5. , 5.8, 5.2, 4.6, 4.8, 4.4, 5.4, 5. , 4.7, 5.1, 5.5, 5. ])

>>> values[setosa, sepal_length].mean()
5.013725490196078

>>> values[setosa, sepal_length].mean().round(2)
5.01


Assignments
-----------
.. literalinclude:: assignments/numpy_importexport_a.py
    :caption: :download:`Solution <assignments/numpy_importexport_a.py>`
    :end-before: # Solution

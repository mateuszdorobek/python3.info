Pandas Read CSV
===============
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd
>>>
>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)


Header
------
>>> DATA = 'https://python3.info/_static/iris-clean.csv'
>>>
>>> header = pd.read_csv(DATA, nrows=0).columns

Label Encoder:

>>> DATA = 'https://python3.info/_static/iris-clean.csv'
>>>
>>> class_labels = pd.read_csv(DATA, nrows=0).columns[2:]
>>> label_encoder = dict(enumerate(class_labels))


Content
-------
>>> DATA = 'https://python3.info/_static/iris-clean.csv'
>>>
>>> df = pd.read_csv(DATA)
>>> df.head(3)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor


Rename Columns
--------------
>>> DATA = 'https://python3.info/_static/iris-dirty.csv'
>>>
>>> COLUMNS =  ['sepal_length', 'sepal_width',
...             'petal_length', 'petal_width', 'species']
>>>
>>> df = pd.read_csv(DATA)
>>> df.head(3)
   150    4  setosa  versicolor  virginica
0  5.4  3.9     1.3         0.4          0
1  5.9  3.0     5.1         1.8          2
2  6.0  3.4     4.5         1.6          1
>>>
>>> df = pd.read_csv(DATA, skiprows=1, names=COLUMNS)
>>> df.head(3)
   sepal_length  sepal_width  petal_length  petal_width  species
0           5.4          3.9           1.3          0.4        0
1           5.9          3.0           5.1          1.8        2
2           6.0          3.4           4.5          1.6        1
>>>
>>> df['species'].replace({
...     0: 'setosa',
...     1: 'versicolor',
...     2: 'virginica',
... }, inplace=True)
>>>
>>> df.head(n=3)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``,
  the corresponding compression method is automatically selected

>>> df = pd.read_csv('sample_file.zip', compression='zip')  # doctest: +SKIP
>>> df = pd.read_csv('sample_file.gz', compression='infer')  # doctest: +SKIP


Use Case - 0x01
---------------
>>> DATA = 'https://python3.info/_static/iris-dirty.csv'
>>>
>>> COLUMNS =  ['sepal_length', 'sepal_width',
...             'petal_length', 'petal_width', 'species']

>>> header = pd.read_csv(DATA, nrows=0)
>>> nrows, ncols, *class_labels = header.columns
>>> label_encoder = dict(enumerate(class_labels))
>>>
>>> label_encoder
{0: 'setosa', 1: 'versicolor', 2: 'virginica'}

>>> df = pd.read_csv(DATA, names=COLUMNS, skiprows=1)
>>> df['species'].replace(label_encoder, inplace=True)
>>> df.head(n=5)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor
3           7.3          2.9           6.3          1.8   virginica
4           5.6          2.5           3.9          1.1  versicolor


Use Case - 0x02
---------------
>>> DATA = 'https://python3.info/_static/martian-en.csv'

>>> pd.read_csv(DATA)
  firstname   lastname              born  gender          ssn                email               phone
0      Mark     Watney   October 12 1994    male  94101212345     mwatney@nasa.gov   +1 (234) 555-0000
1   Melissa      Lewis      July 15 1995  female  95071512345      mlewis@nasa.gov   +1 (234) 555-0001
2      Rick   Martinez   January 21 1996    male  96012112345   rmartinez@nasa.gov   +1 (234) 555-0010
3      Alex      Vogel  November 15 1994    male  94111512345       avogel@esa.int  +49 (234) 555-0011
4      Beth  Johanssen        May 9 2006  female   6250912345  bjohanssen@nasa.gov   +1 (234) 555-0100
5     Chris       Beck     August 2 1999    male  99080212345       cbeck@nasa.gov   +1 (234) 555-0101

>>> pd.read_csv(DATA, parse_dates=['born'])
  firstname   lastname       born  gender          ssn                email               phone
0      Mark     Watney 1994-10-12    male  94101212345     mwatney@nasa.gov   +1 (234) 555-0000
1   Melissa      Lewis 1995-07-15  female  95071512345      mlewis@nasa.gov   +1 (234) 555-0001
2      Rick   Martinez 1996-01-21    male  96012112345   rmartinez@nasa.gov   +1 (234) 555-0010
3      Alex      Vogel 1994-11-15    male  94111512345       avogel@esa.int  +49 (234) 555-0011
4      Beth  Johanssen 2006-05-09  female   6250912345  bjohanssen@nasa.gov   +1 (234) 555-0100
5     Chris       Beck 1999-08-02    male  99080212345       cbeck@nasa.gov   +1 (234) 555-0101



Assignments
-----------
.. literalinclude:: assignments/pandas_readcsv_a.py
    :caption: :download:`Solution <assignments/pandas_readcsv_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_readcsv_b.py
    :caption: :download:`Solution <assignments/pandas_readcsv_b.py>`
    :end-before: # Solution

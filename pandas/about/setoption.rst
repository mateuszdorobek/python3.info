About Options
=============
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html


SetUp
-----
>>> import pandas as pd
>>> df = pd.DataFrame()


Display Output
--------------
Limited:

>>> pd.set_option('display.max_rows', 50)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.width', 1000)

Unlimited:

>>> pd.set_option('display.max_rows', None)
>>> pd.set_option('display.max_columns', None)
>>> pd.set_option('display.width', None)


Using in context
----------------
>>> with pd.option_context('display.max_rows', 100):
...     print(df)
Empty DataFrame
Columns: []
Index: []

>>> with pd.option_context('display.max_rows', 50, 'display.max_columns', 10):
...     print(df)
Empty DataFrame
Columns: []
Index: []


Memory Usage
------------
display.memory_usage : bool, string or None
    This specifies if the memory usage of a DataFrame should be displayed when df.info() is called. Valid values True,False,'deep' [default: True] [currently: True]

Precision
---------
display.precision : int
    Floating point output precision in terms of number of places after the decimal, for regular formatting as well as scientific notation. Similar to precision in numpy.set_printoptions(). [default: 6] [currently: 6]


.. todo:: Assignments

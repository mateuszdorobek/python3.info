DataFrame Query
===============


Important
---------
>>> # doctest: +SKIP
... df[df['sales'] > 50000]
... df.query('sales > 50000')

.. figure:: img/pandas-dataframe-query.png

    Pandas query expression [#sharpsightlabs]_


SetUp
-----
>>> import pandas as pd
>>>
>>>
>>> df = pd.DataFrame({
...     'name': ['William','Emma','Sofia','Markus','Edward','Thomas','Ethan','Olivia','Arun','Anika','Paulo'],
...     'region': ['East','North','East','South','West','West','South','West','West','East','South'],
...     'sales': [50000,52000,90000,34000,42000,72000,49000,55000,67000,65000,67000],
...     'expenses': [42000,43000,50000,44000,38000,39000,42000,60000,39000,44000,45000]})
>>>
>>> df
       name region  sales  expenses
0   William   East  50000     42000
1      Emma  North  52000     43000
2     Sofia   East  90000     50000
3    Markus  South  34000     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan  South  49000     42000
7    Olivia   West  55000     60000
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000


Query Data
----------
Subset a pandas dataframe based on a numeric variable:

>>> df.query('sales > 60000')
      name region  sales  expenses
2    Sofia   East  90000     50000
5   Thomas   West  72000     39000
8     Arun   West  67000     39000
9    Anika   East  65000     44000
10   Paulo  South  67000     45000

Select rows based on a categorical variable:

>>> df.query('region == "East"')
      name region  sales  expenses
0  William   East  50000     42000
2    Sofia   East  90000     50000
9    Anika   East  65000     44000

Subset a pandas dataframe with multiple conditions:

>>> df.query('(sales > 50000) and (region in ["East", "West"])')
     name region  sales  expenses
2   Sofia   East  90000     50000
5  Thomas   West  72000     39000
7  Olivia   West  55000     60000
8    Arun   West  67000     39000
9   Anika   East  65000     44000


Query Index
-----------
* Works also with Time Series

Subset a dataframe by index:

>>> df.query('index < 3')
      name region  sales  expenses
0  William   East  50000     42000
1     Emma  North  52000     43000
2    Sofia   East  90000     50000

Every odd index:

>>> df.query('index%2 == 1')
     name region  sales  expenses
1    Emma  North  52000     43000
3  Markus  South  34000     44000
5  Thomas   West  72000     39000
7  Olivia   West  55000     60000
9   Anika   East  65000     44000


Query Columns
-------------
Subset a pandas dataframe by comparing two columns:

>>> df.query('sales < expenses')
     name region  sales  expenses
3  Markus  South  34000     44000
7  Olivia   West  55000     60000


Query Variable
--------------
Reference local variables inside of query:

>>> mean = df['sales'].mean()
>>> mean
58454.545454545456
>>>
>>> df.query('sales > @mean')
      name region  sales  expenses
2    Sofia   East  90000     50000
5   Thomas   West  72000     39000
8     Arun   West  67000     39000
9    Anika   East  65000     44000
10   Paulo  South  67000     45000

>>> regions = ['East','North',]
>>> df.query('region in @regions')
      name region  sales  expenses
0  William   East  50000     42000
1     Emma  North  52000     43000
2    Sofia   East  90000     50000
9    Anika   East  65000     44000


Query Save
----------
Modify a dataframe in place:

>>> df2 = df.copy()
>>> df2.query('index < 5', inplace=True)
>>>
>>> df2
      name region  sales  expenses
0  William   East  50000     42000
1     Emma  North  52000     43000
2    Sofia   East  90000     50000
3   Markus  South  34000     44000
4   Edward   West  42000     38000


References
----------
.. [#sharpsightlabs] https://www.sharpsightlabs.com/blog/pandas-query/

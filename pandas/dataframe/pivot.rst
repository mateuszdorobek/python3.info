DataFrame Pivot
===============
* Create a spreadsheet-style pivot table as a DataFrame
* Levels in the pivot table will be stored in MultiIndex objects

Create a spreadsheet-style pivot table as a DataFrame.
The levels in the pivot table will be stored in MultiIndex objects
(hierarchical indexes) on the index and columns of the result DataFrame.


Parameters
----------
values : column to aggregate, optional

index : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The
    list can contain any of the other types (except list).
    Keys to group by on the pivot table index.  If an array is passed,
    it is being used as the same manner as column values.

columns : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The
    list can contain any of the other types (except list).
    Keys to group by on the pivot table column.  If an array is passed,
    it is being used as the same manner as column values.

aggfunc : function, list of functions, dict, default numpy.mean
    If list of functions passed, the resulting pivot table will have
    hierarchical columns whose top level are the function names
    (inferred from the function objects themselves)
    If dict is passed, the key is column to aggregate and value
    is function or list of functions.

fill_value : scalar, default None
    Value to replace missing values with (in the resulting pivot table,
    after aggregation).

margins : bool, default False
    Add all row / columns (e.g. for subtotal / grand totals).

dropna : bool, default True
    Do not include columns whose entries are all NaN.

margins_name : str, default 'All'
    Name of the row / column that will contain the totals
    when margins is True.

observed : bool, default False
    This only applies if any of the groupers are Categoricals.
    If True: only show observed values for categorical groupers.
    If False: show all values for categorical groupers.

sort : bool, default True
    Specifies if the result should be sorted.


Returns
-------
DataFrame
    An Excel style pivot table.


See Also
--------
DataFrame.pivot
    Pivot without aggregation that can handle
    non-numeric data.

DataFrame.melt
    Unpivot a DataFrame from wide to long format,
    optionally leaving identifiers set.

wide_to_long
    Wide panel to long format. Less flexible but more
    user-friendly than melt.


SetUp
-----
>>> import pandas as pd
>>> import numpy as np

>>> df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
...                          "bar", "bar", "bar", "bar"],
...                    "B": ["one", "one", "one", "two", "two",
...                          "one", "one", "two", "two"],
...                    "C": ["small", "large", "large", "small",
...                          "small", "large", "small", "small",
...                          "large"],
...                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
...                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

>>> df
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9


Use Case - 0x01
---------------
This first example aggregates values by taking the sum.

>>> result = pd.pivot_table(data=df,
...                         values='D',
...                         index=['A', 'B'],
...                         columns=['C'],
...                         aggfunc=np.sum)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
C        large  small
A   B
bar one    4.0    5.0
    two    7.0    6.0
foo one    4.0    1.0
    two    NaN    6.0


Use Case - 0x02
---------------
We can also fill missing values using the `fill_value` parameter.

>>> result = pd.pivot_table(data=df,
...                         values='D',
...                         index=['A', 'B'],
...                         columns=['C'],
...                         aggfunc=np.sum,
...                         fill_value=0)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
C        large  small
A   B
bar one      4      5
    two      7      6
foo one      4      1
    two      0      6


Use Case - 0x03
---------------
The next example aggregates by taking the mean across multiple columns.

>>> result = pd.pivot_table(data=df,
...                         values=['D', 'E'],
...                         index=['A', 'C'],
...                         aggfunc={'D': np.mean, 'E': np.mean})
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
                  D         E
A   C
bar large  5.500000  7.500000
    small  5.500000  8.500000
foo large  2.000000  4.500000
    small  2.333333  4.333333


Use Case - 0x04
---------------
We can also calculate multiple types of aggregations for any given
value column.

>>> result = pd.pivot_table(data=df,
...                         values=['D', 'E'],
...                         index=['A', 'C'],
...                         aggfunc={'D': np.mean, 'E': [min, max, np.mean]})
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
                  D   E
               mean max      mean min
A   C
bar large  5.500000   9  7.500000   6
    small  5.500000   9  8.500000   8
foo large  2.000000   5  4.500000   4
    small  2.333333   6  4.333333   2

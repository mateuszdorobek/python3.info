DataFrame Update
================
* ``df['column'] = 0``
* ``df[1:2] = 0``
* ``.loc[df['species'] == 0, 'species'] = 'Setosa'``
* ``.replace()``
* ``.eval()``


Update Column
-------------
>>> import pandas as pd
>>>
>>>
>>> df = pd.DataFrame({
...     'A': [10, 11, 12],
...     'B': [20, 21, 22],
...     'C': [30, 31, 32]})
>>>
>>> df
    A   B   C
0  10  20  30
1  11  21  31
2  12  22  32
>>>
>>> df['C'] = 0
>>> df
    A   B  C
0  10  20  0
1  11  21  0
2  12  22  0


Update Row
----------
>>> import pandas as pd
>>>
>>>
>>> df = pd.DataFrame({
...     'A': [10, 11, 12],
...     'B': [20, 21, 22],
...     'C': [30, 31, 32]})
>>>
>>> df
    A   B   C
0  10  20  30
1  11  21  31
2  12  22  32
>>>
>>> df[1:2] = 0
>>> df
    A   B   C
0  10  20  30
1   0   0   0
2  12  22  32
>>>
>>> df[::2] = 99
>>> df
    A   B   C
0  99  99  99
1   0   0   0
2  99  99  99


Use Case - 0x01
---------------
>>> # doctest: +SKIP
... df.loc[df['species'] == 0, 'species'] = 'Setosa'
... df.loc[df['species'] == 1, 'species'] = 'Versicolor'
... df.loc[df['species'] == 2, 'species'] = 'Virginica'


Use Case - 0x02
---------------
>>> # doctest: +SKIP
... df['species'].replace({
...     0: 'setosa',
...     1: 'versicolor',
...     2: 'virginica'
... }, inplace=True)


.. todo:: Assignments

Advanced Indexing
=================


Indexing
--------
* two types of indexes: int, bool
* Also known as Fancy indexing

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a > 2
array([[False, False,  True],
       [ True,  True,  True]])
>>>
>>> a[a > 2]
array([3, 4, 5, 6])
>>>
>>> a[a > a.mean()]
array([4, 5, 6])
>>>
>>> a[a >= a.mean()+1]
array([5, 6])


>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[a % 2 == 0]
array([2, 4, 6])
>>>
>>> even = (a % 2 == 0)
>>> a[even]
array([2, 4, 6])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[ (a>2) & (a<=5) & (a%2==1) ]
array([3, 5])
>>>
>>> query1 = (a > 2)
>>> query2 = (a <= 5)
>>> query3 = (a % 2 == 1)
>>> a[query1 & query2 & query3]
array([3, 5])
>>>
>>> large = (a > 2)
>>> small = (a <= 5)
>>> odd = (a % 2 == 1)
>>> a[large & small & odd]
array([3, 5])

>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
>>>
>>> at_index = np.array([0, 1, 0])
>>> a[at_index]
array([1, 2, 1])
>>>
>>> at_index = np.array([0, 2])
>>> a[at_index]
array([1, 3])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[[0,2]]
array([[1, 2, 3],
       [7, 8, 9]])
>>>
>>> a[[0,2], [1,2]]
array([2, 9])
>>>
>>> a[:2, [1,2]]
array([[2, 3],
       [5, 6]])

``rows,cols`` creates coordinate system for selecting values (like ``zip()``). For example: ``(0,0); (0,1); (1,0); (1,1); (0,1)``, as in this example:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 4], [9, 16]], float)
>>>
>>> rows = np.array([0, 0, 1, 1, 0], int)
>>> cols = np.array([0, 1, 0, 1, 1], int)
>>>
>>> a[rows]
array([[ 1.,  4.],
       [ 1.,  4.],
       [ 9., 16.],
       [ 9., 16.],
       [ 1.,  4.]])
>>>
>>> a[rows,cols]
array([ 1.,  4.,  9., 16.,  4.])


Use Case - 0x01
---------------
>>> import numpy as np
>>>
>>> # '2000-01-01' -> [1, 2, 3]
>>> # '2000-01-02' -> [4, 5, 6]
>>> # '2000-01-03' -> [7, 8, 9]
>>>
>>> date = np.array([
...     '2000-01-01',
...     '2000-01-02',
...     '2000-01-03'])
>>>
>>> values = np.array([[1, 2, 3],
...                    [4, 5, 6],
...                    [7, 8, 9]])
>>>
>>>
>>> date == '2000-01-02'
array([False,  True, False])
>>>
>>> values[date == '2000-01-02']
array([[4, 5, 6]])
>>>
>>> values[date != '2000-01-02']
array([[1, 2, 3],
       [7, 8, 9]])
>>>
>>> values[ (date=='2000-01-01') | (date=='2000-01-03') ]
array([[1, 2, 3],
       [7, 8, 9]])


Use Case - 0x02
---------------
>>> import numpy as np
>>>
>>>
>>> index = np.array([
...     '2000-01-01',
...     '2000-01-02',
...     '2000-01-03'])
>>>
>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> jan01 = (index == '2000-01-01')
>>> jan03 = (index == '2000-01-03')
>>>
>>> data[jan01|jan03]
array([[1, 2, 3],
       [7, 8, 9]])
>>>
>>> data[jan01|jan03, 0]
array([1, 7])
>>>
>>> data[jan01|jan03, :2]
array([[1, 2],
       [7, 8]])
>>>
>>> data[jan01|jan03, :2] = 0
>>> data
array([[0, 0, 3],
       [4, 5, 6],
       [0, 0, 9]])


Use Case - 0x03
---------------
>>> import numpy as np
>>>
>>> #                Morning         Noon      Evening
>>> # 1999-12-30  1.76405235,  0.40015721,  0.97873798,
>>> # 1999-12-31  2.2408932 ,  1.86755799, -0.97727788,
>>> # 2000-01-01  0.95008842, -0.15135721, -0.10321885,
>>> # 2000-01-02  0.4105985 ,  0.14404357,  1.45427351,
>>>
>>> index = np.array([
...     '1999-12-30',
...     '1999-12-31',
...     '2000-01-01',
...     '2000-01-02'])
>>>
>>> columns = np.array(['Morning', 'Noon', 'Evening'])
>>>
>>> data = np.array([[ 1.76405235,  0.40015721,  0.97873798],
...                  [ 2.2408932 ,  1.86755799, -0.97727788],
...                  [ 0.95008842, -0.15135721, -0.10321885],
...                  [ 0.4105985 ,  0.14404357,  1.45427351]])
>>>
>>> dec31 = (index == '1999-12-31')   # array([False,  True, False, False])
>>> jan01 = (index == '2000-01-01')   # array([False, False,  True, False])
>>> morning = (columns == 'Morning')  # array([ True, False, False])
>>>
>>> data[dec31|jan01]
array([[ 2.2408932 ,  1.86755799, -0.97727788],
       [ 0.95008842, -0.15135721, -0.10321885]])
>>>
>>> data[dec31|jan01, (columns == 'Morning')]
array([2.2408932 , 0.95008842])
>>>
>>> data[dec31|jan01, morning]
array([2.2408932 , 0.95008842])


Diagonal problem
----------------
* .. warning:: Without the ``np.ix_`` call, only the diagonal elements would be selected. This difference is the most important thing to remember about indexing with multiple advanced indexes.

>>> import numpy as np
>>>
>>> #                Morning         Noon      Evening
>>> # 1999-12-30  1.76405235,  0.40015721,  0.97873798,
>>> # 1999-12-31  2.2408932 ,  1.86755799, -0.97727788,
>>> # 2000-01-01  0.95008842, -0.15135721, -0.10321885,
>>> # 2000-01-02  0.4105985 ,  0.14404357,  1.45427351,
>>>
>>> index = np.array([
...     '1999-12-30',
...     '1999-12-31',
...     '2000-01-01',
...     '2000-01-02'])
>>>
>>> columns = np.array(['Morning', 'Noon', 'Evening'])
>>>
>>> data = np.array([[ 1.76405235,  0.40015721,  0.97873798],
...                  [ 2.2408932 ,  1.86755799, -0.97727788],
...                  [ 0.95008842, -0.15135721, -0.10321885],
...                  [ 0.4105985 ,  0.14404357,  1.45427351]])
>>>
>>> dec31 = (index == '1999-12-31')     # array([False,  True, False, False])
>>> jan01 = (index == '2000-01-01')     # array([False, False,  True, False])
>>> morning = (columns == 'Morning')    # array([ True, False, False])
>>> evening = (columns == 'Evening')    # array([False, False,  True])
>>>
>>> data[dec31|jan01]
array([[ 2.2408932 ,  1.86755799, -0.97727788],
       [ 0.95008842, -0.15135721, -0.10321885]])
>>>
>>> data[(dec31|jan01), (morning|evening)]
array([ 2.2408932 , -0.10321885])
>>>
>>> data[np.ix_((dec31|jan01), (morning|evening))]
array([[ 2.2408932 , -0.97727788],
       [ 0.95008842, -0.10321885]])

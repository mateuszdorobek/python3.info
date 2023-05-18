Mapping Nested
==============


List of Dicts
-------------
>>> data = [
...     {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
...     {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
...     {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
...     {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
...     {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
...     {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
... ]

>>> data = [
...     {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
...     {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
...     {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
... ]

>>> data = [
...     {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
...     {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
...     {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
... ]


Mixed
-----
>>> data = {
...     'date': '1969-07-21',
...     'age': 42,
...     'astronaut': {'name': 'Mark Watney', 'medals': {'Medal of Honor', 'Purple Heart'}},
...     'agency': ['NASA', 'ESA', 'POLSA'],
...     'location': ('Baikonur', 'Johnson Space Center'),
... }


GetItem
-------
>>> data = [
...     {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
...     {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
...     {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
... ]
>>>
>>>
>>> data[0]
{'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'}
>>>
>>> data[0]['measurements']
[4.7, 3.2, 1.3, 0.2]
>>>
>>> data[0]['measurements'][2]
1.3
>>>
>>> data[0]['species']
'setosa'
>>>


Get Method
----------
>>> data = [
...     {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
...     {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
...     {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
... ]
>>>
>>>
>>> data[0].get('kind')
>>>
>>> data[0].get('kind', 'n/a')
'n/a'
>>>
>>> data[2].get('measurements')
[7.6, 3.0, 6.6, 2.1]
>>>
>>> data[2].get('measurements')[1]
3.0


Length
------
>>> data = [
...     {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
...     {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
...     {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
... ]
>>>
>>>
>>> len(data)
3
>>>
>>> len(data[0])
2
>>>
>>> len(data[1])
2
>>>
>>> len(data[1]['species'])
10
>>>
>>> len(data[1]['measurements'])
4


.. todo:: Assignments

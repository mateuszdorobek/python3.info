FuncProg First-class Functions
==============================
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...
* Function can be returned
* Function can be user as a parameter


Assigning Functions
-------------------
* Function can be assigned to variable

>>> def addition(a, b):
...     return a + b
>>>
>>>
>>> add = addition
>>>
>>> add(1,2)
3
>>>
>>> add(3,4)
7


Storing Functions
-----------------
* Function can be stored in data structures such as hash tables, lists, ...

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = (cube, square)

>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> operations = {
...     'cube': cube,
...     'square': square,
...     'root': lambda x: x ** (1/2)
... }

>>> def increment(x):
...     return x + 1
>>>
>>> def decrement(x):
...     return x - 1
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3
>>>
>>>
>>> data = [1,2,3,4]
>>> operations = [increment, square, decrement, cube]
>>>
>>> for operation in operations:
...     data = list(map(operation, data))
>>>
>>> data
[27, 512, 3375, 13824]


Returning Functions
-------------------
* Function can be returned

>>> def get_greeting(lang='English'):
...
...     def english(firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
...
...     def polish(firstname, lastname):
...         print(f'Witaj {firstname} {lastname}')
...
...     match lang:
...         case 'English': return english
...         case 'Polish':  return polish
...         case _:         raise NotImplementedError
>>>
>>>
>>> greeting = get_greeting('English')
>>> greeting('Mark', 'Watney')
Hello Mark Watney
>>>
>>> greeting = get_greeting('Polish')
>>> greeting('Mark', 'Watney')
Witaj Mark Watney
>>>
>>> greeting = get_greeting('Spanish')
Traceback (most recent call last):
NotImplementedError


Parameter Functions
-------------------
* Function can be user as a parameter

>>> from urllib.request import urlopen
>>>
>>>
>>> def fetch(url: str,
...           on_success = lambda response: ...,
...           on_error = lambda error: ...,
...           ) -> None:
...     try:
...         result = urlopen(url).read().decode('utf-8')
...     except Exception as error:
...         on_error(error)
...     else:
...         on_success(result)

>>> fetch(
...     url = 'https://python3.info',
...     on_success = lambda resp: print(resp),
...     on_error = lambda err: print(err),
... )  # doctest: +SKIP

>>> def ok(response: str):
...     print(response)
>>>
>>> def err(error: Exception):
...     print(error)
>>>
>>>
>>> fetch(url='https://python3.info')  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_success=ok)  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_error=err)  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_success=ok, on_error=err)  # doctest: +SKIP
>>> fetch(url='https://python3.info/not-existing', on_error=err)  # doctest: +SKIP


Use Case - 0x01
---------------
>>> def map(func, data):
...     ...

>>> def filter(func, data):
...     ...

>>> def reduce(func, data):
...     ...


Use Case - 0x02
---------------
>>> # doctest: +SKIP
... import pandas as pd
...
...
... DATA = 'https://python3.info/_static/phones-pl.csv'
...
... result = (
...     pd
...     .read_csv(DATA, parse_dates=['datetime'])
...     .set_index('datetime', drop=True)
...     .drop(columns=['id'])
...     .loc['2000-01-01':'2000-03-01']
...     .query('item == "sms"')
...     .groupby(['period','item'])
...     .agg(
...         duration_count = ('duration', 'count'),
...         duration_sum = ('duration', 'sum'),
...         duration_median = ('duration', 'median'),
...         duration_mean = ('duration', 'mean'),
...         duration_std = ('duration', 'std'),
...         duration_var = ('duration', 'var'),
...         value = ('duration', lambda column: column.mean().astype(int))
...     )
... )

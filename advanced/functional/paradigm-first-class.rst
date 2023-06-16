Functional First-Class
======================
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...
* Function can be returned
* Function can be user as a parameter

In Python, functions are considered first-class citizens, which means that
they can be treated like any other object in the language. This concept is
also known as first-class functions.

Here are some of the properties of first-class functions in Python:

1. A function can be assigned to a variable: You can assign a function to a
variable, just like you would with any other object.

2. A function can be passed as an argument to another function: You can pass
a function as an argument to another function.

3. A function can be returned as a value from another function: A function
can return another function as its value.

4. A function can be stored in a data structure: You can store functions in
lists, dictionaries, or other data structures.

Here's an example of using a function as a first-class citizen in Python:

>>> def add(a, b):
...     return a + b
>>>
>>> def multiply(a, b):
...     return a * b
>>>
>>> def apply(func, a, b):
...     return func(a, b)
>>>
>>> apply(add, 2, 3)
5
>>>
>>> apply(multiply, 2, 3)
6

In this example, the ``apply()`` function takes a function as its first
argument, and two numbers as the second and third arguments. It then calls
the function with the two numbers and returns the result. The ``add()`` and
``multiply()`` functions are passed as arguments to the ``apply()`` function,
and the results are stored in ``result1`` and ``result2``.


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

Function Return
===============


.. glossary::

    return
        Python keyword for specifying value outcome from a function.


Syntax
------
.. code-block:: python

    def myfunction():
        return <expression>

>>> def mean():
...     return (1+2) / 2

>>> def add():
...     a = 1
...     b = 2
...     return a + b


Return Keyword
--------------
* ``return`` keyword indicates outcome of the function

>>> def hello():
...     return 'hello'
>>>
>>>
>>> hello()
'hello'

Code after ``return`` will not execute:

>>> def hello():
...     print('before')
...     return 'hello'
...     print('after')
>>>
>>> hello()
before
'hello'

You can have more than one ``return`` keyword in a function, although function
will close after hitting any of them, and will not proceed any further.

>>> def hello():
...     print('before')
...     return 'hello'
...     return 'world'
...     print('after')
>>>
>>> hello()
before
'hello'

>>> def hello():
...     print('before')
...     return 'hello'
...     print('between')
...     return 'world'
...     print('after')
>>>
>>> hello()
before
'hello'

>>> def hello():
...     if True:
...         return 'hello'
...     else:
...         return 'world'
>>>
>>> hello()
'hello'

>>> def hello():
...     if True:
...         return 'hello'
...     else:
...         return 'world'
...     print('after if')
>>>
>>> hello()
'hello'


Return Basic Type
-----------------
>>> def myfunction():
...     return 42

>>> def myfunction():
...     return 13.37

>>> def myfunction():
...     return 'Mark Watney'

>>> def myfunction():
...     return True


Return Sequence
---------------
>>> def myfunction():
...     return list([42, 13.37, 'Mark Watney'])

>>> def myfunction():
...     return [42, 13.37, 'Mark Watney']

>>> def myfunction():
...     return tuple((42, 13.37, 'Mark Watney'))

>>> def myfunction():
...     return (42, 13.37, 'Mark Watney')

>>> def myfunction():
...     return 42, 13.37, 'Mark Watney'

>>> def myfunction():
...     return set({42, 13.37, 'Mark Watney'})

>>> def myfunction():
...     return {42, 13.37, 'Mark Watney'}


Return Mapping
--------------
>>> def myfunction():
...     return dict(firstname='Mark', lastname='Watney')

>>> def myfunction():
...     return {'firstname': 'Mark', 'lastname': 'Watney'}


Return Nested Sequence
----------------------
>>> def myfunction():
...     return [
...         ('Mark', 'Watney'),
...         {'Mark Watney', 'Melissa Lewis', 'Rick Martinez'},
...         {'astro': 'Mark Watney', 'agency': {'name': 'NASA'}},
...         {'astro': 'Mark Watney', 'missions': ['Ares1', 'Ares3']},
...         {'astro': 'Mark Watney', 'medals': (list(), tuple(), set())},
...     ]


Return None
-----------
* Python will ``return None`` if no explicit return is specified

>>> def myfunction():
...     return None

>>> def myfunction():
...     print('hello')

>>> def myfunction():
...     pass

>>> def myfunction():
...     """My function"""


Intercept Returned Value
------------------------
>>> def myfunction():
...     return 1
>>>
>>>
>>> result = myfunction()
>>> print(result)
1


Locals
------
>>> def myfunc():
...     a = 1
...     b = 2
...     return locals()
...
>>> myfunc()
{'a': 1, 'b': 2}


Assignments
-----------
.. literalinclude:: assignments/function_return_a.py
    :caption: :download:`Solution <assignments/function_return_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_return_b.py
    :caption: :download:`Solution <assignments/function_return_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_return_c.py
    :caption: :download:`Solution <assignments/function_return_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_return_d.py
    :caption: :download:`Solution <assignments/function_return_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_return_e.py
    :caption: :download:`Solution <assignments/function_return_e.py>`
    :end-before: # Solution

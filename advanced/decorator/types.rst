Decorator Types
===============


Important
---------
By type:

    * Function decorators
    * Class decorators

By decorated object:

    * Decorating function
    * Decorating class
    * Decorating method

By wrapper type:

    * Wrapper function
    * Wrapper class
    * Wrapper method

By number of arguments:

    * Without arguments
    * With arguments


Decorator Types
---------------
* Function decorators
* Class decorators
* In this example:

    * ``obj`` is a decorated object
    * doesn't matter, whether is a function, class or method

>>> def mydecorator(obj):
...     ...

>>> class MyDecorator:
...     def __init__(self, obj):
...         ...


Wrapper Type
------------
* Wrapper function
* Wrapper class
* Wrapper method
* In this example:

    * ``obj`` is a decorated object
    * doesn't matter, whether is a function, class or method

* If ``obj`` and ``Wrapper`` are classes, ``Wrapper`` can inherit from ``obj`` (to extend it)

>>> def mydecorator(obj):
...     def wrapper(*args, **kwargs):
...         ...
...     return wrapper

>>> def mydecorator(obj):
...     class Wrapper:
...         def __init__(self, *args, **kwargs):
...             ...
...     return Wrapper

>>> class MyDecorator:
...     def __init__(self, obj):
...         ...
...
...     def __call__(self, *args, **kwargs):
...         ...


Decorated Object
----------------
* Decorating function (by convention ``func`` or ``fn``)
* Decorating class (by convention ``cls``)
* Decorating method (by convention ``mth``, ``meth`` or ``method``)

>>> def mydecorator(func):
...     ...

>>> def mydecorator(cls):
...     ...

>>> def mydecorator(mth):
...     ...

>>> class MyDecorator:
...     def __init__(self, func):
...         ...

>>> class MyDecorator:
...     def __init__(self, cls):
...         ...

>>> class MyDecorator:
...     def __init__(self, mth):
...         ...


Usage
-----
>>> @mydecorator
... def myfunction(*args, **kwargs):
...     ...

>>> class MyClass:
...     @mydecorator
...     def mymethod(self, *args, **kwargs):
...         ...

>>> @mydecorator
... class MyClass:
...     ...

>>> @MyDecorator
... def myfunction(*args, **kwargs):
...     ...

>>> class MyClass:
...     @MyDecorator
...     def mymethod(self, *args, **kwargs):
...         ...

>>> @MyDecorator
... class MyClass:
...     ...


Arguments
---------
* Without arguments
* With arguments

>>> @mydecorator
... def myfunction(*args, **kwargs):
...     ...

>>> @MyDecorator
... def myfunction(*args, **kwargs):
...     ...

>>> @mydecorator('arg1', 'arg2')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...

>>> @MyClass('arg1', 'arg2')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


Assignments
-----------
.. literalinclude:: assignments/decorator_syntax_a.py
    :caption: :download:`Solution <assignments/decorator_syntax_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_syntax_b.py
    :caption: :download:`Solution <assignments/decorator_syntax_b.py>`
    :end-before: # Solution

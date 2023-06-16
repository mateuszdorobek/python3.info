Functional Pattern Closure
==========================
* Technique by which the data is attached to some code even after end of those other original functions is called as closures
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants
* Inner functions implicitly carry references to all of the local variables in the surrounding scope that are referenced by the function
* Since Python 2.2

In Python, a closure is a function object that has access to variables in
its enclosing lexical scope, even when the function is called outside that
scope. A closure is created when a nested function references a value from
its enclosing scope.

Here's an example of using a closure in Python:

>>> def outer_function(x):
...     def inner_function(y):
...         return x + y
...     return inner_function
>>>
>>> add_five = outer_function(5)
>>> result = add_five(10)
>>>
>>> print(result)
15

In this example, the ``outer_function()`` function takes a value ``x``
as its argument and defines a nested function ``inner_function()``.
The ``inner_function()`` function references the ``x`` variable from
its enclosing scope.

When the ``outer_function()`` function is called with the argument ``5``,
it returns the ``inner_function()`` function. This function is assigned
to the variable ``add_five``.

The ``add_five()`` function is then called with the argument ``10``,
which is added to the ``x`` value of ``5`` from the enclosing scope.
The result of ``15`` is returned and stored in the ``result`` variable.

The ``add_five()`` function is a closure because it has access to the ``x``
variable from its enclosing scope, even though it is called outside that
scope. The closure allows the ``add_five()`` function to "remember" the
value of ``x`` from when it was defined.

Closures are useful for creating functions that have state or that need
to remember values from previous calls. They can also be used to create
decorators, which are functions that modify the behavior of other functions.

>>> def f(x):
...     def g(y):
...         return x + y
...     return g


Recap
-----
Functions can define their own variables:

>>> def main():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> main()
Hello Mark Watney

Function can access data from outer scope:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> def main():
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> main()
Hello Mark Watney


Nested Function
---------------
* Function inside the function
* Nested functions can access the variables of the enclosing scope

>>> def main():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def say_hello():
...         print(f'Hello {firstname} {lastname}')
...     say_hello()
>>>
>>>
>>> main()
Hello Mark Watney
>>>
>>> say_hello()
Traceback (most recent call last):
NameError: name 'say_hello' is not defined


What is closure?
----------------
Closure is a technique by which the data is attached to some code even after end
of those other original functions is called as closures. When the interpreter
detects the dependency of inner nested function on the outer function, it stores
or makes sure that the variables in which inner function depends on are
available even if the outer function goes away.

>>> def main():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def say_hello():
...         print(f'Hello {firstname} {lastname}')
...     return say_hello

Function local variables are stored on the stack (function stack frame). Inner
functions have access to outer functions variables (access to outer function
stack). In order to that work, you can call inner function only when outer
function is running [#ytclosures]_

>>> result = main()
>>> result()
Hello Mark Watney

Remove outer function:

>>> result = main()
>>> del main
>>> result()
Hello Mark Watney


Why?
----
* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants

>>> def main():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print(f'Hello {firstname} {lastname}')
...
...     return say_hello

>>> hello = main()
>>> hello()
Hello Mark Watney

>>> hello = main()
>>> del main
>>> hello()
Hello Mark Watney

>>> hello   # doctest: +ELLIPSIS
<function main.<locals>.say_hello at 0x...>


How Objects Were Born
---------------------
* ``main`` - constructor
* ``say_hello`` - instance method
* ``firstname`` - instance variable (field)
* ``lastname`` - instance variable (field)

>>> def main():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print(f'Hello {firstname} {lastname}')
...
...     return locals()
...

>>> x = main()
>>>
>>> x['firstname']
'Mark'
>>>
>>> x['lastname']
'Watney'
>>>
>>> x['say_hello']()
Hello Mark Watney

>>> x  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
{'say_hello': <function main.<locals>.say_hello at 0x...>,
 'firstname': 'Mark',
 'lastname': 'Watney'}


References
----------
.. [#ytclosures] Martin, Robert C. The S.O.L.I.D. Principles of OO & Agile Design. Year: 2015. Retrieved: 2021-09-22. URL: https://youtu.be/t86v3N4OshQ?t=954


Assignments
-----------
.. literalinclude:: assignments/functional_closure_a.py
    :caption: :download:`Solution <assignments/functional_closure_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/functional_closure_b.py
    :caption: :download:`Solution <assignments/functional_closure_b.py>`
    :end-before: # Solution

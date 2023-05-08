Functional Pattern Closure
==========================
* Technique by which the data is attached to some code even after end of those other original functions is called as closures
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants
* Inner functions implicitly carry references to all of the local variables in the surrounding scope that are referenced by the function
* Since Python 2.2

>>> def f(x):
...     def g(y):
...         return x + y
...     return g


Recap
-----
Functions can define their own variables:

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> run()
Hello Mark Watney

Function can access data from outer scope:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> def run():
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> run()
Hello Mark Watney


Nested Function
---------------
* Function inside the function
* Nested functions can access the variables of the enclosing scope

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def hello():
...         print(f'Hello {firstname} {lastname}')
...     hello()
>>>
>>>
>>> run()
Hello Mark Watney
>>>
>>> hello()
Traceback (most recent call last):
NameError: name 'hello' is not defined


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
...         print(firstname, lastname)
...
...     return say_hello

>>> hello = main()
>>>
>>> hello()
Mark Watney
>>>

>>> hello = main()
>>> del main
>>>
>>> hello()
Mark Watney

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
...         print(firstname, lastname)
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
>>> x['say_hello'].__call__()
Mark Watney

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

Functional Referential Transparency
===================================
* Value of a variable in a functional program never changes once defined
* This eliminates any chances of side effects
* Any variable can be replaced with its actual value at any point of execution [#Hughes1984]_

Any variable can be replaced with its actual value at any point of
execution [#Hughes1984]_. This is known as referential transparency.
It ensures that the same language expression gives the same output.
[#Inouye2022]_

Variables, once defined in a functional programming language, aren't allowed
to change the value that they hold. However, we can create a new variable.
The immutable nature of variables helps preserve the state throughout the
program. Assignment statements are discouraged in functional programming.
For storing additional values in a program developed using the functional
paradigm, new variables must be defined. The state of a variable in such
a program is constant at any moment in time. [#Inouye2022]_

Referential transparency eliminates the slightest chances of any undesired
effects, as any variable can be replaced with its actual value at any point
during the program execution. [#Inouye2022]_

Bad:

>>> a = 1
>>> a += 2

Good:

>>> a = 1
>>> b = a + 2


Use Case - 0x01
---------------
>>> def add(a,b):
...     return a + b
>>>
>>>
>>> x = 1
>>> y = 2
>>>
>>> add(x,y)
3
>>> add(1,y)
3
>>> add(x,2)
3
>>> add(1,2)
3


References
----------
.. [#Inouye2022] Inouye, Jenna. "Functional Programming Languages: Concepts & Advantages". Year: 2022. Retrieved: 2022-07-28, URL: https://hackr.io/blog/functional-programming

.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.

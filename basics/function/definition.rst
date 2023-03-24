Function Definition
===================
* Automate repetitive tasks
* Allow code reuse
* Improve code readability
* Clean-up code
* Allow easier refactoring

>>> def say_hello():
...     print('hello')

.. glossary::

    function
    func
    fn
        A set of instructions which has common name. Function will execute
        all of those instructions each time it is called.

    call
    function call
    call a function
        Run a function.

    procedure
        The same as function. Way back in history there was a distinction
        that the procedures don't take an arguments and functions does.
        Now this blurred completely. Hardly anyone is talking about procedures
        now, so the same stuck, but it is very rarely used. Most common
        old-school programmers whill use that word. You may find this also
        in documentation of aged projects.


Syntax
------
.. code-block:: python

    def <name>():
        <do something>


Example
-------
>>> def say_hello():
...     print('hello')

If the function is short, you can also write it in the one line. This is not
recommended and degrades code readability:

>>> def say_hello(): print('hello')


Calling
-------
Let's define a function:

>>> def say_hello():
...     print('hello')

Call a function for a first time:

>>> say_hello()
hello

Call a function for a second time:

>>> say_hello()
hello

Each time it will give the same result. That's right. This function is very
simple and all what it does is just print word 'hello' on the standard output.


Function Name Case
------------------
Do not use ``camelCase`` or ``PascalCase`` names.

The ``camelCase`` name is c/c++/Java/JavaScript convention. It is not good
to mix conventions from different languages. If you write C code, use C
conventions. If you program in Python, use Python conventions. Remember,
there are different communities around both of those languages:

>>> def sayHello():  # bad, function name should be lowercase
...     pass

The ``PascalCase`` name has completely different meaning in Python - it is
used for classes. Using such name convention will mistake others.

>>> def SayHello():  # bad, function name should be lowercase
...     pass

Use ``snake_case`` names in Python. It is easy to remember. Python looks like
a snake, and sounds like a snake ;) This is double internal joke, because
Python name came from Monty Python, of which Guido van Rossum was a big fun.

This is ``snake_case()`` name. It is Pythonic way:

>>> def say_hello():  # good
...     pass


Choosing Good Name
------------------
People, especially those who uses simple IDEs or notepads without
sophisticated autocompletion will tend to create function with shorter
names in order to save couple of characters each time when it is called.
This at the beginning could be a good idea, but in the long run will lead
to disaster. Coming back to your code after a year or two will require you
to rediscover the code and read it once again.

>>> def var(data, m):
...     return sum((Xi-m) ** 2 for Xi in data) / len(data)
>>>
>>> var([1,2,3,4], 1)  # doctest: +SKIP
>>> vars([1,2,3,4])  # doctest: +SKIP

Function name ``var()`` is very similar to built-in function ``vars()`` which
does something completely different. It shows all the attributes of an object
passed to it. A single misspell, such as forgetting about letter ``s`` at the
end of a name may lead to printing all the internal information about object
publicly. This is very dangerous for publicly accessed systems.

More verbose names, such as ``variance()`` will distinguish this function
from built-in ``vars()`` far better:

>>> def variance(data, m):
...     return sum((Xi-m) ** 2 for Xi in data) / len(data)
>>>
>>> variance([1,2,3,4], 1)  # doctest: +SKIP
>>> vars([1,2,3,4])  # doctest: +SKIP

This way a probability for mistake is far lower and even if, then will be
better discoverable.


Name Collisions
---------------
Add underscore (``_``) at the end of name when name collide.

>>> def print_(text):
...     print(f'<strong>{text}</strong>')

Although prefer naming it differently:

>>> def print_html(text):
...     print(f'<strong>{text}</strong>')


Special Function Names
----------------------
System functions names starts and ends with 'dunder'. The word 'dunder'
stands for double underscores: ``__``:

>>> def __import__(module_name):
...     pass


Assignments
-----------
.. literalinclude:: assignments/function_definition_a.py
    :caption: :download:`Solution <assignments/function_definition_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_definition_b.py
    :caption: :download:`Solution <assignments/function_definition_b.py>`
    :end-before: # Solution

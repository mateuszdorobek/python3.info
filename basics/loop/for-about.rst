Loop For About
==============
>>> data = ['a', 'b', 'c']
>>> i = 0
>>>
>>> while i < len(data):
...     x = data[i]
...     print(x)
...     i += 1
a
b
c

>>> data = ['a', 'b', 'c']
>>>
>>> for x in data:
...     print(x)
a
b
c


Syntax
------
* ``ITERABLE`` must implement ``iterator`` interface
* More information in `Protocol Iterator`

For loop syntax:

.. code-block:: python

    for <variable> in <iterable>:
        <do something>

>>> for digit in [1, 2, 3]:
...     pass


Iterating Sequences
-------------------
* Iterating works for builtin sequences:

    * ``str``
    * ``bytes``
    * ``list``
    * ``tuple``
    * ``set``
    * ``dict``

>>> DATA = 'NASA'
>>>
>>> for letter in DATA:
...     print(letter)
N
A
S
A

>>> DATA = [1, 2, 3]
>>>
>>> for digit in DATA:
...     print(digit)
1
2
3

>>> DATA = ['a', 'b', 'c']
>>>
>>> for letter in DATA:
...     print(letter)
a
b
c

>>> users = [
...     'Mark Watney',
...     'Melissa Lewis',
...     'Rick Martinez',
... ]
>>>
>>> for user in users:
...     print(user)
Mark Watney
Melissa Lewis
Rick Martinez

>>> DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']
>>>
>>> for value in DATA:
...     print(value)
5.1
3.5
1.4
0.2
setosa

>>> for current in [1,2,3]:
...     print(current)
1
2
3


Note to the Programmers of Other Languages
------------------------------------------
There are several types of loops in general:

    * for
    * foreach
    * while
    * do while
    * until

But in Python we have only two:

    * while
    * for

This does not takes into consideration comprehensions and generator
expressions, which will be covered in next chapters.

Note, that Python ``for`` is not the same as ``for`` in other languages,
such as C, C++, C#, JAVA, Java Script. Python ``for`` loop is more like
``foreach``. Check the following example in JAVA:

.. code-block:: java

    char[] DATA = {'a', 'b', 'c'};

    forEach (var letter : DATA) {
        System.out.println(letter);
    }

.. code-block:: php

    $data = array('a', 'b', 'c');

    foreach ($data as $letter) {
        echo $letter;
    }

.. code-block:: js

    DATA = ['a', 'b', 'c']

    for (let letter of DATA) {
        console.log(letter)
    }

And this relates to Python regular ``for`` loop:

>>> DATA = ['a', 'b', 'c']
>>>
>>> for letter in DATA:
...     print(letter)
a
b
c

Regular ``for`` loop in other languages looks like that (example in C++):

.. code-block:: cpp

    char DATA[] = {'a', 'b', 'c'}

    for (int i = 0; i < std::size(DATA); i++) {
       letter = data[i];
       printf(letter);
    }

Python equivalent will be:

>>> DATA = ['a', 'b', 'c']
>>> i = 0
>>>
>>> while i < len(DATA):
...     letter = DATA[i]
...     print(letter)
...     i += 1
a
b
c

Yes, that's true, it is a ``while`` loop. This is due to the fact, that ``for``
loop from other languages is more like a ``while`` loop in Python.

Nevertheless, the very common bad practice is to do ``range(len())``:

>>> data = ['a', 'b', 'c']
>>>
>>> for i in range(len(data)):
...     letter = data[i]
...     print(letter)
a
b
c

Note, how similar are those concepts. This is trying to take syntax from other
languages and apply it to Python. ``range(len())`` is considered a bad practice
and it will not work with generators. But it gives similar look-and-feel.

Please remember:

    * Python ``for`` is more like ``foreach`` in other languages.
    * Python ``while`` is more like ``for`` in other languages.


Good Practices
--------------
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Prefer locally meaningful name over generic names
* Generic names:

    * ``obj`` - generic name (in Python everything is an object)
    * ``element`` - generic name
    * ``item`` - generic name
    * ``x`` - ok for oneliners, bad for more than one line
    * ``e`` - ok for oneliners, bad for more than one line
    * ``l`` - bad
    * ``o`` - bad
    * ``d`` - bad (for digit)

* Locally meaningful name:

    * ``letter``
    * ``feature``
    * ``digit``
    * ``person``
    * ``color``
    * ``username``
    * etc.

* Special meaning (by convention):

    * ``i`` - for loop counter
    * ``_`` - if value is not used

>>> for x in [1, 2, 3]:
...     print(x)
1
2
3

>>> for i in range(0,3):
...     print(i)
0
1
2


Use Case - 0x01
---------------
>>> def spawn_thread():
...     ...
>>>
>>>
>>> for _ in range(3):
...     spawn_thread()


Use Case - 0x02
---------------
* https://www.keepandshare.com/userpics/r/o/b/e/rt/2019-12/sb/screen_shot_2019_12_01_at_3.26.20_pm-34867850.jpg?ts=1575242835

>>> text = 'hello'

>>> text.upper()
'HELLO'

>>> i = 0
>>> result = ''
>>> offset = 32  # ASCII table between lowercase and uppercase letters
>>>
>>> while i < len(text):
...     letter = ord(text[i])
...     letter = chr(letter-32)
...     result += letter
...     i += 1
...
>>> result
'HELLO'

>>> # doctest: +SKIP
... if value == 97:
...     return 'a'
... elif value == 99:
...     return 'b'


Assignments
-----------
.. literalinclude:: assignments/loop_for_a.py
    :caption: :download:`Solution <assignments/loop_for_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_b.py
    :caption: :download:`Solution <assignments/loop_for_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_c.py
    :caption: :download:`Solution <assignments/loop_for_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_d.py
    :caption: :download:`Solution <assignments/loop_for_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_e.py
    :caption: :download:`Solution <assignments/loop_for_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_f.py
    :caption: :download:`Solution <assignments/loop_for_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_for_g.py
    :caption: :download:`Solution <assignments/loop_for_g.py>`
    :end-before: # Solution

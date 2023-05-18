String Input
============
* ``input()`` always returns ``str``
* Good practice: add space at the end of prompt
* Good practice: always ``.strip()`` text from user input
* Good practice: always sanitize values from user prompt


SetUp
-----
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['Mark Watney', '42', '42.0', '42,0'])


Input Str
---------
``input()`` function argument is prompt text, which "invites" user to enter
specific information. Note colon-space (": ") at the end. Space is needed
to separate user input from prompt. Without it, user inputted text will be
glued to your question.

>>> name = input('What is your name: ')  #input: 'Mark Watney'
>>>
>>> print(name)
Mark Watney
>>>
>>> type(name)
<class 'str'>


Input Int
---------
``input()`` always returns a ``str``.
To get numeric value type casting to ``int`` is needed.

>>> age = input('What is your age: ')  #input: 42
>>>
>>> print(age)
42
>>> type(age)
<class 'str'>
>>>
>>> age = int(age)
>>> print(age)
42
>>>
>>> type(age)
<class 'int'>


Input Float
-----------
Conversion to ``float`` handles decimals, which ``int`` does not support:

>>> age = input('What is your age: ')  #input: 42.0
>>>
>>> age = int(age)
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '42.0'
>>>
>>> age = float(age)
>>> print(age)
42.0
>>>
>>> type(age)
<class 'float'>

Conversion to ``float`` cannot handle comma (',') as a decimal separator:

>>> age = input('What is your age: ')  #input: 42,0
>>>
>>> age = int(age)
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '42,0'
>>>
>>> age = float(age)
Traceback (most recent call last):
ValueError: could not convert string to float: '42,0'
>>>
>>> float(age.replace(',', '.'))
42.0


Automated Input
---------------
* Stub - simple object which always returns the same result
* Mock - an object which has more advanced capabilities than Stub, such as:
         counting number of calls, recording passed arguments etc.

Note, that usage of Stubs and Mocks is only for testing purposes. You should
not do that in your programs at the production level! Mocks and Stubs
assumes, that user will input particular values.


Stub
----
You can also use Stub (a function with fixed value) to simulate ``input()``:

>>> def input(_):
...     return 'Mark Watney'
>>>
>>>
>>> input('What is your name?: ')
'Mark Watney'

At the end of the chapter about Functions, there is a mention about ``lambda``
expression. This could be also used here to make the code more compact.

>>> input = lambda _: 'Mark Watney'
>>>
>>>
>>> input('What is your name?: ')
'Mark Watney'

Both methods: Function Stub and Lambda Stub works the same.


Mock
----
In following example we simulate ``input()`` built-in function with MagicMock.
Then, usage of ``input()`` is as normal.

>>> from unittest.mock import MagicMock
>>>
>>>
>>> input = MagicMock(side_effect=['Mark Watney'])
>>>
>>> input('What is your name?: ')
'Mark Watney'

Using MagicMock you can simulate more than one future input values from user:

>>> from unittest.mock import MagicMock
>>>
>>>
>>> input = MagicMock(side_effect=['red', 'green', 'blue'])
>>>
>>> input('Type color: ')
'red'
>>> input('Type color: ')
'green'
>>> input('Type color: ')
'blue'

Mocks has advantage over stubs, because they collect some diagnostic
information.

>>> input.called
True

>>> input.call_count
3

>>> input.mock_calls  # doctest: +NORMALIZE_WHITESPACE
[call('Type color: '),
 call('Type color: '),
 call('Type color: ')]


Assignments
-----------
.. literalinclude:: assignments/type_strinput_a.py
    :caption: :download:`Solution <assignments/type_strinput_a.py>`
    :end-before: # Solution

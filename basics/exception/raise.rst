Exception Raise
===============
* Used when error occurs
* You can catch exception and handles erroneous situation
* If file does not exists
* If no permissions to read file
* If function argument is invalid type (ie. ``int('one')``)
* If value is incorrect (ie. negative Kelvin temperature)
* If network or database connection could not be established


Raising Exceptions
------------------
* Exceptions can have message
* You choose which exception best represent error

Raise Exception without message:

>>> raise RuntimeError
Traceback (most recent call last):
RuntimeError

Exception with additional message:

>>> raise RuntimeError('Some message')
Traceback (most recent call last):
RuntimeError: Some message


Example
-------
We want to check if Kelvin temperature given by user is not negative.
Note that Kelvin temperatures below zero doesn't exist, hence it's an
absolute scale. In order to do so, we need to ask user to input value.
Let's assume user input ``-1``.

>>> temperature = -1  # User input this value

Now we need to check if the temperature is not negative. If temperature is 0
or above we can proceed with program execution. However if the temperature
is below zero... Then we should warn user about problem and exit the program.
This is why we have exceptions. We can break execution of a program
in erroneous situations.

>>> if temperature > 0.0:
...     print('Temperature is valid')
... else:
...     raise ValueError('Kelvin cannot be negative')
Traceback (most recent call last):
ValueError: Kelvin cannot be negative

Good software communicates well with programmer. Exceptions are common
language to talk about problems and not-nominal (abnormal) situations
in your code.

>>> def check(temperature):
...     if type(temperature) not in {float, int}:
...         raise TypeError('Temperature must be int or float')
...     if temperature < 0:
...         raise ValueError('Kelvin temperature cannot be negative')
...     return temperature


Use Case - 0x01
---------------
>>> def apollo13():
...     raise RuntimeError('Oxygen tank explosion')
>>>
>>>
>>> apollo13()
Traceback (most recent call last):
RuntimeError: Oxygen tank explosion

>>> def apollo18():
...     raise NotImplementedError('Mission dropped due to budget cuts')
>>>
>>>
>>> apollo18()
Traceback (most recent call last):
NotImplementedError: Mission dropped due to budget cuts


Assignments
-----------
.. literalinclude:: assignments/exception_raise_a.py
    :caption: :download:`Solution <assignments/exception_raise_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_raise_b.py
    :caption: :download:`Solution <assignments/exception_raise_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_raise_c.py
    :caption: :download:`Solution <assignments/exception_raise_c.py>`
    :end-before: # Solution

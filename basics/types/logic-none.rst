Logic None
==========
* Empty (null) or unknown (unset) value
* It is not ``False`` value
* First letter capitalized, other are lower cased


Syntax
------
* First letter capitalized, other are lower cased

>>> data = None


None, Null, Nil
---------------
>>> data = none  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'none' is not defined
>>>
>>> data = NONE  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'NONE' is not defined

>>> data = null  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'null' is not defined
>>>
>>> data = Null  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'Null' is not defined
>>>
>>> data = NULL  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'NULL' is not defined

>>> data = nil  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'NIL' is not defined
>>>
>>> data = NIL  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'NIL' is not defined


Check If None
-------------
* ``x is None`` - ``x`` is the same object as ``y``
* ``x is not None`` - ``x`` is not the same object as ``y``

>>> data = None
>>>
>>>
>>> data is None
True
>>>
>>> data is not None
False

* Do not use ``==`` or ``!=`` to check ``None`` values
* It works, but it is a subject to change

>>> data = None
>>>
>>>
>>> data == None
True
>>>
>>> data != None
False


Type Conversion
---------------
With ``if`` statements behaves like negative values

>>> bool(None)
False

>>> bool(False)
False

>>> None == False
False
>>>
>>> None is False
False



Use Case - 0x01
---------------
>>> adult = False  # Person is not adult
>>> adult = None   # We don't know is person is adult


Use Case - 0x02
---------------
>>> age = False  # False is invalid in this context
>>> age = None   # Age is unknown


Use Case - 0x03
---------------
>>> firstname = 'Melissa'
>>> lastname = 'Lewis'
>>> age = None
>>>
>>>
>>> age is None
True


Assignments
-----------
.. literalinclude:: assignments/type_none_a.py
    :caption: :download:`Solution <assignments/type_none_a.py>`
    :end-before: # Solution

Syntax Comparison
=================


Greater Than
------------
* ``obj > obj``

>>> 1 > 2
False

>>> x = 1
>>> x > 2
False

>>> x = 1
>>> y = 2
>>>
>>> x > y
False


Greater or Equal Then
---------------------
* ``obj >= obj``

>>> 1 >= 2
False

>>> x = 1
>>> x >= 2
False

>>> x = 1
>>> y = 2
>>>
>>> x >= y
False


Less Than
---------
* ``obj < obj``

>>> 1 < 2
True

>>> x = 1
>>> x < 2
True

>>> x = 1
>>> y = 2
>>>
>>> x < y
True


Less or Equal Then
------------------
* ``obj <= obj``

>>> 1 <= 2
True

>>> x = 1
>>> x <= 2
True

>>> x = 1
>>> y = 2
>>>
>>> x <= y
True


Equals
------
* ``obj == obj``

>>> 1 == 2
False

>>> x = 1
>>> x == 2
False

>>> x = 1
>>> y = 2
>>>
>>> x == y
False

>>> 0 == -0
True


Not Equals
----------
* Inversion of ``==``
* ``obj != obj``

>>> 1 != 2
True

>>> x = 1
>>> x != 2
True

>>> x = 1
>>> y = 2
>>>
>>> x != y
True


Use Case - 0x01
---------------
>>> ADULT = 18
>>> user_age = 42
>>>
>>> user_age > ADULT
True

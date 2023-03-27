Star Signature
==============
* Define API for you functions
* Require particular way of passing positional and optional parameters
* All parameters after ``*`` must be keyword-only
* All parameters before ``/`` must be positional-only
* ``*`` could be anywhere, not only at the beginning
* ``/`` could be anywhere, not only at the end
* Since Python 3.8: :pep:`570` -- Python Positional-Only Parameters


Recap
-----
* Positional arguments - value passed to function
* Positional arguments - order is important
* Positional arguments - must be at the left side
* Keyword arguments - value passed to function resolved by name
* Keyword arguments - order is not important
* Keyword arguments - must be on the right side
* Positional argument cannot follow keyword arguments

>>> def set_point(x, y, z=None):
...      print(f'{x=}, {y=}, {z=}')

Valid:

>>> set_point(1, 2, 3)
x=1, y=2, z=3
>>>
>>> set_point(x=1, y=2, z=3)
x=1, y=2, z=3
>>>
>>> set_point(1, 2, z=3)
x=1, y=2, z=3
>>>
>>> set_point(1, y=2, z=3)
x=1, y=2, z=3

Errors:

>>> set_point(1, 2)
x=1, y=2, z=None
>>>
>>> set_point(1, y=2)
x=1, y=2, z=None
>>>
>>> set_point(1, z=3)
Traceback (most recent call last):
TypeError: set_point() missing 1 required positional argument: 'y'


Keyword-only Parameters
-----------------------
* All parameters after ``*`` must be keyword-only
* ``*`` could be anywhere, not only at the beginning

>>> def set_point(*, x, y, z=None):
...     print(f'{x=}, {y=}, {z=}')

Valid:

>>> set_point(x=1, y=2)
x=1, y=2, z=None
>>>
>>> set_point(x=1, y=2, z=3)
x=1, y=2, z=3

Errors:

>>> set_point(1, 2, 3)
Traceback (most recent call last):
TypeError: set_point() takes 0 positional arguments but 3 were given
>>>
>>> set_point(1, 2, z=3)
Traceback (most recent call last):
TypeError: set_point() takes 0 positional arguments but 2 positional arguments (and 1 keyword-only argument) were given
>>>
>>> set_point(1, y=2, z=3)
Traceback (most recent call last):
TypeError: set_point() takes 0 positional arguments but 1 positional argument (and 2 keyword-only arguments) were given


Positional-only Parameters
--------------------------
* Since Python 3.8: :pep:`570` -- Python Positional-Only Parameters
* All parameters before ``/`` must be positional-only
* ``/`` could be anywhere, not only at the end

>>> def set_point(x, y, z=None, /):
...     print(f'{x=}, {y=}, {z=}')

Valid:

>>> set_point(1, 2)
x=1, y=2, z=None
>>>
>>> set_point(1, 2, 3)
x=1, y=2, z=3

Errors:

>>> set_point(1, 2, z=3)
Traceback (most recent call last):
TypeError: set_point() got some positional-only arguments passed as keyword arguments: 'z'
>>>
>>> set_point(1, y=2, z=3)
Traceback (most recent call last):
TypeError: set_point() got some positional-only arguments passed as keyword arguments: 'y, z'


Positional and Keyword Parameters
---------------------------------
>>> def set_point(x, /, y, *, z=None):
...     print(f'{x=}, {y=}, {z=}')

Valid:

>>> set_point(1, 2)
x=1, y=2, z=None
>>>
>>> set_point(1, 2, z=3)
x=1, y=2, z=3
>>>
>>> set_point(1, y=2)
x=1, y=2, z=None
>>>
>>> set_point(1, y=2, z=3)
x=1, y=2, z=3

Errors:

>>> set_point(1, 2, 3)
Traceback (most recent call last):
TypeError: set_point() takes 2 positional arguments but 3 were given
>>>
>>>
>>> set_point(x=1, y=2, z=3)
Traceback (most recent call last):
TypeError: set_point() got some positional-only arguments passed as keyword arguments: 'x'


Use Case - 0x01
---------------
* Add
* https://docs.python.org/3/library/operator.html#operator.add

>>> def add(a, b, /):
...     return a + b


Use Case - 0x02
---------------
* Divmod

>>> def divmod(a, b, /):
...     return a//b, a%b


Use Case - 0x03
---------------
* ``sorted(iterable, /, *, key=None, reverse=False)``
* https://docs.python.org/3/library/functions.html#sorted:

>>> from inspect import signature
>>>
>>>
>>> data = [3, 1, 2]
>>>
>>> sorted(data)
[1, 2, 3]
>>>
>>> sorted(data, reverse=True)
[3, 2, 1]
>>>
>>> signature(sorted)
<Signature (iterable, /, *, key=None, reverse=False)>


Use Case - 0x03
---------------
* ``len(obj, /)``

>>> from inspect import signature
>>>
>>>
>>> data = [3, 1, 2]
>>>
>>> len(data)
3
>>>
>>> signature(len)
<Signature (obj, /)>


Use Case - 0x04
---------------
* ``sum(iterable, /, start=0)``
* https://docs.python.org/3/library/functions.html#sum:

>>> from inspect import signature
>>>
>>>
>>> data = [3, 1, 2]
>>>
>>> sum(data)
6
>>>
>>> sum(data, start=10)
16
>>>
>>> sum(data, 10)
16
>>>
>>> signature(sum)
<Signature (iterable, /, start=0)>


Use Case - 0x05
---------------
* ``str.strip(self, chars=None, /)``
* https://docs.python.org/3/library/stdtypes.html#str.strip

>>> from inspect import signature
>>>
>>>
>>> signature(str.strip)
<Signature (self, chars=None, /)>


Use Case - 0x06
---------------
* ``str.split(self, /, sep=None, maxsplit=-1)``
* https://docs.python.org/3/library/stdtypes.html#str.split

>>> from inspect import signature
>>>
>>>
>>> signature(str.split)
<Signature (self, /, sep=None, maxsplit=-1)>


Use Case - 0x07
---------------
* 49 parameters

>>> def read_csv(filepath_or_buffer, /, *, sep=', ', delimiter=None,
...              header='infer', names=None, index_col=None, usecols=None,
...              squeeze=False, prefix=None, mangle_dupe_cols=True,
...              dtype=None, engine=None, converters=None, true_values=None,
...              false_values=None, skipinitialspace=False, skiprows=None,
...              nrows=None, na_values=None, keep_default_na=True,
...              na_filter=True, verbose=False, skip_blank_lines=True,
...              parse_dates=False, infer_datetime_format=False,
...              keep_date_col=False, date_parser=None, dayfirst=False,
...              iterator=False, chunksize=None, compression='infer',
...              thousands=None, decimal=b'.', lineterminator=None,
...              quotechar='"', quoting=0, escapechar=None, comment=None,
...              encoding=None, dialect=None, tupleize_cols=None,
...              error_bad_lines=True, warn_bad_lines=True, skipfooter=0,
...              doublequote=True, delim_whitespace=False, low_memory=True,
...              memory_map=False, float_precision=None): ...

>>> read_csv('iris.csv', ';', None, 'infer', None, None, None, False, None,
...          True, None, None, None, None, None, False, None, None, None,
...          True, True, False, True, False, False, False, None, False,
...          False, None, 'infer', None, b',', None, '"', 0, None, None,
...          None, None, None, True, True, 0, True, False, True, False, None)
Traceback (most recent call last):
TypeError: read_csv() takes 1 positional argument but 49 were given

>>> read_csv('mydata.csv',
...          verbose=False,
...          skiprows=1,
...          parse_dates=['date', 'time'],
...          encoding='utf-8')


Assignments
-----------
.. literalinclude:: assignments/star_signature_a.py
    :caption: :download:`Solution <assignments/star_signature_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_signature_b.py
    :caption: :download:`Solution <assignments/star_signature_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/star_signature_c.py
    :caption: :download:`Solution <assignments/star_signature_c.py>`
    :end-before: # Solution

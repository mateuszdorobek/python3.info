Exception Traceback
===================
* Traceback will help you track down the bug

.. code-block:: pycon

    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>> apollo13()  # doctest +SKIP
    Traceback (most recent call last):
      File "/home/watney/myscript.py", line 5, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion


Fine Grained Error Locations
----------------------------
* Since Python 3.11
* :pep:`657` -- Include Fine Grained Error Locations in Tracebacks

.. code-block:: python

    Traceback (most recent call last):
      File "calculation.py", line 54, in <module>
        result = (x / y / z) * (a / b / c)
                  ~~~~~~^~~
    ZeroDivisionError: division by zero

.. code-block:: python

    Traceback (most recent call last):
      File "distance.py", line 11, in <module>
        print(manhattan_distance(p1, p2))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "distance.py", line 6, in manhattan_distance
        return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)
                               ^^^^^^^^^
    AttributeError: 'NoneType' object has no attribute 'x'

.. code-block:: python

    Traceback (most recent call last):
      File "query.py", line 37, in <module>
        magic_arithmetic('foo')
      File "query.py", line 18, in magic_arithmetic
        return add_counts(x) / 25
               ^^^^^^^^^^^^^
      File "query.py", line 24, in add_counts
        return 25 + query_user(user1) + query_user(user2)
                    ^^^^^^^^^^^^^^^^^
      File "query.py", line 32, in query_user
        return 1 + query_count(db, response['a']['b']['c']['user'], retry=True)
                                   ~~~~~~~~~~~~~~~~~~^^^^^
    TypeError: 'NoneType' object is not subscriptable


Traceback Analysis
------------------
* Stacktrace is 8 levels deep, it's not Java's 200 ;)
* Start analysing traceback from bottom-up

.. figure:: img/exception-traceback-java.png

    Stacktrace is 8 levels deep, it's not Java's 200 ;) [#javastacktrace]_

>>> def apollo13():
...     raise RuntimeError('Oxygen tank explosion')

Running script in Python console (REPL):

.. code-block:: pycon

    >>> apollo13()  # doctest +SKIP
    Traceback (most recent call last):
      File "<input>", line 5, in <module>
      File "<input>", line 2, in apollo13
    RuntimeError: Oxygen tank explosion

Running Python script:

.. code-block:: pycon

    >>> apollo13()  # doctest +SKIP
    Traceback (most recent call last):
      File "/home/watney/myscript.py", line 5, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion

Running Python script in PyCharm:

.. code-block:: pycon

    >>> apollo13()  # doctest +SKIP
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/Applications/PyCharm 2023.1.app/Contents/helpers/pydev/_pydev_bundle/pydev_umd.py", line 197, in runfile
        pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
      File "/Applications/PyCharm 2023.1.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
        exec(compile(contents+"\n", file, 'exec'), glob, loc)
      File "/home/watney/myscript.py", line 4, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion


Change Verbosity Level
----------------------
* Change level with ``sys.tracebacklimit``
* Default traceback limit is 8
* From time to time you can have problems somewhere in the middle, but it's rare
* Last lines are the most important, in most cases error is there

SetUp:

>>> import sys
>>>
>>> def apollo13():
...     raise RuntimeError('Oxygen tank explosion')

.. code-block:: pycon

    >>> sys.tracebacklimit = 2
    >>>
    >>> apollo13()  # doctest: +SKIP
    Traceback (most recent call last):
      File "/home/watney/myscript.py", line 4, in <module>
        apollo13()
      File "/home/watney/myscript.py", line 2, in apollo13
        raise RuntimeError('Oxygen tank explosion')
    RuntimeError: Oxygen tank explosion

.. code-block:: pycon

    >>> sys.tracebacklimit = 0
    >>>
    >>> apollo13()  # doctest: +SKIP
    RuntimeError: Oxygen tank explosion

Note, that ``sys.tracebacklimit = 0`` is useful in Python console (REPL).


References
----------
.. [#javastacktrace] https://mattwarren.org/images/2016/12/Huge%20Java%20Stack%20Trace.png

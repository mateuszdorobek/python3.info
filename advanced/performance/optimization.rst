Performance Optimization
========================
* https://wiki.python.org/moin/TimeComplexity


Contains
--------
* ``in`` checks whether iterable contains value
* O(n) - ``in str``
* O(n) - ``in list``
* O(n) - ``in tuple``
* O(1) - ``in set``
* O(1) - ``in dict``

List:

>>> DATABASE = ['mwatney', 'mlewis', 'rmartinez']
>>> user = 'ptwardowski'
>>>
>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... user in DATABASE
165 ns ± 35 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Set:

>>> DATABASE = {'mwatney', 'mlewis', 'rmartinez'}
>>> user = 'ptwardowski'
>>>
>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... login in users
103 ns ± 34.4 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Note, that the longer our ``DATABASE`` is, then the difference is more visible:

List:

>>> DATABASE = ['mwatney', 'mlewis', 'rmartinez', 'bjohanssen', 'avogel' 'cbeck']
>>> user = 'ptwardowski'
>>>
>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... login in users
276 ns ± 90.6 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Set:

>>> DATABASE = {'mwatney', 'mlewis', 'rmartinez', 'bjohanssen', 'avogel' 'cbeck'}
>>> user = 'ptwardowski'
>>>
>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... login in users
105 ns ± 35.2 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


PyPy
----
* http://pypy.org
* No GIL
* Can speedup couple order of magnitude


Patterns
--------
* Source: [#Shaw2022]_

.. figure:: img/performance-hints.png

    [#Shaw2022]_

Tools
-----
* memray [#Galindo2022]_
* tracemalloc
* mmap - memory allocation
* Pytest extension for doing benchmarking
* ``pip install line_profiler``

.. figure:: img/performance-tracemalloc.png

    [#Galindo2022]_

.. figure:: img/performance-memray-realtime.png

    Memray allows for real-time monitoring. [#Galindo2022]_

.. figure:: img/performance-memray-pytestplugin.png

    Memray has pytest plugin. [#Galindo2022]_

.. figure:: img/performance-memray.png

    Memray is Open Source. [#Galindo2022]_


Numpy vectorization
-------------------
Scipy Ecosystem:

.. figure:: img/scipy-ecosystem.png


Specialized data structures
---------------------------
* ``scipy.spatial`` - for spatial queries like distances, nearest neighbours, etc.
* ``pandas`` - for SQL-like grouping and aggregation
* ``xarray`` - for grouping across multiple dimensions
* ``scipy.sparse`` - sparse metrics for 2-dimensional structured data
* ``sparse`` (package) - for N-dimensional structured data
* ``scipy.sparse.csgraph`` - for graph-like problems (e.g. finding shortest paths)


Cython
------
* https://numba.pydata.org/
* https://cython.readthedocs.io/en/latest/
* https://en.wikipedia.org/wiki/Cython
* https://youtu.be/zQeYx87mfyw?t=747
* types
* Cython files have a ``.pyx`` extension

.. code-block:: text

    def primes(int kmax):   # The argument will be converted to int or raise a TypeError.
        cdef int n, k, i    # These variables are declared with C types.
        cdef int p[1000]    # Another C type
        result = []         # A Python type

        if kmax > 1000:
            kmax = 1000

        k = 0
        n = 2

        while k < kmax:
            i = 0

            while i < k and n % p[i] != 0:
                i = i + 1

            if i == k:
                p[k] = n
                k = k + 1
                result.append(n)

            n = n + 1
        return result

.. code-block:: text

    In [1]: %load_ext Cython

    In [2]: %%cython
       ...: def f(n):
       ...:     a = 0
       ...:     for i in range(n):
       ...:         a += i
       ...:     return a
       ...:
       ...: cpdef g(int n):
       ...:     cdef int a = 0, i
       ...:     for i in range(n):
       ...:         a += i
       ...:     return a
       ...:

    In [3]: %timeit f(1000000)
    42.7 ms ± 783 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    In [4]: %timeit g(1000000)
    74 µs ± 16.6 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

    # which gives a 585 times improvement over the pure-python version

Cython compiling:

.. figure:: img/performance-cython.png


Numba
-----
Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.

>>> # doctest: +SKIP
... from numba import jit, int32
...
...
... @jit(nogil=True)
... def do_something():
...     pass
...
...
... @jit(int32(int32, int32))
... def add(x, y):
...     return x + y


Dask
----
* https://dask.org

Dask natively scales Python. Dask provides advanced parallelism for
analytics, enabling performance at scale for the tools you love.

Dask's schedulers scale to thousand-node clusters and its algorithms have
been tested on some of the largest supercomputers in the world.

But you don't need a massive cluster to get started. Dask ships with
schedulers designed for use on personal machines. Many people use Dask
today to scale computations on their laptop, using multiple cores for
computation and their disk for excess storage.


Find existing implementation
----------------------------
* https://pypi.org


String Concatenation
--------------------
How many string are there in a memory?:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname + ' ' + lastname
'Mark Watney'

How many string are there in a memory?:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> f'{firstname} {lastname}'
'Mark Watney'

How many string are there in a memory?:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = 42
>>>
>>> 'Hello ' + firstname + ' ' + lastname + ' ' + str(age) + '!'
'Hello Mark Watney 42!'

How many string are there in a memory?:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = 42
>>>
>>> f'Hello {firstname} {lastname} {age}!'
'Hello Mark Watney 42!'


String Append
-------------
* Use ``list.append()`` instead of ``str + str``:

Concatenates strings using + in a loop:

>>> DATA = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>> result = '<table>'
>>>
>>> for element in DATA:
...     result += f'<tr><td>{element}</td></tr>'
>>>
>>> result += '</table>'
>>> print(result)
<table><tr><td>Mark Watney</td></tr><tr><td>Melissa Lewis</td></tr><tr><td>Rick Martinez</td></tr></table>

Problem solved:

>>> DATA = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>> result = ['<table>']
>>>
>>> for element in DATA:
...     result.append(f'<tr><td>{element}</td></tr>')
>>>
>>> result.append('</table>')
>>> print(''.join(result))
<table><tr><td>Mark Watney</td></tr><tr><td>Melissa Lewis</td></tr><tr><td>Rick Martinez</td></tr></table>


Range between two ``float``
---------------------------
* There are indefinitely many values between two floats

>>> range(0, 1)
range(0, 1)

Note, that in Python following code will not execute, as of ``range()`` requires two integers. However similar code with ``numpy.arange()`` will work.

>>> range(0.0, 1.0)  # doctest: +SKIP
0.000...000
0.000...001
0.000...002
0.000...003


Deque
-----
* ``collections.deque`` - Double ended Queue


Further Reading
---------------
* https://wiki.python.org/moin/TimeComplexity
* https://youtu.be/YY7yJHo0M5I
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
* https://www.youtube.com/watch?v=fOdCxum-qLA
* https://www.youtube.com/watch?v=zQeYx87mfyw
* https://www.youtube.com/watch?v=EEUXKG97YRw


References
----------
.. [#Shaw2022] Anthony Shaw. Write faster Python! Common performance anti patterns. Year: 2022. Retrieved: 2022-06-09. URL: https://youtu.be/YY7yJHo0M5I

.. [#Galindo2022] Pablo Galindo. Memray: hardcore memory profiling. Year: 2022. Retrieved: 2022-06-09. URL: https://youtu.be/1IiL31tUEVk?t=1010


Assignments
-----------
.. literalinclude:: assignments/optimization_memoize.py
    :caption: :download:`Solution <assignments/optimization_memoize.py>`
    :end-before: # Solution

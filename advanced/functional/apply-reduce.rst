Functional Reduce
=================
* Reduce sequence using function
* Built-in

In Python, ``reduce()`` is a built-in function that applies a given function
to the elements of an iterable (e.g. a list, tuple, or set) and returns a
single value. The function takes two arguments: the first is the function to
apply, and the second is the iterable to be processed.

The ``reduce()`` function works by applying the function to the first two
elements of the iterable, then to the result and the next element, and so
on, until all elements have been processed and a single value is obtained.

Here's an example:

>>> from functools import reduce
>>>
>>> # Define a list of numbers
>>> numbers = [1, 2, 3, 4, 5]
>>>
>>> # Use reduce() to sum the numbers
>>> result = reduce(lambda x,y: x+y, numbers)
>>>
>>> print(result)
15

In this example, the ``reduce()`` function applies the ``lambda`` function
(which adds two numbers) to the elements of the ``numbers`` list, resulting
in the sum of all the numbers.


SetUp
-----
>>> from functools import reduce


Syntax
------
* ``functools.reduce(function, iterable[, initializer])``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object
* https://docs.python.org/library/functools.html


Problem
-------
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>> result = 0
>>>
>>> for element in DATA:
...     result = add(result, element)
>>>
>>> print(result)
10


Solution
--------
>>> DATA = [1, 2, 3, 4]
>>>
>>>
>>> def add(x, y):
...     return x + y
>>>
>>> reduce(add, DATA)
10


Rationale
---------
* https://docs.python.org/library/operator.html

The ``operator`` module in Python provides a set of functions that implement
common operations on Python objects, such as arithmetic operations,
comparisons, and logical operations. These functions are designed to be used
as functional arguments to other functions, such as ``map()``, ``filter()``,
and ``reduce()``.

The ``operator`` module provides functions for arithmetic operations such as
addition, subtraction, multiplication, division, and exponentiation. It also
provides functions for bitwise operations, such as bitwise AND, OR, XOR, and
shift operations.

In addition to arithmetic and bitwise operations, the ``operator`` module
provides functions for comparisons, such as greater than, less than, equal
to, and not equal to. It also provides functions for logical operations,
such as ``not``, ``and``, and ``or``.

Here's an example of using the ``operator`` module to sort a list of tuples
based on the second element of each tuple:

>>> import operator
>>>
>>> # Define a list of tuples
>>> data = [(2, 'b'), (1, 'a'), (3, 'c')]
>>>
>>> # Sort the list based on the second element of each tuple
>>> sorted_data = sorted(data, key=operator.itemgetter(1))
>>>
>>> print(sorted_data)
[(1, 'a'), (2, 'b'), (3, 'c')]

In this example, the ``itemgetter()`` function from the ``operator`` module
is used as the ``key`` argument to the ``sorted()`` function. This function
returns a callable that extracts the second element of each tuple, which is
used to sort the list.

>>> DATA = [1, 2, 3, 4]
>>>
>>> from operator import mul
>>> reduce(mul, DATA)
24

>>> def add(a, b):
...     print(f'{a=}, {b=}')
...     return a + b
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> reduce(add, data)
a=1, b=2
a=3, b=3
a=6, b=4
10


Use Case - 0x01
---------------
>>> from functools import reduce
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>>
>>> reduce(min, DATA)
1
>>> reduce(max, DATA)
4


Map Reduce
----------
* https://dask.org

Map-Reduce is a programming model for processing large datasets in parallel
across a cluster of computers. The Map-Reduce algorithm consists of two main
phases: the map phase and the reduce phase.

In the map phase, the input data is divided into smaller chunks and
processed in parallel by multiple nodes in the cluster. Each node applies a
mapping function to the input data and produces a set of key-value pairs as
output.

In the reduce phase, the output of the map phase is collected and processed
by a single node in the cluster. The reduce function aggregates the
key-value pairs produced by the map function and produces a final output.

Here's an example of using the Map-Reduce algorithm in Python to count the
number of occurrences of each word in a large text file:

>>> # doctest: +SKIP
... from multiprocessing import Pool
... import collections
...
... # Define the mapping function
... def map_function(line):
...     words = line.strip().split()
...     return [(word, 1) for word in words]
...
... # Define the reduce function
... def reduce_function(key_value_pairs):
...     word_counts = collections.defaultdict(int)
...     for key, value in key_value_pairs:
...         word_counts[key] += value
...     return word_counts.items()
...
... # Read the input file
... with open('/tmp/myfile.txt', mode='r') as input_file:
...     lines = input_file.readlines()
...
... # Divide the input into chunks
... chunk_size = len(lines) // 4
... chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
...
... # Process the chunks in parallel
... with Pool(processes=4) as pool:
...     mapped_results = pool.map(map_function, chunks)
...
... # Collect the output of the map phase
... mapped_output = [item for sublist in mapped_results for item in sublist]
...
... # Group the mapped results by key and reduce the values
... grouped_output = collections.defaultdict(list)
... for key, value in mapped_output:
...     grouped_output[key].append(value)
... reduced_output = reduce_function(grouped_output.items())
...
... # Print the final output
... for word, count in reduced_output:
...     print(word, count)

In this example, the input text file is divided into four chunks, which are
processed in parallel by four processes using the ``Pool`` class from the
``multiprocessing`` module. The ``map_function`` applies a mapping function
to each line of the input file, producing a list of key-value pairs for each
line. The ``reduce_function`` aggregates the key-value pairs produced by the
map function, producing a final output of word counts. The ``defaultdict``
class from the ``collections`` module is used to simplify the code for
grouping and reducing the key-value pairs.

.. figure:: img/idiom-reduce-mapreduce.gif


Assignments
-----------
.. literalinclude:: assignments/idiom_reduce_a.py
    :caption: :download:`Solution <assignments/idiom_reduce_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_reduce_b.py
    :caption: :download:`Solution <assignments/idiom_reduce_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idiom_reduce_c.py
    :caption: :download:`Solution <assignments/idiom_reduce_c.py>`
    :end-before: # Solution

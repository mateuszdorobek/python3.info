Protocol Context Manager
========================
* Files
* Buffering data
* Database connection
* Database transactions
* Database cursors
* Locks
* Network sockets
* Network streams
* HTTP sessions
* Since Python 3.10: Parenthesized context managers [#pydocpython310]_


Protocol
--------
* ``__enter__(self) -> self``
* ``__exit__(self, *args) -> None``

>>> class ContextManager:
...     def __enter__(self):
...         return self
...
...     def __exit__(self, *args):
...         return None
>>>
>>>
>>> with ContextManager() as cm:
...     print('Do something with: cm')
Do something with: cm


Type Annotations
----------------
* ``contextlib.AbstractContextManager``
* ``contextlib.AbstractAsyncContextManager``


Example
-------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __enter__(self):
...         print('Entering the block')
...         return self
...
...     def __exit__(self, *args):
...         print('Exiting the block')
...
...     def say_hello(self):
...         print(f'Hello {self.firstname} {self.lastname}')

Now we can use context manager:

>>> with Astronaut('Mark', 'Watney') as mark:
...     mark.say_hello()
...
Entering the block
Hello Mark Watney
Exiting the block

Is equivalent to:

>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> mark = mark.__enter__()
Entering the block
>>>
>>> mark.say_hello()
Hello Mark Watney
>>>
>>> mark.__exit__()
Exiting the block


Contex Manager
--------------
We need to import ``time()`` function to get current timestamp
(number of seconds from 1970-01-01 00:00:00 UTC):

>>> from time import time

Define our context manager:

>>> class Timeit:
...     def __enter__(self):
...         self.start = time()
...
...     def __exit__(self, *args):
...         self.stop = time()
...         duration = self.stop - self.start
...         print(f'Duration: {duration:.4f} seconds')

>>> # doctest: +SKIP
... with Timeit():
...     result = [x**x for x in range(0, 10_000)]
...
Duration: 5.9882 seconds


Context Decorator Class
-----------------------
* Inherit from ``contextlib.ContextDecorator``
* Class become context manager decorator
* Mind the brackets in decorator ``@Timeit()``

We need to import ``time()`` function to get current timestamp
(number of seconds from 1970-01-01 00:00:00 UTC). Moreover,
this time we need also ``contextlib.ContextDecorator`` for our
class to inherit from:

>>> from time import time
>>> from contextlib import ContextDecorator

Define our context manager:

>>> class Timeit(ContextDecorator):
...     def __enter__(self):
...         self.start = time()
...
...     def __exit__(self, *args):
...         self.stop = time()
...         duration = self.stop - self.start
...         print(f'Duration: {duration:.4f} seconds')

Define the function which will be automatically wrapped by context manager.
Mind the brackets in ``@Timeit()``:

>>> @Timeit()
... def run():
...     result = [x**x for x in range(0, 10_000)]

Calling function will result in executing context manager:

>>> run()  # doctest: +SKIP
Duration: 5.9302 seconds


Context Decorator Function
--------------------------
* Split function for parts before and after ``yield``
* Code before ``yield`` becomes ``__enter__()``
* Code after ``yield`` becomes ``__exit__()``

We need to import ``time()`` function to get current timestamp
(number of seconds from 1970-01-01 00:00:00 UTC):

>>> from time import time
>>> from contextlib import contextmanager

Define our context manager. Mind that Python will split our function
for parts before and after ``yield``. Code before ``yield`` becomes
``__enter__()`` and code after ``yield`` becomes ``__exit__()``:

>>> @contextmanager
... def timeit():
...     start = time()
...     yield
...     end = time()
...     duration = stop - start
...     print(f'Duration: {duration:.4f} seconds')

Now we can use our function as a context manager:

>>> with timeit():  # doctest: +SKIP
...     result = [x**x for x in range(0, 10_000)]
...
Duration 4.0250 seconds


Use Case - 0x01
---------------
>>> from contextlib import contextmanager
>>>
>>>
>>> @contextmanager
... def html_tag(name):
...     print(f'<{name}>')
...     yield
...     print(f'</{name}>')
>>>
>>>
>>> with html_tag('p'):
...     print('We choose to go to the Moon.')
...
<p>
We choose to go to the Moon.
</p>


Use Case - 0x02
---------------
* Files

SetUp:

>>> from pathlib import Path
>>>
>>> Path('/tmp/myfile.txt').touch()

Open/Close:

>>> f = open('/tmp/myfile.txt')
>>>
>>> try:
...     content = f.read()
... finally:
...     f.close()

Context Manager:

>>> with open('/tmp/myfile.txt') as f:
...     content = f.read()

Story about file allocation table:

.. code-block:: console

    $ uptime
    11:29  up 39 days,  2:33, 2 users, load averages: 2.97 4.23 4.41

    $ lsof |wc -l
       12710

.. code-block:: text

    uint32_max = 4_294_967_295
    char* file[uint32_max];

    file_alloc[0] = '/tmp/myfile1.txt'
    file_alloc[1] = '/tmp/myfile2.txt'
    file_alloc[2] = '/tmp/myfile3.txt'
    ...
    file_alloc[4_294_967_294] = '/tmp/myfile4294967294.txt'
    file_alloc[4_294_967_295] = '/tmp/myfile4294967295.txt'
    file_alloc[4_294_967_296] -> KernelPanic


Use Case - 0x03
---------------
* Database

>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         firstname TEXT NOT NULL,
...         lastname TEXT NOT NULL,
...         age INTEGER
...     )
... """
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts VALUES(NULL, :firstname, :lastname, :age)
... """
>>>
>>> SQL_SELECT = """
...     SELECT * FROM astronauts
... """
>>>
>>> DATA = [{'firstname': 'Pan', 'lastname': 'Twardowski', 'age': 44},
...         {'firstname': 'Mark', 'lastname': 'Watney', 'age': 33},
...         {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 36}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:  # doctest: +ELLIPSIS
...     db.execute(SQL_CREATE_TABLE)
...     db.executemany(SQL_INSERT, DATA)
...     db.row_factory = sqlite3.Row
...
...     for row in db.execute(SQL_SELECT):
...         print(dict(row))
...
<sqlite3.Cursor object at 0x...>
<sqlite3.Cursor object at 0x...>
{'id': 1, 'firstname': 'Pan', 'lastname': 'Twardowski', 'age': 44}
{'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'age': 33}
{'id': 3, 'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 36}


Use Case - 0x04
---------------
* Lock

Without context manager:

>>> from threading import Lock
>>>
>>>
>>> lock = Lock()
>>> lock.acquire()
True
>>>
>>> try:
...     print('Critical section 1')
...     print('Critical section 2')
... finally:
...     lock.release()
...
Critical section 1
Critical section 2

With context manager:

>>> from threading import Lock
>>>
>>>
>>> mylock = Lock()
>>>
>>> with mylock:
...     print('Critical section 1')
...     print('Critical section 2')
...
Critical section 1
Critical section 2


Use Case - 0x05
---------------
SetUp:

>>> from threading import Lock

Define decorator to automatically use context manager with lock:

>>> def lock(mylock: Lock):
...     def decorator(func):
...         def wrapper(*args, **kwargs):
...             with mylock:
...                 return func(*args, **kwargs)
...         return wrapper
...     return decorator

Usage:

>>> mylock = Lock()
>>>
>>> @lock(mylock)
... def write(file, content):
...     print(f'Writing "{content}" to {file}')
>>>
>>>
>>> write(file='/tmp/myfile.txt', content='hello')
Writing "hello" to /tmp/myfile.txt


Use Case - 0x06
---------------
* Microbenchmark

SetUp:

>>> from time import time

Define Context Manager to measure start, stop times and calculate duration:

>>> class Timeit:
...     def __enter__(self):
...         self.start = time()
...
...     def __exit__(self, *args):
...         self.stop = time()
...         duration = self.stop - self.start
...         print(f'Duration: {duration:.4f} seconds')

Let's define some constants for tests:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> repetitions = 10_000_000

Microbenchmark for concatenation using ``f-string``:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         f'{firstname}{lastname}'
Duration: 1.3408 seconds

Microbenchmark for concatenation using add (``+``) operator:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         firstname + lastname
Duration: 1.2745 seconds

Microbenchmark for concatenation using modulo (``%``) operator:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         '%s%s' % (firstname, lastname)
Duration: 2.1886 seconds

Microbenchmark for concatenation using modulo (``%``) operator:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         '%(fname)s%(lname)s' % {'fname': firstname, 'lname': lastname}
Duration: 4.1019 seconds

Microbenchmark for concatenation using ``str.format()`` method:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         '{}{}'.format(firstname, lastname)
Duration: 2.6623 seconds

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         '{0}{1}'.format(firstname, lastname)
Duration: 2.7617 seconds

Microbenchmark for concatenation using ``str.format()`` method:

>>> with Timeit():  # doctest: +SKIP
...     for _ in range(repetitions):
...         '{fname}{lname}'.format(fname=firstname, lname=lastname)
Duration: 5.3505 seconds


Use Case - 0x07
---------------
>>> from unittest import IsolatedAsyncioTestCase
>>> import httpx as httpx  # doctest: +SKIP
>>>
>>> BASE_URL = 'https://python3.info'
>>>
>>>
>>> async def request(method='GET', path='/', data=None):
...     async with httpx.AsyncClient(base_url=BASE_URL) as client:
...         return await client.request(method=method, url=path, data=data)
...
...
>>> class MyAppTest(IsolatedAsyncioTestCase):
...     async def test_index(self):
...         resp = await request('GET', '/index.html')
...         self.assertEqual(resp.status_code, 200)
...
...     async def test_license(self):
...         resp = await request('GET', '/LICENSE.html')
...         self.assertEqual(resp.status_code, 200)
...         text = 'Creative Commons Attribution-ShareAlike 4.0 International Public License'
...         self.assertIn(text, resp.text)
...
...     async def test_install(self):
...         resp = await request('GET', '/install.html')
...         self.assertEqual(resp.status_code, 200)
...
...         with self.subTest(msg='Python Version'):
...             self.assertIn('3.11', resp.text)
...             self.assertIn('3.10', resp.text)
...             self.assertIn('3.9', resp.text)
...             self.assertNotIn('3.8', resp.text)
...             self.assertNotIn('3.7', resp.text)
...             self.assertNotIn('3.6', resp.text)
...
...         with self.subTest(msg='PyCharm Version'):
...             self.assertIn('2022.1', resp.text)
...             with self.assertRaises(AssertionError):
...                 self.assertIn('2022.0', resp.text)


Use Case - 0x08
---------------
* Source [#sqlalchemySessions]_

In the most general sense, the Session establishes all conversations with
the database and represents a 'holding zone' for all the objects which
you've loaded or associated with it during its lifespan. It provides the
interface where SELECT and other queries are made that will return and
modify ORM-mapped objects. The ORM objects themselves are maintained
inside the Session, inside a structure called the identity map - a data
structure that maintains unique copies of each object, where 'unique'
means 'only one object with a particular primary key'.

>>> # doctest: +SKIP
... from sqlalchemy import create_engine
... from sqlalchemy.orm import Session
...
... engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")

Create session and add objects:

>>> # doctest: +SKIP
... with Session(engine) as session:
...     session.add(some_object)
...     session.add(some_other_object)
...     session.commit()

The long-form sequence of operations illustrated above can be achieved more
succinctly by making use of the SessionTransaction object returned by the
Session.begin() method, which provides a context manager interface for the
same sequence of operations:

>>> # doctest: +SKIP
... with Session(engine) as session:
...     with session.begin():
...         session.add(some_object)
...         session.add(some_other_object)

Create session and add objects. Inner context calls session.commit(),
if there were no exceptions. Outer context calls session.close()

There could be several context managers entered at the same time:

>>> # doctest: +SKIP
... with Session(engine) as session, session.begin():
...     session.add(some_object)
...     session.add(some_other_object)

Create session and add objects. Inner context calls session.commit(),
if there were no exceptions. Outer context calls session.close()


References
----------
.. [#sqlalchemySessions] SQLAlchemy authors and contributors. Session Basics. Year: 2022. Retrieved: 2022-11-25. URL: https://docs.sqlalchemy.org/en/20/orm/session_basics.html
.. [#pydocpython310] Python Software Foundation. Parenthesized context managers. Year: 2022. Retrieved: 2022-12-03. URL: https://docs.python.org/dev/whatsnew/3.10.html#parenthesized-context-managers


Assignments
-----------
.. literalinclude:: assignments/protocol_contextmanager_a.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_contextmanager_b.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_contextmanager_c.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_c.py>`
    :end-before: # Solution

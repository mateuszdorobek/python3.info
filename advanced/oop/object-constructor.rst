OOP Object Constructor
======================
In Python, ``__new__`` and ``__init__`` are two special methods that
are used in the creation of objects. ``__new__`` is a static method
that is responsible for creating an instance of a class. It takes the
class as its first argument and returns a new instance of the class.
It is called before the ``__init__`` method. ``__init__`` is an instance
method that is responsible for initializing the instance of a class that
was created by the ``__new__`` method. It takes the instance as its first
argument and initializes its attributes.

In other words, ``__new__`` creates the object and ``__init__``
initializes it. You can think of ``__new__`` as the constructor
of the class and ``__init__`` as the initializer of the instance.

In Python by definition both methods ``__new__()`` and ``__init__()``
combined and called consecutively are constructors. This is something
which is not existing in other programming languages, hence programmers
has problem with grasping this idea. In most cases people will take their
"experience" and "habits" from other languages, mixed with vogue knowledge
about ``__new__()`` and call ``__init__()`` a constructor.

In Object Oriented Programming constructor is:

    a. Special method
    b. Called automatically on object creation
    c. Can set instance attributes with initial values
    d. Works on not fully created object
    e. Method calls are not allowed (as of object is not ready)
    f. Returns None

Python ``__init__()`` method:

    a. Yes
    b. Yes
    c. Yes
    d. No
    e. No
    f. Yes

Python ``__new__()`` method:

    a. Yes
    b. Yes
    c. Yes (could be)
    d. Yes
    e. Yes (before instantiating) / No (after instantiating)
    f. No

Method ``__new__`` will always get called when an object has to be created.
There are some situations where ``__init__`` will not get called. One example
is when you unpickle objects from a pickle file, they will get allocated
(``__new__``) but not initialised (``__init__``) [#Noufal2011]_.


Example
-------
>>> class User:
...     def __new__(cls, *args, **kwargs):
...         print('New: before instantiating')
...         result = super().__new__(cls, *args, **kwargs)
...         print('New: after instantiating')
...         return result
...
...     def __init__(self):
...         print('Init: initializing')
>>>
>>>
>>> mark = User()
New: before instantiating
New: after instantiating
Init: initializing


New Method
----------
* object constructor
* solely for creating the object
* ``cls`` as it's first parameter
* when calling ``__new__()`` you actually don't have an instance yet,
  therefore no ``self`` exists at that moment

Called to create a new instance of class ``cls``. ``__new__()`` is a static
method (special-cased so you need not declare it as such) that takes the
class of which an instance was requested as its first argument. The remaining
arguments are those passed to the object constructor expression (the call
to the class). The return value of ``__new__()`` should be the new object
instance (usually an instance of ``cls``) [#pydocDatamodelNew]_.

Typical implementations create a new instance of the class by invoking the
superclass's ``__new__()`` method using ``super().__new__(cls[, ...])`` with
appropriate arguments and then modifying the newly-created instance as
necessary before returning it [#pydocDatamodelNew]_.

If ``__new__()`` is invoked during object construction and it returns an
instance of ``cls``, then the new instance's ``__init__()`` method will be
invoked like ``__init__(self[, ...])``, where ``self`` is the new instance and
the remaining arguments are the same as were passed to the object constructor.
If ``__new__()`` does not return an instance of ``cls``, then the new
instance's ``__init__()`` method will not be invoked [#pydocDatamodelNew]_.

``__new__()`` is intended mainly to allow subclasses of immutable types
(like ``int``, ``str``, or ``tuple``) to customize instance creation.
It is also commonly overridden in custom metaclasses in order to customize
class creation [#pydocDatamodelNew]_.

>>> class User:
...     def __new__(cls):
...         print('Constructing object')
...         return super().__new__(cls)
>>>
>>>
>>> mark = User()
Constructing object


Init Method
-----------
* object initializer
* for initializing object with initial values
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance
  is in place, so you can use ``self`` with it
* it's purpose is just to alter the fresh state of the newly created
  instance

Called after the instance has been created (by ``__new__()``), but before
it is returned to the caller. The arguments are those passed to the
class constructor expression. If a base class has an ``__init__()`` method,
the derived class's ``__init__()`` method, if any, must explicitly call it
to ensure proper initialization of the base class part of the instance;
for example: ``super().__init__([args...])`` [#pydocDatamodelInit]_.

>>> class User:
...     def __init__(self):
...         print('Initializing object')
>>>
>>>
>>> mark = User()
Initializing object

Because ``__new__()`` and ``__init__()`` work together in constructing objects
(``__new__()`` to create it, and ``__init__()`` to customize it), no non-None
value may be returned by ``__init__()``; doing so will cause a ``TypeError``
to be raised at runtime.

>>> class User:
...     def __init__(self):
...         print('Initializing object')
...         return True
>>>
>>>
>>> mark = User()
Traceback (most recent call last):
TypeError: __init__() should return None, not 'bool'


Return
------
>>> class User:
...     def __new__(cls):
...         print('Constructing object')
...         return super().__new__(cls)
...
...     def __init__(self):
...         print('Initializing object')
>>>
>>>
>>> mark = User()
Constructing object
Initializing object

Missing ``return`` from constructor. The instantiation is evaluated to
``None`` since we don't return anything from the constructor:

>>> class User:
...     def __new__(cls):
...         print('Constructing object')
...         super().__new__(cls)
...
...     def __init__(self):
...         print('Initializing object')  # -> is actually never called
>>>
>>>
>>> mark = User()
Constructing object
>>>
>>> type(mark)
<class 'NoneType'>

Return invalid from constructor:

>>> class User:
...     def __new__(cls):
...         return 'Mark Watney'
>>>
>>> mark = User()
>>>
>>> type(mark)
<class 'str'>
>>>
>>> mark
'Mark Watney'

Return invalid from initializer:

>>> class User:
...     def __init__(self):
...         return 'Mark Watney'
>>>
>>> mark = User()
Traceback (most recent call last):
TypeError: __init__() should return None, not 'str'


Injecting New
-------------
>>> from datetime import datetime
>>> import logging
>>> from uuid import uuid4
>>>
>>>
>>> def trace_object(cls, *args, **kwargs):
...     instance = object.__new__(cls)
...     instance._log = logging.getLogger(f'{cls.__name__}')
...     instance._since = datetime.now()
...     instance._uuid = str(uuid4())
...     return instance


Without injecting:

>>> class User:
...     pass
>>>
>>> mark = User()
>>> vars(mark)
{}

With injecting:

>>> class User:
...     pass
>>>
>>> User.__new__ = trace_object
>>>
>>> mark = User()
>>> vars(mark)  # doctest: +SKIP
{'_log': <Logger myapp.User (INFO)>,
 '_since': datetime.datetime(1969, 7, 21, 2, 56, 15),
 '_uuid': '971827b5-5bc5-4a4b-9c8a-ecf5e4dbcfe3'}


Do not Trigger Methods for User
-------------------------------
* It is better when user can choose a moment when call ``.connect()`` method

Let user to call method:

>>> class Server:
...     def __init__(self, host, username, password=None):
...         self.host = host
...         self.username = username
...         self.password = password
...         self.connect()    # Better ask user to ``connect()`` explicitly
...
...     def connect(self):
...         print(f'Logging to {self.host} using: {self.username}:{self.password}')
>>>
>>>
>>> connection = Server(
...     host='example.com',
...     username='admin',
...     password='myVoiceIsMyPassword')
Logging to example.com using: admin:myVoiceIsMyPassword

Let user to call method:

>>> class Server:
...     def __init__(self, host, username, password=None):
...         self.host = host
...         self.username = username
...         self.password = password
...
...     def connect(self):
...         print(f'Logging to {self.host} using: {self.username}:{self.password}')
>>>
>>>
>>> connection = Server(
...     host='example.com',
...     username='admin',
...     password='myVoiceIsMyPassword')
>>>
>>> connection.connect()
Logging to example.com using: admin:myVoiceIsMyPassword

However it is better to use ``self.set_position(position_x, position_y)``
than to set those values one by one and duplicate code. Imagine if there
will be a condition boundary checking (for example for negative values):

>>> class PositionBad:
...     def __init__(self, position_x=0, position_y=0):
...         self.position_x = position_x
...         self.position_y = position_y
...
...     def set_position(self, x, y):
...         self.position_x = x
...         self.position_y = y
>>>
>>>
>>> class PositionGood:
...     def __init__(self, position_x=0, position_y=0):
...         self.set_position(position_x, position_y)
...
...     def set_position(self, x, y):
...         self.position_x = x
...         self.position_y = y

>>> class PositionBad:
...     def __init__(self, position_x=0, position_y=0):
...         self.position_x = min(1024, max(0, position_x))
...         self.position_y = min(1024, max(0, position_y))
...
...     def set_position(self, x, y):
...         self.position_x = min(1024, max(0, x))
...         self.position_y = min(1024, max(0, y))
>>>
>>>
>>> class PositionGood:
...     def __init__(self, position_x=0, position_y=0):
...         self.set_position(position_x, position_y)
...
...     def set_position(self, x, y):
...         self.position_x = min(1024, max(0, x))
...         self.position_y = min(1024, max(0, y))


Use Case - 0x01
---------------
* Iris Factory

>>> from dataclasses import dataclass, field
>>> from itertools import starmap
>>>
>>>
>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str = field(repr=False)
...
...     def __new__(cls, *args, **kwargs):
...         *measurements, species = args
...         clsname = species.capitalize()
...         cls = globals()[clsname]
...         return super().__new__(cls)
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> result = starmap(Iris, DATA)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x02
---------------
* Path

Note, that this unfortunately does not work this way. ``Path()`` always returns ``PosixPath``:

>>> from pathlib import Path
>>>
>>>
>>> Path('/etc/passwd')
PosixPath('/etc/passwd')
>>>
>>> Path('c:\\Users\\Admin\\myfile.txt')  # doctest: +SKIP
WindowsPath('c:\\Users\\Admin\\myfile.txt')
>>>
>>> Path(r'C:\Users\Admin\myfile.txt')  # doctest: +SKIP
WindowsPath('C:\\Users\\Admin\\myfile.txt')
>>>
>>> Path(r'C:/Users/Admin/myfile.txt')  # doctest: +SKIP
WindowsPath('C:/Users/Admin/myfile.txt')


Use Case - 0x03
---------------
* Document Factory
* Factory method
* Could be used to implement Singleton

>>> class PDF:
...     pass
>>>
>>> class Docx:
...     pass
>>>
>>> class Document:
...     def __new__(cls, *args, **kwargs):
...         filename, extension = args[0].split('.')
...         if extension == 'pdf':
...             return PDF()
...         elif extension == 'docx':
...             return Docx()
>>>
>>>
>>> file1 = Document('myfile.pdf')
>>> file2 = Document('myfile.docx')
>>>
>>> print(file1)  # doctest: +ELLIPSIS
<__main__.PDF object at 0x...>
>>>
>>> print(file2)  # doctest: +ELLIPSIS
<__main__.Docx object at 0x...>


Use Case - 0x04
---------------
* Document Factory

>>> class Docx:
...     pass
>>>
>>> class PDF:
...     pass
>>>
>>> class Document:
...     def __new__(cls, filename):
...         basename, extension = filename.split('.')
...         match extension:
...             case 'pdf':             return PDF()
...             case 'doc' | 'docx':    return Docx()
>>>
>>>
>>> file1 = Document('myfile.pdf')
>>> file2 = Document('myfile.docx')
>>> file3 = Document('myfile.doc')
>>>
>>> print(file1)  # doctest: +ELLIPSIS
<__main__.PDF object at 0x...>
>>>
>>> print(file2)  # doctest: +ELLIPSIS
<__main__.Docx object at 0x...>
>>>
>>> print(file3)  # doctest: +ELLIPSIS
<__main__.Docx object at 0x...>


Use Case - 0x05
---------------
* Document Factory

>>> from abc import ABC, abstractmethod, abstractproperty
>>>
>>>
>>> class Document(ABC):
...     @abstractproperty
...     def EXTENSIONS(self) -> list[str]:
...         ...
...
...     @abstractmethod
...     def display(self):
...         ...
...
...     def __init__(self, filename):
...         self.filename = filename
...
...     def __str__(self):
...         return self.filename
...
...     def __new__(cls, filename):
...         extension = filename.split('.')[-1]
...         plugins = cls.__subclasses__()
...         for plugin in plugins:
...             if extension in plugin.EXTENSIONS:
...                 instance = object.__new__(plugin)
...                 instance.__init__(filename)
...                 return instance
...         else:
...             raise NotImplementedError('No plugin for this filetype')
>>>
>>>
>>> class PDF(Document):
...     EXTENSIONS = ['pdf']
...
...     def display(self):
...         print(f'Displaying PDF file {self.filename}')
>>>
>>>
>>> class Word(Document):
...     EXTENSIONS = ['docx', 'doc']
...
...     def display(self):
...         print(f'Displaying Word file {self.filename}')
>>>
>>>
>>> file = Document('myfile.pdf')
>>> file.display()
Displaying PDF file myfile.pdf
>>>
>>> file = Document('myfile.doc')
>>> file.display()
Displaying Word file myfile.doc
>>>
>>> file = Document('myfile.docx')
>>> file.display()
Displaying Word file myfile.docx

Plugins can be hot-plugged. This means that you can attach a new plugin
without reloading server code or application. Just define a class which
conforms to Plugin protocol (inherits from abstract base class Document)
and it will work. No reloads nor restarts. That's it.

>>> file = Document('myfile.txt')
Traceback (most recent call last):
NotImplementedError: No plugin for this filetype
>>>
>>>
>>> class Plaintext(Document):
...     EXTENSIONS = ['txt']
...
...     def display(self):
...         print(f'Displaying Plaintext file {self.filename}')
>>>
>>>
>>> file = Document('myfile.txt')
>>> file.display()
Displaying Plaintext file myfile.txt


Use Case - 0x06
---------------
>>> from datetime import datetime, timezone
>>> import logging
>>> from uuid import uuid4
>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class BaseClass(ABC):
...     def __new__(cls, *args, **kwargs):
...         obj = object.__new__(cls)
...         obj._since = datetime.now(timezone.utc)
...         obj._uuid = str(uuid4())
...         obj._logger = logging.getLogger(cls.__name__)
...         return obj
...
...     def _log(self, level: int, id: int, msg: str):
...         self._logger.log(level, f'[{level}:{id}] {msg}')
...
...     def _debug(self, id:int, msg:str):    self._log(logging.DEBUG, id, msg)
...     def _info(self, id:int, msg:str):     self._log(logging.INFO, id, msg)
...     def _warning(self, id:int, msg:str):  self._log(logging.WARNING, id, msg)
...     def _error(self, id:int, msg:str):    self._log(logging.ERROR, id, msg)
...     def _critical(self, id:int, msg:str): self._log(logging.CRITICAL, id, msg)
...
...     @abstractmethod
...     def __init__(self):
...         pass
>>>
>>>
>>> class User(BaseClass):
...     def __init__(self, *args, **kwargs):
...         ...
>>>
>>>
>>> mark = User()
>>>
>>> vars(mark)  # doctest: +SKIP +NORMALIZE_WHITESPACE
{'_since': datetime.datetime(1969, 7, 21, 2, 56, 15),
 '_uuid': '83cefe23-3491-4661-b1f4-3ca570feab0a',
 '_log': <Logger User (WARNING)>}
>>>
>>> mark._error(123456, 'An error occurred')  # doctest: +SKIP
1969-07-21T02:56:15Z [ERROR:123456] An error occurred


References
----------
.. [#Noufal2011] Noufal Ibrahim. Python (and Python C API): __new__ versus __init__. Year: 2011. Retrieved: 2022-03-09. URL: https://stackoverflow.com/a/5143108


.. [#pydocDatamodelNew] Basic customization. object.__new__(cls[, ...]). Year: 2022. Retrieved: 2022-04-01. URL: https://docs.python.org/3/reference/datamodel.html#object.__new__

.. [#pydocDatamodelInit] object.__init__(self[, ...]). Year: 2022. Retrieved: 2022-04-01. URL: https://docs.python.org/3/reference/datamodel.html#object.__init__


Assignments
-----------
.. literalinclude:: assignments/oop_object_constructor_a.py
    :caption: :download:`Solution <assignments/oop_object_constructor_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_object_constructor_b.py
    :caption: :download:`Solution <assignments/oop_object_constructor_b.py>`
    :end-before: # Solution

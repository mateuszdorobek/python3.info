OOP Abstract Protocol
=====================
* :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.8
* Protocol describe an interface, not an implementation
* Protocol classes should not have method implementations
* Protocol can describe both methods and attributes

A class object is considered an implementation of a protocol if accessing
all members on it results in types compatible with the protocol members.

All things protocol related resides in typing library in ``Protocol`` class:

>>> from typing import Protocol, Self, runtime_checkable, NamedTuple

Typical protocol implementation looks like that:

>>> class Message(Protocol):
...     recipient: str
...     body: str
...
...     def send() -> None: ...
...     def receive() -> Self: ...


Example
-------
In Python there is a ``Context Manager`` protocol. In order to conform
to this protocol, your class needs to define two methods: ``__enter__()``
and ``__exit__()``. When you have both of those methods, you can use it
in the ``with`` statement. There is no checking if you have certain type
or your class inherits from some kind of abstract. Just define two methods
and your good to go.

>>> class MyFile:
...     def __enter__(self):
...         return ...
...
...     def __exit__(self, exc_type, exc_val, exc_tb):
...         ...
>>>
>>>
>>> with MyFile() as file:
...     pass

Note, that there is no explicit information, that your code implements
the protocol. This is called ``structural subtyping``.

The intuitive implementation of the protocol might look like:

>>> class ContextManager(Protocol):
...     def __enter__(self): ...
...     def __exit__(self, exc_type, exc_val, exc_tb): ...

Which enables it use it in the with statement:

>>> cm: ContextManager
>>>
>>> with cm() as variable:  # doctest: +SKIP
...     ...

Note, that the above code is just only to demonstrate the example and
it is not intended run. Executing it will result in ``SyntaxError``
exception.


Standard Library Protocols
--------------------------
* ``from collections.abc import *``
* ``Container``
* ``Hashable``
* ``Iterable``
* ``Iterator``
* ``Reversible``
* ``Generator``
* ``Callable``
* ``Collection``
* ``Sequence``
* ``MutableSequence``
* ``ByteString``
* ``Set``
* ``MutableSet``
* ``Mapping``
* ``MutableMapping``
* ``MappingView``
* ``ItemsView``
* ``KeysView``
* ``ValuesView``
* ``Awaitable``
* ``Coroutine``
* ``AsyncIterator``
* ``AsyncGenerator``

.. csv-table:: Protocols
    :header: "Abstract Base Class", "Inherits from", "Methods"
    :widths: 15, 15, 60

    "Container",           "",                           "``__contains__``"
    "Hashable",            "",                           "``__hash__``"
    "Iterable",            "",                           "``__iter__``"
    "Iterator",            "Iterable",                   "``__next__``, ``__iter__``"
    "Reversible",          "Iterable",                   "``__reversed__``"
    "Generator",           "Iterator",                   "``send``, ``throw``, ``close``, ``__iter__``, ``__next__``, ``__len__``"
    "Callable",            "",                           "``__call__``"
    "Collection",          "Sized, Iterable, Container", "``__contains__``, ``__iter__``, ``__len__``"
    "Sequence",            "Reversible, Collection",     "``__getitem__``, ``__contains__``, ``__iter__``, ``__reversed__``, ``__len__``, ``index``, ``count``"
    "MutableSequence",     "Sequence",                   "``__getitem__``, ``__setitem__``, ``append``, ``reverse``, ``extend``, ``pop``, ``__delitem__``, ``remove``, ``__iadd__``, ``__len__``, ``insert``, ``__contains__``, ``__iter__``, ``__reversed__``, ``index``, ``count``"
    "ByteString",          "Sequence",                   "``__getitem__``, ``__len__``, ``__contains__``, ``__iter__``, ``__reversed__``, ``index``, ``count``"
    "Set",                 "Collection",                 "``__contains__``, ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``, ``__iter__``, ``__gt__``, ``__ge__``, ``__and__``, ``__or__``, ``__len__``, ``__sub__``, ``__xor__``, ``isdisjoint``"
    "MutableSet",          "Set",                        "``__contains__``, ``__iter__``, ``clear``, ``pop``, ``remove``, ``__ior__``, ``__len__``, ``__iand__``, ``__ixor__``, ``__isub__``, ``add``, ``discard``, ``__contains__``, ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``, ``__iter__``, ``__gt__``, ``__ge__``, ``__and__``, ``__or__``, ``__len__``, ``__sub__``, ``__xor__``, ``isdisjoint``"
    "Mapping",             "Collection",                 "``__getitem__``, ``__contains__``, ``keys``, ``items``, ``values``, ``__iter__``, ``get``, ``__eq__``, ``__ne__``, ``__len__``"
    "MutableMapping",      "Mapping",                    "``__getitem__``, ``__setitem__``, ``pop``, ``popitem``, ``clear``, ``update``, ``__delitem__``, ``setdefault``, ``__iter__``, ``__len__``, ``__getitem__``, ``__contains__``, ``keys``, ``items``, ``values``, ``__iter__``, ``get``, ``__eq__``, ``__ne__``, ``__len__``"
    "MappingView",         "Sized",                      "``__len__``"
    "ItemsView",           "MappingView, Set",           "``__contains__``, ``__iter__``"
    "KeysView",            "MappingView, Set",           "``__contains__``, ``__iter__``"
    "ValuesView",          "MappingView, Collection",    "``__contains__``, ``__iter__``"
    "Awaitable",           "",                           "``__await__``"
    "Coroutine",           "Awaitable, AsyncIterable",   "``send``, ``throw``, ``close``, ``__aiter__``"
    "AsyncIterator",       "AsyncIterable",              "``__anext__``, ``__aiter__``"
    "AsyncGenerator",      "AsyncIterator",              "``asend``, ``athrow``, ``aclose``, ``__aiter__``, ``__anext__``"


Terminology
-----------
:pep:`544` propose to use the term protocols for types supporting structural
subtyping. The reason is that the term iterator protocol, for example, is
widely understood in the community, and coming up with a new term for this
concept in a statically typed context would just create confusion
[#PEP544]_.

This has the drawback that the term protocol becomes overloaded with two
subtly different meanings: the first is the traditional, well-known but
slightly fuzzy concept of protocols such as iterator; the second is the
more explicitly defined concept of protocols in statically typed code. The
distinction is not important most of the time, and in other cases we
propose to just add a qualifier such as protocol classes when referring to
the static type concept. [#PEP544]_

If a class includes a protocol in its MRO, the class is called an explicit
subclass of the protocol.

If a class is a structural subtype of a protocol, it is said to implement
the protocol and to be compatible with a protocol. If a class is compatible
with a protocol but the protocol is not included in the MRO, the class is
an implicit subtype of the protocol. (Note that one can explicitly subclass
a protocol and still not implement it if a protocol attribute is set to
None in the subclass, see Python data-model for details.) [#PEP544]_

The attributes (variables and methods) of a protocol that are mandatory for
other class in order to be considered a structural subtype are called
protocol members. [#PEP544]_


Explicit Subtyping
------------------
* ``Email`` is explicit subclass of the protocol

If a class includes a protocol in its MRO, the class is called an explicit
subclass of the protocol.

>>> class Message(Protocol):
...     recipient: str
...     body: str

>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> def send(message: Message):
...     ...
>>>
>>>
>>> email = Email()
>>> email.sender = 'mwatney@nasa.gov'
>>> email.recipient = 'mlewis@nasa.gov'
>>> email.subject = 'I am alive!'
>>> email.body = 'I survived the storm. I am alone on Mars.'
>>>
>>> send(email)  # will pass the checker


Structural Subtyping
--------------------
* If an object that has all the protocol attributes it implements it
* Structural subtyping is natural for Python programmers
* Matches the runtime semantics of duck typing
* ``Email`` is structural subtype of a protocol (it conforms to structure)
* ``Email`` is implicit subtype of the protocol ``Message`` (not inherits)
* ``Email`` implement the protocol ``Message``
* ``Email`` is compatible with a protocol ``Message``

If a class is a structural subtype of a protocol, it is said to implement
the protocol and to be compatible with a protocol. If a class is compatible
with a protocol but the protocol is not included in the MRO, the class is
an implicit subtype of the protocol. (Note that one can explicitly subclass
a protocol and still not implement it if a protocol attribute is set to
None in the subclass, see Python data-model for details.) [#PEP544]_

>>> class Message(Protocol):
...     recipient: str
...     body: str

>>> class Email:
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> def send(message: Message):
...     ...
>>>
>>>
>>> email = Email()
>>> email.sender = 'mwatney@nasa.gov'
>>> email.recipient = 'mlewis@nasa.gov'
>>> email.subject = 'I am alive!'
>>> email.body = 'I survived the storm. I am alone on Mars.'
>>>
>>> send(email)  # will pass the checker


What Protocols are Not?
-----------------------
* At runtime, protocol classes is simple ABC
* No runtime type check
* Protocols are completely optional

At runtime, protocol classes will be simple ABCs. There is no intent to
provide sophisticated runtime instance and class checks against protocol
classes. This would be difficult and error-prone and will contradict the
logic of :pep:`484`. As well, following :pep:`484` and :pep:`526` Python
steering committee states that protocols are completely optional [#PEP544]_:

* No runtime semantics will be imposed for variables or parameters
  annotated with a protocol class.
* Any checks will be performed only by third-party type checkers and other
  tools.
* Programmers are free to not use them even if they use type annotations.
* There is no intent to make protocols non-optional in the future.

>>> class SMS(Protocol):
...     recipient: str
...     body: str
>>>
>>> class MMS(Protocol):
...     recipient: str
...     body: str
...     mimetype: str

>>> class MyMessage:
...     recipient: str
...     body: str
>>>
>>>
>>> a: SMS = MyMessage()  # Ok
>>> b: MMS = MyMessage()  # Expected type 'MMS', got 'MyMessage' instead


Covariance, Contravariance, Invariance
--------------------------------------
* https://www.youtube.com/watch?v=1IiL31tUEVk&t=445s
* Covariance - Enables you to use a more derived type than originally specified
* Contravariance - Enables you to use a more generic (less derived) type than originally specified
* Invariance - Means that you can use only the type originally specified.
* Invariance is important for example in ``np.ndarray``, where all items must be exactly the same type

Covariance and contravariance are terms that refer to the ability to use a
more derived type (more specific) or a less derived type (less specific)
than originally specified. Generic type parameters support covariance and
contravariance to provide greater flexibility in assigning and using
generic types [#MicrosoftGenericsCovContra]_

In general, a covariant type parameter can be used as the return type of a
delegate, and contravariant type parameters can be used as parameter types.

>>> def check(what: int):
...     pass

>>> bool.mro()
[<class 'bool'>, <class 'int'>, <class 'object'>]

.. glossary::

    Covariance
        Enables you to use a more derived type than originally specified
        [#MicrosoftGenericsCovContra]_

        >>> check(True)     # ok
        >>> check(1)        # ok
        >>> check(object)   # error

    Contravariance
        Enables you to use a more generic (less derived) type than
        originally specified [#MicrosoftGenericsCovContra]_

        >>> check(True)     # error
        >>> check(1)        # ok
        >>> check(object)   # ok

    Invariance
        Means that you can use only the type originally specified. An
        invariant generic type parameter is neither covariant nor
        contravariant [#MicrosoftGenericsCovContra]_

        >>> check(True)     # error
        >>> check(1)        # ok
        >>> check(object)   # error

.. figure:: img/oop-protocol-covariance.png

    Covariance. Replacement with more specialized type.
    Dog is more specialized than Animal. [#Langa2022]_

.. figure:: img/oop-protocol-contravariance.png

    Contravariance. Replacement with more generic type.
    Animal is more generic than Cat. [#Langa2022]_

.. figure:: img/oop-protocol-contravariance.png

    Invariance. Type must be the same and you cannot replace it.
    Animal cannot be substituted for Cat and vice versa. [#Langa2022]_


Example:

By default type annotation checkers works in covariant mode:

>>> def print_coordinates(point: tuple):
...     x, y, z = point
...     print(f'{x=}, {y=}, {z=}')

This means, that the ``point`` argument to the ``print_coordinates`` function
could be either ``tuple`` or any object which inherits from ``tuple``.

In the following example ``pt`` is **invariant** type as it is exactly as
required, that is ``tuple``:

>>> pt = (1, 2, 3)
>>> print_coordinates(pt)
x=1, y=2, z=3

``NamedTuple`` inherits from ``tuple``, so it could be used as **covariant**
type:

>>> class Point(NamedTuple):
...     x: int
...     y: int
...     z: int
>>>
>>> pt = Point(1,2,3)
>>> print_coordinates(pt)
x=1, y=2, z=3


Default Value
-------------
>>> class Astronaut(Protocol):
...     firstname: str
...     lastname: str
...     job: str = 'astronaut'


Merging and extending protocols
-------------------------------
>>> from typing import Sized, Protocol
>>>
>>>
>>> class Closable(Protocol):
...     def close(self) -> None:
...         ...
>>>
>>> class SizableAndClosable(Sized, Closable, Protocol):
...     pass


Generic Protocols
-----------------
>>> from abc import abstractmethod
>>> from typing import Protocol, TypeVar, Iterator
>>>
>>>
>>> T = TypeVar('T')
>>>
>>> class Iterable(Protocol[T]):
...     @abstractmethod
...     def __iter__(self) -> Iterator[T]:
...         ...


Recursive Protocols
-------------------
* Since 3.11 :pep:`673` –- Self Type
* Since 3.7 ``from __future__ import annotations``
* Future :pep:`563` -- Postponed Evaluation of Annotations

>>> from typing import Protocol, Iterable, Self

Traversing Graph nodes:

>>> class Graph(Protocol):
...     def get_node(self) -> Iterable[Self]:
...         ...

Traversing Tree nodes:

>>> class Tree(Protocol):
...     def get_node(self) -> Iterable[Self]:
...         ...


Unions
------
>>> class Exitable(Protocol):
...     def exit(self) -> int:
...         ...
>>>
>>> class Quittable(Protocol):
...     def quit(self) -> int | None:
...         ...

>>> def finish(task: Exitable | Quittable) -> None:
...     task.exit()
...     task.quit()


Modules as implementations of protocols
---------------------------------------
A module object is accepted where a protocol is expected if the public
interface of the given module is compatible with the expected protocol. For
example:

File ``config.py``:

>>> database_host = '127.0.0.1'
>>> database_port = 5432
>>> database_name = 'ares3'
>>> database_user = 'mwatney'
>>> database_pass = 'myVoiceIsMyPassword'

File ``main.py``:

>>> from typing import Protocol
>>>
>>>
>>> class DatabaseConfig(Protocol):
...     database_host: str
...     database_port: int
...     database_name: str
...     database_user: str
...     database_pass: str
>>>
>>>
>>> import config  # doctest: +SKIP
>>> dbconfig: DatabaseConfig = config # Passes type check  # doctest: +SKIP


Callbacks
---------
File ``myrequest.py``:

>>> URL = 'https://python.astrotech.io'
>>>
>>> def on_success(result: str) -> None:
...     ...
>>>
>>> def on_error(error: Exception) -> None:
...     ...

File ``main.py``:

>>> from typing import Protocol
>>>
>>>
>>> class Request(Protocol):
...     URL: str
...     def on_success(self, result: str) -> None: ...
...     def on_error(self, error: Exception) -> None: ...
>>>
>>>
>>> import myrequest  # doctest: +SKIP
>>> request: Request = myrequest  # Passes type check  # doctest: +SKIP


Runtime Checkable
-----------------
* By default ``isinstance()`` and ``issubclass()`` won't work with protocols
* You can use ``typing.runtime_checkable`` decorator to make it work

The default semantics is that ``isinstance()`` and ``issubclass()`` fail for
protocol types. This is in the spirit of duck typing -- protocols basically
would be used to model duck typing statically, not explicitly at runtime.

However, it should be possible for protocol types to implement custom
instance and class checks when this makes sense, similar to how ``Iterable``
and other ABCs in ``collections.abc`` and ``typing`` already do it, but this
is limited to non-generic and unsubscripted generic protocols (``Iterable``
is statically equivalent to ``Iterable[Any]``).

The typing module will define a special ``@runtime_checkable`` class
decorator that provides the same semantics for class and instance checks
as for ``collections.abc`` classes, essentially making them 'runtime
protocols':

>>> @runtime_checkable
... class Person(Protocol):
...     firstname: str
...     lastname: str
>>>
>>>
>>> class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'
...     job: str = 'astronaut'
>>>
>>>
>>> isinstance(Astronaut, Person)
True

>>> class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> email = Email()
>>> isinstance(email, Message)  # doctest: +SKIP
Traceback (most recent call last):
TypeError: Instance and class checks can only be used with @runtime_checkable protocols

>>> from typing import Protocol, runtime_checkable
>>>
>>>
>>> @runtime_checkable
... class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> email = Email()
>>> isinstance(email, Message)
True

>>> from typing import Protocol, runtime_checkable
>>>
>>>
>>> @runtime_checkable
... class SupportsClose(Protocol):
...     def close(self): ...
>>>
>>>
>>> file = open('/tmp/myfile.txt', mode='w')
>>> isinstance(file, SupportsClose)
True
>>> file.close()


Use Case - 0x01
---------------
>>> from typing import Protocol
>>>
>>>
>>> class SupportsClose(Protocol):
...     def close(self) -> None:
...         ...


Use Case - 0x02
---------------
>>> from abc import abstractmethod
>>> from typing import Protocol
>>>
>>>
>>> class RGB(Protocol):
...     rgb: tuple[int, int, int]
...
...     @abstractmethod
...     def opacity(self) -> int:
...         return 0
>>>
>>>
>>> class Pixel(RGB):
...     def __init__(self, red: int, green: int, blue: float) -> None:
...         self.rgb = red, green, blue
...

Type checker will warn:

* ``blue`` must be ``int``
* ``opacity`` is not defined


Use Case - 0x03
---------------
File ``myapp/view.py``

>>> def get(request):
...     ...
>>>
>>> def post(request):
...     ...
>>>
>>> def put(request):
...     ...
>>>
>>> def delete(request):
...     ...

File ``main.py``

>>> from typing import Protocol
>>>
>>>
>>> class HttpView(Protocol):
...     def get(request): ...
...     def post(request): ...
...     def put(request): ...
...     def delete(request): ...
>>>
>>>
>>> import myapp.view  # doctest: +SKIP
>>> view: HttpView = myapp.view  # doctest: +SKIP


References
----------
.. [#MicrosoftGenericsCovContra] https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance

.. [#PEP544] Levkivskyi, I. and Lehtosalo, J. and Langa, Ł. PEP 544 -- Protocols: Structural subtyping (static duck typing). Year: 2017. Retrieved: 2022-03-09. URL: https://www.python.org/dev/peps/pep-0544/

.. [#Langa2022] Langa, Ł. Covariance/Contravariance/Invariance. Year: 2022. Retrieved: 2022-06-09. URL: https://www.youtube.com/watch?v=1IiL31tUEVk&t=445s

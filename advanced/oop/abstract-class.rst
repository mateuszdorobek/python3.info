OOP Abstract Class
==================
* Since Python 3.0: :pep:`3119` -- Introducing Abstract Base Classes
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation
* Python Abstract Base Classes [#pydocabc]_

.. glossary::

    abstract class
        Class which can only be inherited, not instantiated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


SetUp
-----
>>> from abc import ABC, ABCMeta, abstractmethod, abstractproperty


Syntax
------
* Inherit from ``ABC``
* At least one method must be ``abstractmethod`` or ``abstractproperty``
* Body of the method is not important, it could be ``raise NotImplementedError`` or ``pass``

>>> class Account(ABC):
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError

You cannot create instance of a class ``Account`` as of
this is the abstract class:

>>> mark = Account()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Account with abstract method login


Implement Abstract Methods
--------------------------
Abstract base class:

>>> class Account(ABC):
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError
...
...     @abstractmethod
...     def logout(self):
...         raise NotImplementedError

Implementation:

>>> class User(Account):
...     def login(self):
...         print('Logging-in')
...
...     def logout(self):
...         print('Logging-out')

Use:

>>> mark = User()
>>>
>>> mark.login()
Logging-in
>>>
>>> mark.logout()
Logging-out

Mind, that all abstract methods must be covered, otherwise it will raise
an error.


ABCMeta
-------
There is also an alternative (older) way of defining abstract base classes.
It uses ``metaclass=ABCMeta`` specification during class creation.
This method is not recommended since Python 3.4 when ``ABC`` class was
introduce to simplify the process.

>>> class Account(metaclass=ABCMeta):
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError


Abstract Property
-----------------
* ``abc.abstractproperty`` is deprecated since Python 3.3
* Use ``property`` with ``abc.abstractmethod`` instead

>>> class Account(ABC):
...     @abstractproperty
...     def AGE_MIN(self) -> int:
...         raise NotImplementedError
...
...     @abstractproperty
...     def AGE_MAX(self) -> int:
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     AGE_MIN: int = 18
...     AGE_MAX: int = 65

Since 3.3 instead of ``@abstractproperty`` using both ``@property``
and ``@abstractmethod`` is recommended.

>>> class Account(ABC):
...     @property
...     @abstractmethod
...     def AGE_MIN(self) -> int:
...         raise NotImplementedError
...
...     @property
...     @abstractmethod
...     def AGE_MAX(self) -> int:
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     AGE_MIN: int = 18
...     AGE_MAX: int = 65

Mind that the order here is important and it cannot be the other way around.
Decorator closest to the method must be ``@abstractmethod`` and then
``@property`` at the most outer level. This is because ``@abstractmethod``
sets special attribute on the method and then this method with attribute
is turned to the property. This does not work if you reverse the order.


Problem: Base Class Has No Abstract Method
------------------------------------------
In order to use Abstract Base Class you must create at least one abstract
method. Otherwise it won't prevent from instantiating:

>>> class Account(ABC):
...     pass

The code above will allo to create ``mark`` from ``Account`` because
this class did not have any abstract methods.

>>> mark = Account()
>>> mark  # doctest: +ELLIPSIS
<__main__.Account object at 0x...>


Problem: Base Class Does Not Inherit From ABC
---------------------------------------------
The ``Human`` class does not inherits from ``ABC`` or has ``metaclass=ABCMeta``:

>>> class Account:
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     pass

This code above will allow to create ``mark`` from ``User`` because
``Account`` class does not inherit from ``ABC``.

>>> mark = User()
>>> mark  # doctest: +ELLIPSIS
<__main__.User object at 0x...>


Problem: All Abstract Methods are not Implemented
-------------------------------------------------
Must implement all abstract methods:

>>> class Account(ABC):
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError
...
...     @abstractmethod
...     def logout(self):
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     pass

The code above will prevent from creating ``User`` instance,
because class ``User`` does not overwrite all abstract methods.
In fact it does not overwrite any abstract method at all.

>>> mark = User()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class User with abstract methods login, logout


Problem: Some Abstract Methods are not Implemented
--------------------------------------------------
All abstract methods must be implemented in child class:

>>> class Account(ABC):
...     @abstractmethod
...     def login(self):
...         raise NotImplementedError
...
...     @abstractmethod
...     def logout(self):
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     def login(self):
...         print('Logging-in')

The code above will prevent from creating ``User`` instance,
because class ``User`` does not overwrite all abstract methods.
The ``.login()`` method is not overwritten. In order abstract class
to work, all methods must be covered.

>>> mark = User()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class User with abstract method logout


Problem: Child Class has no Abstract Property
---------------------------------------------
* Using ``abstractproperty``

>>> class Account(ABC):
...     @abstractproperty
...     def AGE_MIN(self) -> int:
...         raise NotImplementedError
...
...     @abstractproperty
...     def AGE_MAX(self) -> int:
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     AGE_MIN: int = 18

>>> mark = User()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class User with abstract method AGE_MAX


Problem: Child Class has no Abstract Properties
-----------------------------------------------
* Using ``property`` and ``abstractmethod``

>>> class Account(ABC):
...     @property
...     @abstractmethod
...     def AGE_MIN(self) -> int:
...         raise NotImplementedError
...
...     @property
...     @abstractmethod
...     def AGE_MAX(self) -> int:
...         raise NotImplementedError
>>>
>>>
>>> class User(Account):
...     AGE_MIN: int = 18

>>> mark = User()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class User with abstract method AGE_MAX


Problem: Invalid Order of Decorators
------------------------------------
* Invalid order of decorators: ``@property`` and ``@abstractmethod``
* Should be: first ``@property`` then ``@abstractmethod``

>>> class Account(ABC):
...     @abstractmethod
...     @property
...     def AGE_MIN(self) -> int:
...         raise NotImplementedError
...
...     @abstractmethod
...     @property
...     def AGE_MAX(self) -> int:
...         raise NotImplementedError
...
Traceback (most recent call last):
AttributeError: attribute '__isabstractmethod__' of 'property' objects is not writable

Note, that this will not even allow to define ``User`` class at all.


Problem: Overwrite ABC File
---------------------------
``abc`` is common name and it is very easy to create file, variable
or module with the same name as the library, hence overwriting it.
In case of error check all entries in ``sys.path`` or ``sys.modules['abc']``
to find what is overwriting it:

>>> from pprint import pprint
>>> import sys
>>>
>>>
>>> sys.modules['abc']  # doctest: +ELLIPSIS
<module 'abc' (frozen)>
>>>
>>> pprint(sys.path)  # doctest: +SKIP
['/Users/watney/myproject',
 '/Applications/PyCharm 2022.3.app/Contents/plugins/python/helpers/pydev',
 '/Applications/PyCharm 2022.3.app/Contents/plugins/python/helpers/pycharm_display',
 '/Applications/PyCharm 2022.3.app/Contents/plugins/python/helpers/third_party/thriftpy',
 '/Applications/PyCharm 2022.3.app/Contents/plugins/python/helpers/pydev',
 '/Applications/PyCharm 2022.3.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
 '/usr/local/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/lib/python311.zip',
 '/usr/local/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/lib/python3.11',
 '/usr/local/Cellar/python@3.11/3.11.1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload',
 '/Users/watney/myproject/venv-3.11/lib/python3.11/site-packages']


Use Case - 0x01
---------------
Abstract Class:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Document(ABC):
...     def __init__(self, filename):
...         self.filename = filename
...
...     @abstractmethod
...     def display(self):
...         pass
>>>
>>>
>>> class PDFDocument(Document):
...     def display(self):
...         print('Display file content as PDF Document')
>>>
>>> class WordDocument(Document):
...     def display(self):
...         print('Display file content as Word Document')

>>> file = PDFDocument('myfile.pdf')
>>> file.display()
Display file content as PDF Document

>>> file = WordDocument('myfile.pdf')
>>> file.display()
Display file content as Word Document

>>> file = Document('myfile.txt')
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Document with abstract method display


Use Case - 0x02
---------------
>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class UIElement(ABC):
...     def __init__(self, name):
...         self.name = name
...
...     @abstractmethod
...     def render(self):
...         pass
>>>
>>>
>>> class TextInput(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} TextInput')
>>>
>>>
>>> class Button(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} Button')
>>>
>>>
>>> def render(component: list[UIElement]):
...     for element in component:
...         element.render()
>>>
>>>
>>> login_window = [
...     TextInput(name='Username'),
...     TextInput(name='Password'),
...     Button(name='Submit'),
... ]
>>>
>>> render(login_window)
Rendering Username TextInput
Rendering Password TextInput
Rendering Submit Button


Use Case - 0x03
---------------
>>> class Person(ABC):
...     age: int
...
...     @property
...     @abstractmethod
...     def AGE_MAX(self) -> int: ...
...
...     @abstractproperty
...     def AGE_MIN(self) -> int: ...
...
...     def __init__(self, age):
...         if not self.AGE_MIN <= age < self.AGE_MAX:
...             raise ValueError('Age is out of bounds')
...         self.age = age
>>>
>>>
>>> class Astronaut(Person):
...     AGE_MIN = 30
...     AGE_MAX = 50
>>>
>>>
>>> mark = Astronaut(age=40)


Further Reading
---------------
* https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes
* https://www.youtube.com/watch?v=S_ipdVNSFlo


References
----------
.. [#pydocabc] https://docs.python.org/3/library/collections.abc.html


Assignments
-----------
.. literalinclude:: assignments/oop_abstract_class_a.py
    :caption: :download:`Solution <assignments/oop_abstract_class_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_class_b.py
    :caption: :download:`Solution <assignments/oop_abstract_class_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_class_c.py
    :caption: :download:`Solution <assignments/oop_abstract_class_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_class_d.py
    :caption: :download:`Solution <assignments/oop_abstract_class_d.py>`
    :end-before: # Solution

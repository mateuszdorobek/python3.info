OOP Method About
================
* Methods are functions in the class
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)

    self
        Instance on which method was called.


Define
------
* At definition - ``self`` should always be a first parameter

>>> class User:
...     def login(self):
...         print(f'Logged in')
...
>>>
>>> mark = User()
>>> mark.login()
Logged in


Self
----
* At definition - ``self`` should always be a first parameter
* When called Python will pass an instance as ``self``
* You don't do that manually
* Later you will learn more advanced things like static methods etc.

>>> class User:
...     def login(self):
...         print(f'Logged in')

>>> mark = User()
>>> mark.login()
Logged in

>>> User.login()
Traceback (most recent call last):
TypeError: User.login() missing 1 required positional argument: 'self'

>>> User.login(mark)
Logged in


Return
------
>>> class User:
...     def login(self):
...         return 'Logged in'
...
>>>
>>> mark = User()
>>> result = mark.login()
>>>
>>> print(result)
Logged in


Exceptions
----------
>>> class User:
...     def login(self):
...         raise PermissionError
...
>>>
>>> mark = User()
>>> mark.login()
Traceback (most recent call last):
PermissionError


Use Case - 0x01
---------------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def say_hello(self):
...         return f'Hello {self.firstname} {self.lastname}'
...
...     def say_goodbye(self):
...         return f'Goodbye {self.firstname} {self.lastname}'

>>> mark = User('Mark', 'Watney')
>>> melissa = User('Melissa', 'Lewis')
>>>
>>>
>>> mark.say_hello()
'Hello Mark Watney'
>>>
>>> melissa.say_hello()
'Hello Melissa Lewis'
>>>
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis'}


Use Case - 0x02
---------------
>>> class User:
...     firstname: str
...     lastname: str
...     is_authenticated: bool
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.is_authenticated = False
...
...     def login(self, username, password):
...         if username == 'mwatney' and password == 'nasa':
...             self.is_authenticated = True
...         else:
...             raise PermissionError('Invalid username and/or password')
...
...     def logout(self):
...         self.is_authenticated = False
...

>>> mark = User('Mark', 'Watney')
>>> melissa = User('Melissa', 'Lewis')
>>>
>>>
>>> mark.is_authenticated
False
>>>
>>> melissa.is_authenticated
False
>>>
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_authenticated': False}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'is_authenticated': False}


>>> mark.login(username='mwatney', password='nasa')
>>>
>>>
>>> mark.is_authenticated
True
>>>
>>> melissa.is_authenticated
False
>>>
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_authenticated': True}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'is_authenticated': False}


>>> melissa.login('mlewis', 'nasa')
Traceback (most recent call last):
PermissionError: Invalid username and/or password
>>>
>>>
>>> mark.is_authenticated
True
>>> melissa.is_authenticated
False
>>>
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_authenticated': True}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'is_authenticated': False}

>>> mark.logout()
>>>
>>>
>>> mark.is_authenticated
False
>>> melissa.is_authenticated
False
>>>
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'is_authenticated': False}
>>>
>>> vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis', 'is_authenticated': False}





Use Case - 0x01
---------------
>>> def add(a, b):
...     return a + b
>>>
>>> def sub(a, b):
...     return a - b
>>>
>>> def mul(a, b):
...     return a * b
>>>
>>> def div(a, b):
...     return a / b
>>>
>>> def say_hello():
...     return 'hello'
>>>
>>> def say_goodbye():
...     return 'goodbye'
>>>
>>> def login(username, password):
...     return 'logged-in'
>>>
>>> def logout():
...     return 'logged-out'

>>> class Calculator:
...     def add(self, a, b):
...         return a + b
...
...     def sub(self, a, b):
...         return a - b
...
...     def mul(self, a, b):
...         return a * b
...
...     def div(self, a, b):
...         return a / b
>>>
>>>
>>> class User:
...     def say_hello(self):
...         return 'hello'
...
...     def say_goodbye():
...         return 'goodbye'
...
...     def login(self, username, password):
...         return 'logged-in'
...
...     def logout(self):
...         return 'logged-out'


Use Case - 0x02
---------------
* Staticmethod

>>> class Calculator:
...     def add(self, a, b):
...         return a + b
...
...     def sub(self, a, b):
...         return a - b
...
...     def mul(self, a, b):
...         return a * b
...
...     def div(self, a, b):
...         return a / b
>>>
>>> Calculator.add(a=1, b=2)
Traceback (most recent call last):
TypeError: Calculator.add() missing 1 required positional argument: 'self'
>>>
>>> calc = Calculator()
>>> calc.add(a=1, b=2)
3

>>> class Calculator:
...     def add(a, b):
...         return a + b
...
...     def sub(a, b):
...         return a - b
...
...     def mul(a, b):
...         return a * b
...
...     def div(a, b):
...         return a / b
>>>
>>> Calculator.add(a=1, b=2)
3
>>>
>>> calc = Calculator()
>>> calc.add(a=1, b=2)
Traceback (most recent call last):
TypeError: Calculator.add() got multiple values for argument 'a'

>>> class Calculator:
...     @staticmethod
...     def add(a, b):
...         return a + b
...
...     @staticmethod
...     def sub(a, b):
...         return a - b
...
...     @staticmethod
...     def mul(a, b):
...         return a * b
...
...     @staticmethod
...     def div(a, b):
...         return a / b
>>>
>>> Calculator.add(1,2)
3
>>>
>>> calc = Calculator()
>>> calc.add(a=1, b=2)
3


Use Case - 0x03
---------------
>>> class User:
...     def create(self, username, password):
...         self.username = username
...         self.password = password
...         return self
...
...     def login(self):
...         return 'logged-in'
...
...     def logout(self):
...         return 'logged-out'

>>> mark = User.create(username='mwatney', password='nasa')
Traceback (most recent call last):
TypeError: User.create() missing 1 required positional argument: 'self'

>>> mark = User().create(username='mwatney', password='nasa')
>>>
>>> mark.login()
'logged-in'
>>>
>>> mark.logout()
'logged-out'


Use Case - 0x04
---------------
>>> class User:
...     @staticmethod
...     def create(username, password):
...         user = object.__new__(User)
...         user.username = username
...         user.password = password
...         return user
...
...     def login(self):
...         return 'logged-in'
...
...     def logout(self):
...         return 'logged-out'

>>> mark = User.create(username='mwatney', password='nasa')
>>>
>>> mark.login()
'logged-in'
>>>
>>> mark.logout()
'logged-out'


Use Case - 0x05
---------------
>>> class User:
...     @classmethod
...     def create(cls, username, password):
...         user = object.__new__(cls)
...         user.username = username
...         user.password = password
...         return user
...
...     def login(self):
...         return 'logged-in'
...
...     def logout(self):
...         return 'logged-out'

>>> mark = User.create(username='mwatney', password='nasa')
>>>
>>> mark.login()
'logged-in'
>>>
>>> mark.logout()
'logged-out'


Use Case - 0x06
---------------
>>> class TextInput:
...     def __init__(self, name):
...         self.name = name
...
...     def display(self):
...         print(f'Displaying {self.name} text field')
...
>>>
>>> class Button:
...     def __init__(self, name):
...         self.name = name
...
...     def display(self):
...         print(f'Displaing {self.name} button')
...
>>>
>>> login_window = [
...     TextInput('username'),
...     TextInput('password'),
...     Button('submit'),
... ]
>>>
>>> for obj in login_window:
...     obj.display()
...
Displaying username text field
Displaying password text field
Displaing submit button


Use Case - 0x07
---------------
>>> class Car:
...     name: str
...     engine: str
...
...     def __init__(self, name):
...         self.name = name
...         self.engine = 'off'
...
...     def start_engine(self):
...         self.engine = 'on'
...
...     def stop_engine(self):
...         self.engine = 'off'
...
...     def drive(self, destination):
...         if self.engine == 'off':
...             raise RuntimeError('Cannot drive while engine is off')
...         else:
...             print(f'Driving to: {destination}')
...
>>>
>>> maluch = Car('Fiat 126p')
>>>
>>> vars(maluch)
{'name': 'Fiat 126p', 'engine': 'off'}
>>>
>>> maluch.drive('Kraków')
Traceback (most recent call last):
RuntimeError: Cannot drive while engine is off
>>>
>>> maluch.start_engine()
>>>
>>> vars(maluch)
{'name': 'Fiat 126p', 'engine': 'on'}
>>>
>>> maluch.drive('Kraków')
Driving to: Kraków
>>>
>>> maluch.stop_engine()
>>>
>>> vars(maluch)
{'name': 'Fiat 126p', 'engine': 'off'}
>>>
>>> maluch.drive('Kraków')
Traceback (most recent call last):
RuntimeError: Cannot drive while engine is off

>>> tesla = Car('Model S')
>>>
>>> tesla.start_engine()
>>>
>>> tesla.drive('Warszawa')
Driving to: Warszawa
>>>
>>>
>>> maluch.drive('Warszawa')
Traceback (most recent call last):
RuntimeError: Cannot drive while engine is off


Use Case - 0x08
---------------
>>> class List:
...     def __init__(self, values):
...         self.values = values
...
...     def sort(self):
...         self.values.sort()
...
...     def setitem(self, index, newvalue):
...         self.values[index] = newvalue
...
...     def getitem(self, index):
...         return self.values[index]
...
>>>
>>>
>>> data = List(['a', 'b', 'c'])

>>> data.getitem(0)
'a'
>>> data.getitem(1)
'b'
>>> data.getitem(2)
'c'

>>> data.setitem(1, 'x')
>>>
>>> data.getitem(0)
'a'
>>> data.getitem(1)
'x'
>>> data.getitem(2)
'c'

>>> data.sort()
>>>
>>> data.getitem(0)
'a'
>>> data.getitem(1)
'c'
>>> data.getitem(2)
'x'

>>> vars(data)
{'values': ['a', 'c', 'x']}


>>> data2 = List(['A', 'B', 'C'])
>>>
>>> vars(data)
{'values': ['a', 'c', 'x']}
>>>
>>> vars(data2)
{'values': ['A', 'B', 'C']}

>>> data1 = ['a', 'b', 'c']
>>> data2 = ['A', 'B', 'C']
>>>
>>> data1.__getitem__(0)
'a'
>>> data1.__getitem__(1)
'b'
>>> data1.__getitem__(2)
'c'
>>>
>>> data1.__setitem__(1, 'x')
>>>
>>> data1.__getitem__(0)
'a'
>>> data1.__getitem__(1)
'x'
>>> data1.__getitem__(2)
'c'
>>>
>>> data1
['a', 'x', 'c']
>>>
>>> data2
['A', 'B', 'C']
>>>
>>>
>>> data1.sort()
>>>
>>> data1.__getitem__(0)
'a'
>>> data1.__getitem__(1)
'c'
>>> data1.__getitem__(2)
'x'

>>> data1 = ['a', 'b', 'c']
>>> data2 = ['A', 'B', 'C']
>>>
>>> data1[0]
'a'
>>> data1[1]
'b'
>>> data1[2]
'c'
>>>
>>> data1[1] = 'x'
>>>
>>> data1[0]
'a'
>>> data1[1]
'x'
>>> data1[2]
'c'
>>>
>>> data1
['a', 'x', 'c']
>>>
>>> data2
['A', 'B', 'C']
>>>
>>>
>>> data1.sort()
>>>
>>> data1[0]
'a'
>>> data1[1]
'c'
>>> data1[2]
'x'


Use Case - 0x09
---------------
>>> class List:
...     def __init__(self, values):
...         self.values = values
...
...     def sort(self):
...         self.values.sort()
...
...     def __setitem__(self, index, newvalue):
...         self.values[index] = newvalue
...
...     def __getitem__(self, index):
...         return self.values[index]
...
>>>
>>> data = List(['a', 'b', 'c'])

>>> data[0]
'a'
>>> data[1]
'b'
>>> data[2]
'c'

>>> data[1] = 'x'
>>>
>>> data[0]
'a'
>>> data[1]
'x'
>>> data[2]
'c'


Use Case - 0x0A
---------------
>>> class Car:
...     name: str
...     engine: str
...     windows: str
...     speed: int
...
...     def accelerate(self, value):
...         self.speed += value
...
...     def slowdown(self, value):
...         self.speed -= value


.. todo:: Assignments


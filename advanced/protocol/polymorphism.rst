Protocol Polymorphism
=====================


SetUp
-----
>>> from abc import ABC, abstractmethod
>>> from dataclasses import dataclass


Elif
----
It all starts with single ``if`` statement

>>> language = 'English'
>>>
>>> if language == 'English':
...     result = 'Hello'
>>>
>>> print(result)
Hello

>>> language = 'English'
>>>
>>> if language == 'English':
...     result = 'Hello'
... elif language == 'Polish':
...     result = 'Witaj'
>>>
>>> print(result)
Hello

It quickly grows into multiple ``elif``:

>>> language = 'English'
>>>
>>> if language == 'English':
...     result = 'Hello'
... elif language == 'Polish':
...     result = 'Witaj'
... elif language == 'Spanish':
...     result = 'Hola'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Hello


Match: Switch Pattern
---------------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* More information :ref:`Match About` [#pybookSyntaxMatch]_

In other languages you may find ``switch`` statement. Since Python 3.10
there is a ``match`` statement which can do the similar thing:

>>> language = 'English'
>>>
>>> match language:
...     case 'English':  result = 'Hello'
...     case 'Polish':   result = 'Witaj'
...     case 'Spanish':  result = 'Hola'
...     case _:          result = 'Unknown language'

Problem is that, ``match`` moves business logic to the execution place.
You can write it in a function using ``dict`` and ``.get()`` method with
default value. It's a bit cleaner, but essentially the same...

>>> def switch(key):
...     return {
...         'English': 'Hello',
...         'Polish': 'Witaj',
...         'Spanish': 'Hola',
...     }.get(key, 'Unknown language')
>>>
>>> switch('English')
'Hello'
>>> switch('Spanish')
'Hola'


Procedural Polymorphism
-----------------------
* UNIX ``getchar()`` function used function lookup table with pointers

>>> keyboard = {
...     'open': lambda: ...,
...     'close':  lambda: ...,
...     'read':  lambda bytes: ...,
...     'write':  lambda content: ...,
...     'seek':  lambda position: ...,
... }
>>>
>>> file = {
...     'open': lambda: ...,
...     'close':  lambda: ...,
...     'read':  lambda bytes: ...,
...     'write':  lambda content: ...,
...     'seek':  lambda position: ...,
... }
>>>
>>> socket = {
...     'open': lambda: ...,
...     'close':  lambda: ...,
...     'read':  lambda bytes: ...,
...     'write':  lambda content: ...,
...     'seek':  lambda position: ...,
... }
>>>
>>>
>>> def getchar(obj):
...     obj['open']()
...     obj['seek'](0)
...     obj['read'](1)
...     obj['close']()
>>>
>>>
>>> getchar(file)
>>> getchar(keyboard)
>>> getchar(socket)


Explicit Polymorphism
---------------------
.. todo:: Example compatible with code above (elif, switch, pattern matching)

>>> @dataclass
... class Element(ABC):
...     name: str
...
...     @abstractmethod
...     def render(self):
...         pass
>>>
>>>
>>> @dataclass
... class TextInput(Element):
...     def render(self):
...         print(f'Rendering {self.name} TextInput')
>>>
>>>
>>> @dataclass
... class Button(Element):
...     def render(self):
...         print(f'Rendering {self.name} Button')

>>> login_window = [
...     TextInput(name='Username'),
...     TextInput(name='Password'),
...     Button(name='Submit'),
... ]

>>> def render(component: list[Element]):
...     for element in component:
...         element.render()
>>>
>>> render(login_window)
Rendering Username TextInput
Rendering Password TextInput
Rendering Submit Button


Structural Polymorphism
-----------------------
* Duck typing

>>> @dataclass
... class TextInput:
...     name: str
...
...     def render(self):
...         print(f'Rendering {self.name} TextInput')
>>>
>>>
>>> @dataclass
... class Button:
...     name: str
...
...     def render(self):
...         print(f'Rendering {self.name} Button')

>>> login_window = [
...     TextInput(name='Username'),
...     TextInput(name='Password'),
...     Button(name='Submit'),
... ]

>>> def render(component):
...     for element in component:
...         element.render()
>>>
>>> render(login_window)
Rendering Username TextInput
Rendering Password TextInput
Rendering Submit Button


Use Case - 0x01
---------------
>>> from abc import ABC, abstractmethod
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Account(ABC):
...     username: str
...
...     @abstractmethod
...     def login(self):
...         pass
>>>
>>>
>>> class User(Account):
...     def login(self):
...         return f'User {self.username} logged-in'
>>>
>>> class Admin(Account):
...     def login(self):
...         return f'Admin {self.username} logged-in'
>>>
>>>
>>> def login(accounts: list[Account]) -> None:
...     for account in accounts:
...         print(account.login())
>>>
>>>
>>> group = [
...     User('mwatney'),
...     Admin('mlewis'),
...     User('rmartinez'),
...     User('avogel'),
... ]
>>>
>>> login(group)
User mwatney logged-in
Admin mlewis logged-in
User rmartinez logged-in
User avogel logged-in

In Python, due to the duck typing and dynamic nature of the language, the
Interface or abstract class is not needed to do polymorphism:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     username: str
...
...     def login(self):
...         return f'User {self.username} logged-in'
>>>
>>> @dataclass
... class Admin:
...     username: str
...
...     def login(self):
...         return f'Admin {self.username} logged-in'
>>>
>>>
>>> group = [
...     User('mwatney'),
...     Admin('mlewis'),
...     User('rmartinez'),
...     User('avogel'),
... ]
>>>
>>> for account in group:
...     print(account.login())
User mwatney logged-in
Admin mlewis logged-in
User rmartinez logged-in
User avogel logged-in


Use Case - 0x02
---------------
* Login Window

>>> import re
>>>
>>>
>>> class Element:
...     def __init__(self, name):
...         self.name = name
...
...     def on_mouse_hover(self):
...         raise NotImplementedError
...
...     def on_mouse_out(self):
...         raise NotImplementedError
...
...     def on_mouse_click(self):
...         raise NotImplementedError
...
...     def on_key_press(self):
...         raise NotImplementedError
...
...     def render(self):
...         raise NotImplementedError
>>>
>>>
>>> class Button(Element):
...     action: str
...
...     def __init__(self, *args, action: str | None = None, **kwargs):
...         self.action = action
...         super().__init__(*args, **kwargs)
...
...     def on_key_press(self):
...         pass
...
...     def on_mouse_hover(self):
...         pass
...
...     def on_mouse_out(self):
...         pass
...
...     def on_mouse_click(self):
...         pass
...
...     def render(self):
...         action = self.action
...         print(f'Rendering Button with {action}')
>>>
>>>
>>> class Input(Element):
...     regex: re.Pattern
...
...     def __init__(self, *args, regex: str | None = None, **kwargs):
...         self.regex = re.compile(regex)
...         super().__init__(*args, **kwargs)
...
...     def on_key_press(self):
...         pass
...
...     def on_mouse_hover(self):
...         pass
...
...     def on_mouse_out(self):
...         pass
...
...     def on_mouse_click(self):
...         pass
...
...     def render(self):
...         regex = self.regex
...         print(f'Rendering Input with {regex}')
>>>
>>>
>>> def render(components: list[Element]):
...     for obj in components:
...         obj.render()
>>>
>>>
>>> login_window = [
...     Input('Username', regex='[a-zA-Z0-9]'),
...     Input('Password', regex='[a-zA-Z0-9!@#$%^&*()]'),
...     Button('Submit', action='/login.html'),
... ]
>>>
>>> render(login_window)
Rendering Input with re.compile('[a-zA-Z0-9]')
Rendering Input with re.compile('[a-zA-Z0-9!@#$%^&*()]')
Rendering Button with /login.html


References
----------
.. [#pybookSyntaxMatch] https://python3.info/intermediate/match/about.html

.. todo:: Assignments

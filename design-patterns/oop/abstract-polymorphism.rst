OOP Abstract Polymorphism
=========================


SetUp
-----
>>> from abc import ABCMeta, abstractmethod


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


Polymorphism
------------
.. todo:: Example compatible with code above (elif, switch, pattern matching)

>>> class UIElement(metaclass=ABCMeta):
...     def __init__(self, name):
...         self.name = name
...
...     @abstractmethod
...     def render(self):
...         pass
>>>
>>>
>>> def render(component: list[UIElement]):
...     for element in component:
...         element.render()

>>> class TextInput(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} TextInput')
>>>
>>>
>>> class Button(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} Button')

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


Use Case - 0x01
---------------
>>> from abc import ABCMeta, abstractmethod
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Person(metaclass=ABCMeta):
...     name: str
...
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         return f'Hello {self.name}'
>>>
>>> class Cosmonaut(Person):
...     def say_hello(self):
...         return f'Witaj {self.name}'
>>>
>>>
>>> def hello(crew: list[Person]) -> None:
...     for member in crew:
...         print(member.say_hello())
>>>
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Cosmonaut('José Jiménez'),
...         Astronaut('Melissa Lewis'),
...         Cosmonaut('Pan Twardowski'),
... ]
>>>
>>> hello(crew)
Hello Mark Watney
Witaj José Jiménez
Hello Melissa Lewis
Witaj Pan Twardowski

In Python, due to the duck typing and dynamic nature of the language, the
Interface or abstract class is not needed to do polymorphism:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     name: str
...
...     def say_hello(self):
...         return f'Hello {self.name}'
>>>
>>> @dataclass
... class Cosmonaut:
...     name: str
...
...     def say_hello(self):
...         return f'Witaj {self.name}'
>>>
>>>
>>> crew = [Astronaut('Mark Watney'),
...         Cosmonaut('José Jiménez'),
...         Astronaut('Melissa Lewis'),
...         Cosmonaut('Pan Twardowski'),
... ]
>>>
>>> for member in crew:
...     print(member.say_hello())
Hello Mark Watney
Witaj José Jiménez
Hello Melissa Lewis
Witaj Pan Twardowski


Use Case - 0x02
---------------
* Login Window

>>> import re
>>>
>>>
>>> class UIElement:
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
>>> class Button(UIElement):
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
>>> class Input(UIElement):
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
>>> def render(components: list[UIElement]):
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

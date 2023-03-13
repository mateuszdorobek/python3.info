Idiom Match
===========


Problem
-------
>>> language = 'English'
>>>
>>> if language == 'Polish':
...     result = 'Cześć'
... elif language == 'English':
...     result = 'Hello'
... elif language == 'German':
...     result = 'Guten Tag'
... elif language == 'Spanish':
...     result = 'Buenos Días'
... elif language == 'Chinese':
...     result = '你好'
... elif language == 'French':
...     result = 'Bonjour'
... else:
...     result = 'Unknown language'
>>>
>>> print(result)
Hello


Switch
------
In other languages you may find ``switch`` statement:
(note that this is not a valid Python code)

>>> language = 'English'
>>>
>>> switch(language):  # doctest: +SKIP
...     case 'Polish': result = 'Cześć'
...     case 'English': result = 'Hello'
...     case 'German': result = 'Guten Tag'
...     case 'Spanish': result = 'Buenos Días'
...     case 'Chinese': result = '你好'
...     case 'French': result = 'Bonjour'
...     default: result = 'Unknown language'
>>>
>>> print(result)  # doctest: +SKIP
Hello


Pattern Matching
----------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial

>>> language = 'English'
>>>
>>> match language:  # doctest: +SKIP
...     case 'Polish': result = 'Cześć'
...     case 'English': result = 'Hello'
...     case 'German': result = 'Guten Tag'
...     case 'Spanish': result = 'Buenos Días'
...     case 'Chinese': result = '你好'
...     case 'French': result = 'Bonjour'
...     case _: result = 'Unknown language'
>>>
>>> print(result)
Hello


Behavior
--------
.. csv-table:: Pattern Matching [#patternmatching]_
    :header: Statement, Meaning

    ``x``,          "assign x = subject"
    ``'x'``,        "test subject == 'x'"
    ``x.y``,        "test subject == x.y"
    ``x()``,        "test isinstance(subject, x)"
    ``{'x': 'y'}``, "test isinstance(subject, Mapping) and subject.get('x') == 'y'"
    ``['x']``,      "test isinstance(subject, Sequence) and len(subject) == 1 and subject[0] == 'x'"


Matching Alternatives
---------------------
>>> status = 418
>>>
>>>
>>> match status:  # doctest: +SKIP
...     case 400:
...         result = 'Bad request'
...     case 401 | 403 | 405:
...         result = 'Not allowed'
...     case 404:
...         result = 'Not found'
...     case 418:
...         result = "I'm a teapot"
...     case _:
...         result = 'Unexpected status'


Matching on Sequence
--------------------
>>> request = 'GET /index.html HTTP/2.0'
>>>
>>>
>>> match request.split():  # doctest: +SKIP
...     case ['GET', uri, version]:
...         server.get(uri)
...     case ['POST', uri, version]:
...         server.post(uri)
...     case ['PUT', uri, version]:
...         server.put(uri)
...     case ['DELETE', uri, version]:
...         server.delete(uri)


Matching on Sequence with Assignment
------------------------------------
>>> class Hero:
...     def action(self):
...         return  ['move', 'left', 20]
>>>
>>>
>>> match hero.action():  # doctest: +SKIP
...     case ['move', ('up'|'down'|'left'|'right') as direction, value]:
...         hero.move(direction, value)
...     case ['make_damage', value]:
...         hero.make_damage(value)
...     case ['take_damage', value]:
...         hero.take_damage(value)


Matching on Enum
----------------
>>> from enum import Enum
>>>
>>>
>>> class Key(Enum):
...     ESC = 27
...     ARROW_LEFT = 37
...     ARROW_UP = 38
...     ARROW_RIGHT = 39
...     ARROW_DOWN = 40
>>>
>>>
>>> match keyboard.on_key_press():  # doctest: +SKIP
...     case Key.ESC:
...         game.quit()
...     case Key.ARROW_LEFT:
...         hero.move_left()
...     case Key.ARROW_UP:
...         hero.move_up()
...     case Key.ARROW_RIGHT:
...         hero.move_right()
...     case Key.ARROW_DOWN:
...         hero.move_down()
...     case _:
...         raise ValueError(f'Unrecognized key')


References
----------
.. [#patternmatching] Raymond Hettinger. Retrieved: 2021-03-07. URL: https://twitter.com/raymondh/status/1361780586570948609?s=20


Assignments
-----------
.. literalinclude:: assignments/idioms_match_a.py
    :caption: :download:`Solution <assignments/idioms_match_a.py>`
    :end-before: # Solution

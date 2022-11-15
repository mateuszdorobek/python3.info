Match Pattern Constant
======================

A `constant value pattern` works like the literal but for certain named
constants. Note that it must be a qualified (dotted) name, given the
possible ambiguity with a capture pattern. It looks like ``Color.RED``
and only matches values equal to the corresponding value. It never
binds.



Use Case - 0x06
---------------
* Enum

Test Setup:

>>> class Keyboard:
...     def on_key_press(self): ...
>>>
>>> keyboard = Keyboard()

>>> class Game:
...     def quit(self): ...
...     def move_left(self): ...
...     def move_up(self): ...
...     def move_right(self): ...
...     def move_down(self): ...
>>>
>>> game = Game()

Use Case:

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
>>> match keyboard.on_key_press():
...     case Key.ESC:          game.quit()
...     case Key.ARROW_LEFT:   game.move_left()
...     case Key.ARROW_UP:     game.move_up()
...     case Key.ARROW_RIGHT:  game.move_right()
...     case Key.ARROW_DOWN:   game.move_down()
...     case _: raise ValueError(f'Unrecognized key')
Traceback (most recent call last):
ValueError: Unrecognized key

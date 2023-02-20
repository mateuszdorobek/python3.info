Match Subpatterns
=================


Use Case - 0x01
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def move_horizontal(self, direction, value): ...
...     def move_vertical(self, direction, value): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['move', 'left', 10]
>>>
>>> match action:
...
...     case ['move', ('up'|'down') as direction, value]:
...         hero.move_vertical(direction, value)
...
...     case ['move', ('left'|'right') as direction, value]:
...         hero.move_horizontal(direction, value)
...
...     case _:
...         raise ValueError('Invalid direction')

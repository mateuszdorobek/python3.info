Match Guard
===========


Use Case - 0x01
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def make_normal_damage(self, dmg): ...
...     def make_critical_damage(self, dmg): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['make_damage', 5]
>>>
>>> match action:
...     case ['make_damage', value] if value < 0:
...         raise ValueError('Damage cannot be negative')
...
...     case ['make_damage', value] if 0 <= value < 10:
...         hero.make_normal_damage(value)
...
...     case ['make_damage', value] if value >= 10:
...         hero.make_critical_damage(value)


Use Case - 0x02
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def walk(self, direction, value): ...
...     def run(self, direction): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['move', 'left', 10]
>>>
>>> match action:
...
...     case ['move', direction, speed] if speed < 10:
...         hero.walk(direction)
...
...     case ['move', direction, speed] if speed >= 10:
...         hero.run(direction)


Use Case - 0x03
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def move(self, direction, value): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['move', 'left', 10]
>>>
>>> match action:
...
...     case ['move', direction, value] if direction not in ['up','down','left','right']:
...         raise ValueError('Invalid direction')
...
...     case ['move', direction, value] if direction in ['up','down','left','right']:
...         hero.move(direction, value)

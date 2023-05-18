Match Guard
===========
* Additional if statements
* This is not to replace if-else expression
* This add additional validation to match-case
* https://peps.python.org/pep-0622/#guards

>>> data = [1, 2]
>>>
>>> match data:
...     case [x, y] if x > 1024 and y > 1024:
...         print('Got a pair of large numbers')
...     case [x, y] if x > 1024:
...         print('X is a large number')
...     case [x, y] if y > 1024:
...         print('Y is a large number')
...     case [x, y] if x == y:
...         print('Got equal items')
...     case _:
...         print('Not an outstanding input')
Not an outstanding input


Use Case - 0x01
---------------
>>> def status(health):
...     match health:
...         case hp if hp <= 0:   return 'dead'
...         case hp if hp < 50:   return 'low'
...         case hp if hp >= 50:  return 'high'

>>> status(100)
'high'
>>>
>>> status(25)
'low'
>>>
>>> status(10)
'low'
>>>
>>> status(0)
'dead'
>>>
>>> status(-5)
'dead'


Use Case - 0x02
---------------
>>> ADMINS = ['mlewis', 'bjohanssen']
>>> STAFF = ['mwatney', 'mlewis', 'rmartinez', 'bjohanssen', 'cbeck']
>>>
>>> def login(username, password):
...     match username:
...         case _ if username in ADMINS:
...             print('Admin logged-in')
...         case _ if username in STAFF:
...             print('Staff logged-in')
...         case _ if username not in STAFF:
...             raise PermissionError('Access denied')

>>> login('mlewis', 'NASA')
Admin logged-in

>>> login('mwatney', 'Ares3')
Staff logged-in

>>> login('avogel', 'ESA')
Traceback (most recent call last):
PermissionError: Access denied


Use Case - 0x03
---------------
* status "Full Health" - when health 100%
* status "Injured" - when health 75% - 100% (exclusive)
* status "Badly Wounded" - when health 25% - 75% (exclusive)
* status "Near Death" - when health 1% - 25% (exclusive)
* status "Dead" - when health 0% or less

>>> hero = ['health', 10]
>>>
>>>
>>> match hero:
...     case ['health', percent] if percent == 100:
...         status = 'Full health'
...
...     case ['health', percent] if percent in range(75, 100):
...         status = 'Injured'
...
...     case ['health', percent] if percent in range(25, 75):
...         status = 'Badly Wounded'
...
...     case ['health', percent] if percent in range(1, 25):
...         status = 'Near Death'
...
...     case ['health', percent] if percent <= 0:
...         status = 'Dead'
...
>>> print(status)
Near Death


Use Case - 0x04
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
>>>
>>> match action:
...
...     case ['make_damage', value] if value >= 10:
...         hero.make_critical_damage(value)
...
...     case ['make_damage', value] if 0 <= value < 10:
...         hero.make_normal_damage(value)
...
...     case ['make_damage', value] if value < 0:
...         raise ValueError('Damage cannot be negative')


Use Case - 0x05
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
>>>
>>> match action:
...
...     case ['move', direction, speed] if speed < 10:
...         hero.walk(direction)
...
...     case ['move', direction, speed] if speed >= 10:
...         hero.run(direction)


Use Case - 0x06
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
>>>
>>> match action:
...
...     case ['move', direction, value] if direction not in ['up','down','left','right']:
...         raise ValueError('Invalid direction')
...
...     case ['move', direction, value] if direction in ['up','down','left','right']:
...         hero.move(direction, value)

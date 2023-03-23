Mapping Getitem
===============
* Key lookup is very efficient ``O(1)``
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
* ``.get()`` returns ``None`` if key not found
* ``.get()`` can have default value, if key not found

>>> hello = {
...    'English': 'Hello',
...    'German': 'Guten Tag',
...    'Polish': 'Witaj',
... }
>>>
>>>
>>> hello.get('English')
'Hello'
>>>
>>> hello.get('Polish')
'Witaj'



Getitem Method
--------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew['commander']
'Melissa Lewis'
>>>
>>> crew['chemist']
Traceback (most recent call last):
KeyError: 'chemist'


Get Method
----------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew.get('commander')
'Melissa Lewis'
>>>
>>> crew.get('chemist')
>>>
>>> crew.get('chemist', 'not assigned')
'not assigned'


Key Type
--------
Getting keys other than ``str``:

>>> calendarium = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon'}
>>>
>>>
>>> calendarium[1961]
'First Human Space Flight'
>>>
>>> calendarium['1961']
Traceback (most recent call last):
KeyError: '1961'



GetItem
-------
* GetItem with index on ``dict`` is not possible

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[0]
Traceback (most recent call last):
KeyError: 0
>>>
>>> crew[1]
Traceback (most recent call last):
KeyError: 1

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[-0]
Traceback (most recent call last):
KeyError: 0
>>>
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1


Slice
-----
* Slicing on ``dict`` is not possible

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[1:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>>
>>> crew[:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>>
>>> crew[::2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'


GetItem on Numeric Dict Keys
----------------------------
>>> crew = {
...    0: 'Melissa Lewis',
...    1: 'Mark Watney',
...    2: 'Rick Martinez'}
>>>
>>>
>>> crew[0]
'Melissa Lewis'
>>>
>>> crew[1]
'Mark Watney'
>>>
>>> crew[2]
'Rick Martinez'
>>>
>>> crew[-0]
'Melissa Lewis'
>>>
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1
>>>
>>> crew[-2]
Traceback (most recent call last):
KeyError: -2


Dict Switch
-----------
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['French'])

>>> hello = {
...     'English': 'Hello',
...     'German': 'Guten Tag',
...     'Polish': 'Witaj',
...     'default': "I don't speak this language",
... }
>>>
>>>
>>> language = input('What is your language?: ')  #input: 'French'
>>> result = hello.get(language, hello['default'])
>>>
>>> print(result)
I don't speak this language



Use Case - 0x01
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
... }
>>>
>>> MONTHS[1]
'January'
>>>
>>> MONTHS['1']
Traceback (most recent call last):
KeyError: '1'
>>>
>>> MONTHS['01']
Traceback (most recent call last):
KeyError: '01'


Use Case - 0x02
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
... }
>>>
>>> MONTHS.get(1)
'January'
>>>
>>> MONTHS.get(13)
>>>
>>> MONTHS.get(13, 'invalid month')
'invalid month'


Use Case - 0x03
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
...     4: 'April',
...     5: 'May',
...     6: 'June',
...     7: 'July',
...     8: 'August',
...     9: 'September',
...     10: 'October',
...     11: 'November',
...     12: 'December'
... }
>>>
>>> DATE = '1961-04-12'
>>>
>>> year, month, day = DATE.split('-')
>>>
>>> year
'1961'
>>> month
'04'
>>> day
'12'
>>>
>>> MONTHS[month]
Traceback (most recent call last):
KeyError: '04'
>>>
>>> MONTHS[int(month)]
'April'


Use Case - 0x04
---------------
>>> PAYROLL = [
...     {'name': 'Mark Watney',   '2000-01': 2000, '2000-02': 2000, '2000-03': 2000},
...     {'name': 'Melissa Lewis', '2000-01': 3000, '2000-02': 3000, '2000-03': 3000},
...     {'name': 'Rick Martinez', '2000-03': 2500},
...     {'name': 'Alex Vogel',    '2000-01': 2500, '2000-02': 2500, '2000-03': 2500},
... ]

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee['2000-01']
...     february = employee['2000-02']
...     march = employee['2000-03']
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}'
...
Traceback (most recent call last):
KeyError: '2000-01'

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', 'n/a')
...     february = employee.get('2000-02', 'n/a')
...     march = employee.get('2000-03', 'n/a')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez          n/a       n/a   2500
Alex Vogel            2500      2500   2500
<BLANKLINE>

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', '-')
...     february = employee.get('2000-02', '-')
...     march = employee.get('2000-03', '-')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez            -         -   2500
Alex Vogel            2500      2500   2500
<BLANKLINE>

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', '')
...     february = employee.get('2000-02', '')
...     march = employee.get('2000-03', '')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez                          2500
Alex Vogel            2500      2500   2500
<BLANKLINE>


Assignments
-----------
.. literalinclude:: assignments/mapping_getitem_a.py
    :caption: :download:`Solution <assignments/mapping_getitem_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_getitem_b.py
    :caption: :download:`Solution <assignments/mapping_getitem_b.py>`
    :end-before: # Solution

.. todo:: Assignment with dict get item []
.. todo:: Assignment with dict get item .get()
.. todo:: Assignment with dict get item .get() with default value

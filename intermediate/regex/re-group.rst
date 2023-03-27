Regex RE Group
==============
* Match particular parts of a string
* Possible to name matches


Syntax
------
Define:

    * ``(...)`` - Positional group
    * ``(?P<name>...)`` - Named group
    * ``(?:...)`` - Non-matching group
    * ``(?#...)`` - Comment

Backreference:

    * ``(?P=name)``- Backreferencing by group name
    * ``\number`` - Backreferencing by group number

Example:

    * ``(?P<tag><.*?>)text(?P=tag)``
    * ``(?P<tag><.*?>)text\1``
    * ``(.+) \1`` matches ``the the`` or ``55 55``
    * ``(.+) \1`` not matches ``thethe`` (note the space after the group)


SetUp
-----
>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'


Positional Groups
-----------------
>>> result = re.search(r'(\w+) (\w+)', TEXT)
>>>
>>> result
<re.Match object; span=(0, 11), match='Mark Watney'>
>>>
>>> result.group()
'Mark Watney'
>>>
>>> result.group(1)
'Mark'
>>>
>>> result.group(2)
'Watney'
>>>
>>> result.groups()
('Mark', 'Watney')


Named Groups
------------
* Usage of group in ``re.match()``

>>> result = re.match(r'(?P<firstname>\w+) (?P<lastname>\w+)', TEXT)
>>>
>>> result.group('firstname')
'Mark'
>>>
>>> result.group('lastname')
'Watney'
>>>
>>> result.group(1)
'Mark'
>>>
>>> result.group(2)
'Watney'
>>>
>>> result.groups()
('Mark', 'Watney')
>>>
>>> result.groupdict()
{'firstname': 'Mark', 'lastname': 'Watney'}


Non-Capturing Groups
--------------------
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>\w+)'
>>> day = r'(?P<day>\d{1,2})'

>>> re.findall(f'{month} {day}th, {year}', TEXT)
[('Nov', '7', '2035')]
>>>
>>> re.findall(f'{month} {day}st|nd|rd|th, {year}', TEXT)
[('', '', ''), ('', '', '2035')]
>>>
>>> re.findall(f'{month} {day}[stndrdth], {year}', TEXT)
[]
>>>
>>> re.findall(f'{month} {day}[st]|[nd]|[rd]|[th], {year}', TEXT)
[('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('Nov', '7', ''), ('', '', '2035')]
>>>
>>> re.findall(f'{month} {day}(st|nd|rd|th), {year}', TEXT)
[('Nov', '7', 'th', '2035')]
>>>
>>> re.findall(f'{month} {day}(?:st|nd|rd|th), {year}', TEXT)
[('Nov', '7', '2035')]


Use Case - 0x01
---------------
>>> line = 'value=123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]

>>> line = 'value = 123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]


Use Case - 0x02
---------------
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>\w+)'
>>> day = r'(?P<day>\d{1,2})'

Positional Groups:

>>> re.findall('Ares \d', TEXT)
['Ares 3']
>>>
>>> re.findall('Ares (\d)', TEXT)
['3']

>>> re.findall(r'Nov [0-9]th', TEXT)
['Nov 7th']
>>>
>>> re.findall(r'Nov ([0-9])th', TEXT)
['7']
>>>
>>> re.findall(r'Nov [0-9](st|nd|th|rd)', TEXT)
['th']

Named Groups:

>>> re.findall(f'{month} {day}th, {year}', TEXT)
[('Nov', '7', '2035')]
>>>
>>> result = re.search(f'{month} {day}th, {year}', TEXT)
>>>
>>> result.span()
(41, 54)
>>>
>>> result.group()
'Nov 7th, 2035'
>>> result.group(1)
'Nov'
>>> result.group(2)
'7'
>>> result.group(3)
'2035'
>>>
>>> result.group('month')
'Nov'
>>> result.group('day')
'7'
>>> result.group('year')
'2035'
>>>
>>> result.groups()
('Nov', '7', '2035')
>>>
>>> result.groupdict()
{'month': 'Nov', 'day': '7', 'year': '2035'}

Non-capturing Groups:

>>> re.findall(f'{month} {day}(st|nd|rd|th), {year}', TEXT)
[('Nov', '7', 'th', '2035')]
>>>
>>> re.findall(f'{month} {day}(?:st|nd|rd|th), {year}', TEXT)
[('Nov', '7', '2035')]

Comments:

>>> re.findall(f'{month} {day}th(?#ordinal), {year}', TEXT)
[('Nov', '7', '2035')]

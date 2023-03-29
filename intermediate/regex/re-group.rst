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
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'


Positional Groups
-----------------
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

>>> result = re.search(r'([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)
>>>
>>> result
<re.Match object; span=(11, 22), match='Mark Watney'>
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

>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

>>> result = re.search(r'(?P<firstname>[A-Z][a-z]+) (?P<lastname>[A-Z][a-z]+)', TEXT)
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
>>> TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>\w+)'
>>> day = r'(?P<day>\d{1,2})'

>>> re.findall(f'{month} {day}st, {year}', TEXT)
[('Jan', '1', '2000')]
>>>
>>> re.findall(f'{month} {day}st|nd|rd|th, {year}', TEXT)
[('Jan', '1', '')]
>>>
>>> re.findall(f'{month} {day}[stndrdth], {year}', TEXT)
[]
>>>
>>> re.findall(f'{month} {day}[st]|[nd]|[rd]|[th], {year}', TEXT)  # doctest: +NORMALIZE_WHITESPACE
[('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''), ('', '', ''),
 ('', '', ''), ('', '', ''), ('', '', ''), ('Jan', '1', ''), ('', '', '2000')]
>>>
>>> re.findall(f'{month} {day}(st|nd|rd|th), {year}', TEXT)
[('Jan', '1', 'st', '2000')]
>>>
>>> re.findall(f'{month} {day}(?:st|nd|rd|th), {year}', TEXT)
[('Jan', '1', '2000')]


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

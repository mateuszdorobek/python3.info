Syntax Group
============
* Catch expression results
* Can be named or positional
* Note, that for backreference, must use raw-sting or double backslash
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group
* ``(?P<mygroup>...)`` - named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment


SetUp
-----
>>> import re


Positional Group
----------------
* ``(...)`` - unnamed (positional) group

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> re.findall(r'\dth', TEXT)
['7th']
>>>
>>> re.findall(r'(\d{1,2})th', TEXT)
['7']
>>>
>>> re.findall(r'\d{1,2}(th)', TEXT)
['th']

>>> re.findall(r'\d{1,2}:\d{2}', TEXT)
['13:37']
>>>
>>> re.findall(r'(\d{1,2}):\d{2}', TEXT)
['13']
>>>
>>> re.findall(r'\d{1,2}:(\d{2})', TEXT)
['37']
>>>
>>> re.findall(r'(\d{1,2}):(\d{2})', TEXT)
[('13', '37')]

>>> re.findall(r'([A-Z][a-z]+\s[A-Z][a-z]+)', TEXT)
['Mark Watney']
>>>
>>> re.findall(r'([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)
[('Mark', 'Watney')]
>>>
>>> re.findall(r'([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)[0]
('Mark', 'Watney')

>>> firstname = r'([A-Z][a-z]+)'
>>> lastname = r'([A-Z][a-z]+)'
>>>
>>> re.findall(f'{firstname} {lastname}', TEXT)[0]
('Mark', 'Watney')

>>> firstname = r'([A-Z][a-z]+)'
>>> lastname = r'([A-Z][a-z]+)'
>>> name = f'{firstname} {lastname}'
>>>
>>> re.findall(name, TEXT)[0]
('Mark', 'Watney')

>>> firstname = r'[A-Z][a-z]+'
>>> lastname = r'[A-Z][a-z]+'
>>> name = f'({firstname}) ({lastname})'
>>>
>>> re.findall(name, TEXT)[0]
('Mark', 'Watney')


Named Group
-----------
* ``(?P<mygroup>...)`` - named group `mygroup`


>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> firstname = r'[A-Z][a-z]+'
>>> lastname = r'[A-Z][a-z]+'
>>> name = f'(?P<firstname>{firstname}) (?P<lastname>{lastname})'
>>>
>>> re.findall(name, TEXT)
[('Mark', 'Watney')]
>>>
>>> re.search(name, TEXT)
<re.Match object; span=(0, 11), match='Mark Watney'>
>>>
>>> re.search(name, TEXT).groups()
('Mark', 'Watney')
>>>
>>> re.search(name, TEXT).groupdict()
{'firstname': 'Mark', 'lastname': 'Watney'}

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>> time = r'(?P<hour>\d{1,2}):(?P<minute>\d{1,2})'
>>>
>>> re.findall(time, TEXT)
[('13', '37')]
>>>
>>> re.search(time, TEXT).groups()
('13', '37')
>>>
>>> re.search(time, TEXT).group(0)
'13:37'
>>>
>>> re.search(time, TEXT).group(1)
'13'
>>>
>>> re.search(time, TEXT).group(2)
'37'
>>>
>>> re.search(time, TEXT).groupdict()
{'hour': '13', 'minute': '37'}


Non-Capturing Group
-------------------
* ``(?:...)``

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> re.findall(r'\w{3} \d{1,2}th, \d{4}', TEXT)
['Nov 7th, 2035']
>>>
>>> re.findall(r'\w{3} \d{1,2}st|nd|rd|th, \d{4}', TEXT)
['nd', 'th, 2035']
>>>
>>> re.findall(r'\w{3} \d{1,2}(st|nd|rd|th), \d{4}', TEXT)
['th']
>>>
>>> re.findall(r'\w{3} \d{1,2}(?:st|nd|rd|th), \d{4}', TEXT)
['Nov 7th, 2035']
>>>
>>> re.findall(r'(\w{3}) (\d{1,2})(?:st|nd|rd|th), (\d{4})', TEXT)
[('Nov', '7', '2035')]
>>>
>>> re.findall(r'(\w{3}) (\d{1,2})(st|nd|rd|th), (\d{4})', TEXT)
[('Nov', '7', 'th', '2035')]

>>> date = r'(\w{3} \d{1,2}(?:st|nd|rd|th), \d{4})'
>>> re.findall(date, TEXT)
['Nov 7th, 2035']

>>> year = r'\d{4}'
>>> month = r'\w{3}'
>>> day = r'\d{1,2}'
>>>
>>> re.findall(f'{month} {day}(st|nd|rd|th), {year}', TEXT)
['th']
>>>
>>> re.findall(f'{month} {day}(?:st|nd|rd|th), {year}', TEXT)
['Nov 7th, 2035']


Comment
-------
* ``(?#...)`` - comment

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> re.findall(r'\d{4}(?#year)', TEXT)
['2035']
>>>
>>> re.findall(r'\d{1,2}(?#hour):\d{2}(?#minute)', TEXT)
['13:37']

>>> hour = r'\d{1,2}(?#hour)'
>>> minute = r'\d{2}(?#minute)'
>>> time = f'{hour}:{minute}'
>>>
>>> re.findall(time, TEXT)
['13:37']
>>>
>>> time
'\\d{1,2}(?#hour):\\d{2}(?#minute)'


Backreference
-------------
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``(?P=name)`` - backreferencing by group name
* ``\number`` - backreferencing by group number

>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>[A-Z][a-z]{2})'
>>> day = r'(?P<day>\d{1,2})'
>>> date = f'{month} {day}(?:st|nd|rd|th), {year}'
>>>
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>>
>>> re.sub(date, '\g<3> \g<1> \g<2>', TEXT)
'Mark Watney of Ares 3 landed on Mars on: 2035 Nov 7 at 13:37'
>>>
>>> re.sub(date, '\g<year> \g<month> \g<day>', TEXT)
'Mark Watney of Ares 3 landed on Mars on: 2035 Nov 7 at 13:37'

Although this is not working in Python:

>>> re.sub(f'{month} {day}th, {year}', '(?P=day) (?P=month) (?P=year)', TEXT)
'Mark Watney of Ares 3 landed on Mars on: (?P=day) (?P=month) (?P=year) at 13:37'

Example:

>>> html = '<p>We choose to go to the <strong>Moon</strong></p>'
>>>
>>>
>>> re.findall('<(?P<tagname>[a-z]+)>.*</(?P=tagname)>', html)
['p']
>>>
>>> re.findall('<(?P<tagname>[a-z]+)>(.*)</(?P=tagname)>', html)
[('p', 'We choose to go to the <strong>Moon</strong>')]


Examples
--------
* ``(\w+)`` - word character (including unicode chars, numbers an underscores)
* ``\d+(\.\d+)?`` - float with optional decimals
* ``\d+(,\d+)?`` - number with coma (``,``) as  thousands separator
* ``(?P<word>\w+)`` - name group `word` with ``\w+`` with at least one word character (including unicode chars, numbers an underscores)
* ``(?P<tag><.*?>).+(?P=tag)`` - matches text inside of a ``<tag>`` (opening and closing tag is the same)
* ``(.+) \1`` - matches ``the the`` or ``55 55``
* ``(.+) \1`` - not matches ``thethe`` (note the space after the group)

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> re.findall(r'\d{,2}(st|nd|rd|th)?', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
 '', '', '', '', '', 'nd', '', '', '', '', '', '', '', '', '', '', '', '', '',
 '', '', '', '', '', '', 'th', '', '', '', '', '', '', '', '', '', '', '', '']
>>>
>>> re.findall(r'\d{1,2}(st|nd|rd|th)?', TEXT)
['', 'th', '', '', '', '']
>>>
>>> re.findall(r'\d{1,2}(st|nd|rd|th)+?', TEXT)
['th']
>>>
>>> re.findall(r'\d{1,2}st|nd|rd|th+?', TEXT)  # nd is also in word `landed`
['nd', 'th']
>>>
>>> re.findall(r'\d{1,2}(?:st|nd|rd|th)+?', TEXT)
['7th']
>>>
>>> re.findall(r'(\d{1,2})(st|nd|rd|th)+?', TEXT)
[('7', 'th')]
>>>
>>> re.findall(r'(\d{1,2})(?:st|nd|rd|th)+?', TEXT)
['7']
>>>
>>> re.findall(r'(\w{3}) (\d{1,2})(?:st|nd|rd|th)+?, (\d{4})', TEXT)
[('Nov', '7', '2035')]
>>>
>>> re.findall(r'(\w{3}) (\d{1,2})(?:st|nd|rd|th)+?, (\d{4})', TEXT)[0]
('Nov', '7', '2035')
>>>
>>> re.findall(r'(\w{3} \d{1,2}(?:st|nd|rd|th)+?, \d{4})', TEXT)
['Nov 7th, 2035']


Use Case - 0x01
---------------
* Dates

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>\w{3})'
>>> day = r'(?P<day>\d{1,2}(?:st|nd|rd|th)+?)'
>>> date = f'{month} {day}, {year}'
>>>
>>> re.search(date, TEXT).groupdict()
{'month': 'Nov', 'day': '7th', 'year': '2035'}


Use Case - 0x02
---------------
>>> import re

>>> line = 'value=123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]

>>> line = 'value = 123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]


Use Case - 0x03
---------------
>>> import re
>>>
>>>
>>> variable = r'(?P<variable>\w+)'
>>> space = r'\s?'  # optional space
>>> value = r'(?P<value>.+)'
>>> assignment = f'^{variable}{space}={space}{value}$'
>>>
>>> line_of_code = 'myvar = 123'
>>> re.findall(assignment, line_of_code)
[('myvar', '123')]


Use Case - 0x04
---------------
>>> import re
>>>
>>>
>>> variable = r'(?P<variable>\w+)'
>>> space = r'\s?(?#optional space)'
>>> value = r'(?P<value>.+)'
>>> assignment = f'^{variable}{space}={space}{value}$'
>>>
>>> assignment
'^(?P<variable>\\w+)\\s?(?#optional space)=\\s?(?#optional space)(?P<value>.+)$'


Use Case - 0x05
---------------
>>> import re
>>>
>>>
>>> HTML = '<p>Hello World</p>'
>>>
>>> search = r'<p>(.+)</p>'
>>> replace = r'<strong>\g<1></strong>'
>>>
>>> re.sub(search, replace, HTML)
'<strong>Hello World</strong>'


Use Case - 0x06
---------------
>>> import re
>>>
>>>
>>> HTML = '<p>Hello World</p>'
>>>
>>> search = r'<p>(?P<text>.+)</p>'
>>> replace = r'<strong>\g<text></strong>'
>>>
>>> re.sub(search, replace, HTML)
'<strong>Hello World</strong>'


Use Case - 0x07
---------------
>>> import re
>>>
>>>
>>> HTML = '<p>Hello World</p>'
>>> tag = re.findall(r'<(?P<tag>.+)>(?:.+)</(?P=tag)>', HTML)
>>>
>>> tag
['p']


Use Case - 0x08
---------------
>>> import re
>>>
>>>
>>> HTML = '<p>Hello World</p>'
>>>
>>> re.findall(r'<(?P<tag>.*?)>(.*?)</(?P=tag)>', HTML)
[('p', 'Hello World')]


Assignments
-----------
.. literalinclude:: assignments/re_syntax_group_a.py
    :caption: :download:`Solution <assignments/re_syntax_group_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_group_b.py
    :caption: :download:`Solution <assignments/re_syntax_group_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_syntax_group_c.py
    :caption: :download:`Solution <assignments/re_syntax_group_c.py>`
    :end-before: # Solution

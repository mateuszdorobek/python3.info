.. testsetup::

    # doctest: +SKIP_FILE


>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>>
>>> re.findall('[0-9][0-9][0-9][0-9]', TEXT)
['2035']
>>>
>>> re.findall('\d\d\d\d', TEXT)
['2035']
>>>
>>> re.findall('\d{4}', TEXT)
['2035']
>>>
>>>
>>> re.findall('{4}', TEXT)
error: nothing to repeat

>>>
>>> re.findall('.{4}', TEXT)
['Mark', ' Wat', 'ney ', 'of A', 'res ', '3 la', 'nded', ' on ', 'Mars', ' on:', ' Nov', ' 7th', ', 20', '35 a', 't 13']
>>> re.findall('a{4}', TEXT)
[]




>>> text = 'You can write floats as: 1.2 and .3 or 4.'
>>>
>>> re.findall('\d+\.\d+', text)
['1.2']
>>>
>>>
>>> re.findall('\d*\.\d*', text)
['1.2', '.3', '4.']
>>>
>>>
>>> text = 'Floats can have diffent notations. You can write floats as: 1.2 and .3 or 4.'
>>>
>>>
>>> re.findall('\d*\.\d*', text)
['.', '1.2', '.3', '4.']
>>>
>>> re.findall('\d+\.\d*|\d*\.\d+', text)
['1.2', '.3', '4.']



>>> re.findall('.', TEXT)
['M', 'a', 'r', 'k', ' ', 'W', 'a', 't', 'n', 'e', 'y', ' ', 'o', 'f', ' ', 'A', 'r', 'e', 's', ' ', '3', ' ', 'l', 'a', 'n', 'd', 'e', 'd', ' ', 'o', 'n', ' ', 'M', 'a', 'r', 's', ' ', 'o', 'n', ':', ' ', 'N', 'o', 'v', ' ', '7', 't', 'h', ',', ' ', '2', '0', '3', '5', ' ', 'a', 't', ' ', '1', '3', ':', '3', '7']
>>>
>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>>
>>>
>>> re.findall('^.', TEXT)
['M']
>>>
>>> re.findall('.$', TEXT)
['7']
>>>
>>> re.findall('\A.', TEXT)
['M']
>>> re.findall('.\Z', TEXT)
['7']
>>>
>>>
>>> text = """We choose to go to the moon.
... We choose to go to the moon
... in this decade and do the other things,
... not because they are easy, but because they are hard,
... because that goal will serve to organize and measure
... the best of our energies and skills,
... because that challenge is one that we are willing to accept,
... one we are unwilling to postpone,
... and one which we intend to win,
... and the others, too."""
>>>
>>> re.findall('^.', text)
['W']
>>>
>>> re.findall('\A.', text)
['W']
>>>
>>> re.findall('^.', text, flags=re.MULTILNE)
AttributeError: module 're' has no attribute 'MULTILNE'

>>> re.findall('^.', text, flags=re.MULTILINE)
['W', 'W', 'i', 'n', 'b', 't', 'b', 'o', 'a', 'a']
>>>
>>> re.findall('.$', text)
['.']
>>>
>>> re.findall('.$', text, flags=re.MULTILINE)
[' ', ' ', ' ', ' ', 'e', ' ', ',', ' ', ',', '.']
>>>
>>> text = """We choose to go to the moon.
... We choose to go to the moon in this decade and do the other things,
... not because they are easy, but because they are hard,
... because that goal will serve to organize and measure the best of our energies and skills,
... because that challenge is one that we are willing to accept,
... one we are unwilling to postpone,
... and one which we intend to win,
... and the others, too."""




>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>> re.findall('[A-Z][a-z]+', TEXT)
['Mark', 'Watney', 'Ares', 'Mars', 'Nov']
>>>
>>> re.findall('[A-Z][a-z]+ [A-Z][a-z]+', TEXT)
['Mark Watney']
>>>
>>> re.findall('[A-Z][a-z]+ ([A-Z][a-z]+)', TEXT)
['Watney']
>>>
>>> re.findall('([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)
[('Mark', 'Watney')]

>>> result = re.search('([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)
>>> result.group(1)
'Mark'
>>> result.group(2)
'Watney'
>>> result.groups()
('Mark', 'Watney')

>>> result = re.search('(?P<firstname>[A-Z][a-z]+) (?P<lastname>[A-Z][a-z]+)', TEXT)
>>> result.group(1)
'Mark'
>>> result.group(2)
'Watney'
>>> result.groups()
('Mark', 'Watney')
>>> result.group('firstname')
'Mark'
>>> result.group('lastname')
'Watney'
>>> result.groupdict()
{'firstname': 'Mark', 'lastname': 'Watney'}




>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>>
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>[A-Z][a-z]+)'
>>> day = r'(?P<day>\d{1,2})(?:st|nd|rd|th)'
>>>
>>> date = f'{month} {day}, {year}'
>>>
>>> re.findall(date, TEXT)
[('Nov', '7', '2035')]
>>>
>>> result = re.search(date, TEXT)
>>>
>>> result.groupdict()
{'month': 'Nov', 'day': '7', 'year': '2035'}
>>>
>>> result.group('year')
'2035'
>>> result.group('month')
'Nov'
>>> result.group('day')
'7'
>>>
>>> month, day, year = result.groups()
>>>
>>> month
'Nov'
>>> day
'7'
>>> year
'2035'
>>>
>>> date
'(?P<month>[A-Z][a-z]+) (?P<day>\\d{1,2})(?:st|nd|rd|th), (?P<year>\\d{4})'






>>> import re
>>>
>>> re.findall()    # znajdź wszystkie wystąpienia wzorca w tekście, wynik jako list[str]
>>> re.finditer()   # znajdź wszystkie wystąpienia wzorca w tekście, wynik jako Iterator[str]
>>> re.search()     # czy w tekście jest wzorzec, wynik jako re.Match | None (kończy po pierwszym znalezieniu)
>>> re.match()      # czy tekst pasuje do wzorca, wynik jako re.Match | None (do walidacji, np. pesel, nip, email)
>>> re.split()      # podziel tekst po wzorcu
>>> re.sub()        # podmień wyrażenie w tekście
>>> re.compile()    # zbuduj wyrażenie regularne do późniejszego wykorzystania


>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'

>>> def contains(pattern, TEXT):
...     if re.search(pattern, TEXT):
...         return True
...     else:
...         return False
...
>>>
>>> contains('a', TEXT)
True
>>>
>>> contains('x', TEXT)
False



>>> def valid(pattern, STRING):
...     if re.match(pattern, STRING):
...         return True
...     else:
...         return False
...
>>> valid('^[0-9]+$', '19623771263812')
True
>>>
>>> valid('^[0-9]+$', '1962377xxx8d12')
False


>>> text = 'hello world, jak      się masz'
>>>
>>> text.split(' ')
['hello', 'world,', 'jak', '', '', '', '', '', 'się', 'masz']
>>>
>>>
>>> re.split('\s+', text)
['hello', 'world,', 'jak', 'się', 'masz']
>>>
>>>
>>> text.split()
['hello', 'world,', 'jak', 'się', 'masz']



>>> TEXT
'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 13:37'
>>>
>>> re.sub('[0-9]', 'X', TEXT)
'Mark Watney of Ares X landed on Mars on: Nov Xth, XXXX at XX:XX'


>>> text = 'cześć'
>>>
>>>
>>> re.findall('[a-z]', text)
['c', 'z', 'e']
>>>
>>> re.findall('\w', text)
['c', 'z', 'e', 'ś', 'ć']
>>>
>>>
>>> re.findall('\w', text, flags=re.ASCII)
['c', 'z', 'e']
>>>
>>> re.findall('\w', text, flags=re.UNICODE)
['c', 'z', 'e', 'ś', 'ć']

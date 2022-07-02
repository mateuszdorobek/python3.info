Syntax Quantifier
=================
* Quantifier specifies how many occurrences of preceding qualifier or identifier
* Exact
* Greedy
* Lazy

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\d', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '7']

>>> re.findall(r'\d\d\d\d', TEXT)
['2035']


Exact
-----
* Exact match
* ``{n}`` - exactly `n` repetitions, prefer longer

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[0-9]{2}', TEXT)
['20', '35', '37']

>>> re.findall(r'\d{2}', TEXT)
['20', '35', '37']


Greedy
------
* Prefer longest matches
* Works better with numbers
* Not that good results for text
* Default behavior
* ``{,n}`` - maximum `n` repetitions, prefer longer
* ``{n,}`` - minimum `n` repetitions, prefer longer
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer  (alias to ``{0,1}``)

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\d{2,4}', TEXT)
['2035', '37']


Lazy
----
* Prefer shortest matches
* Works better with text
* Not that good results for numbers
* Non-greedy
* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\d{2,4}?', TEXT)
['20', '35', '37']


Greedy vs. Lazy
---------------
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\d{2,4}', TEXT)  # Greedy
['2035', '37']

>>> re.findall(r'\d{2,4}?', TEXT)  # Lazy
['20', '35', '37']

Greedy vs Lazy in exact match has no difference:

>>> re.findall('\d{2}?', TEXT)
['20', '35', '37']

>>> re.findall('\d{2}', TEXT)
['20', '35', '37']


Special
-------
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall('\d{0,}', TEXT) == re.findall('\d*', TEXT)
True

>>> re.findall('\d{1,}', TEXT) == re.findall('\d+', TEXT)
True

>>> re.findall('\d+', TEXT)
['3', '7', '2035', '1', '37']

>>> re.findall('\d*', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
 '', '', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
 '', '', '', '', '', '', '', '', '', '7', '', '', '', '', '2035', '', '',
 '', '', '1', '', '37', '', '', '', '']


Examples
--------
* ``[0-9]{2}`` - exactly two digits from `0` to `9`
* ``\d{2}`` - exactly two digits from `0` to `9`
* ``[A-Z]{2,10}`` - two to ten uppercase letters from `A` to `Z`
* ``[A-Z]{2-10}-[0-9]{,5}`` - two to ten uppercase letters from `A` to `Z` followed by dash (`-`) and at least five numbers
* ``[a-z]+`` - at least one lowercase letter from `a` to `z`, but try to fit the longest match
* ``\d+`` - number
* ``\d+\.\d+`` - float


Use Case - 0x01
---------------
* Float

>>> import re
>>> TEXT = 'Pi number is 3.1415...'

>>> pi = re.findall('\d+\.\d+', TEXT)
>>> pi
['3.1415']


Use Case - 0x02
---------------
* Time

>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall('\d\d:\d\d', TEXT)
[]

>>> re.findall('\d\d?:\d\d', TEXT)
['1:37']


Use Case - 0x03
---------------
* Date

>>> import re
>>> from datetime import datetime

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>> result = re.findall('\w{3} \d{1,2}th, \d{4}', TEXT)

>>> result
['Nov 7th, 2035']

>>> datetime.strptime(result[0], '%b %dth, %Y').date()
datetime.date(2035, 11, 7)


Use Case - 0x04
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


Use Case - 0x05
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'

>>> re.findall('<p>.*</p>', HTML)
['<p>Paragraph 1</p><p>Paragraph 2</p>']

>>> re.findall('<p>.*?</p>', HTML)
['<p>Paragraph 1</p>', '<p>Paragraph 2</p>']


Use Case - 0x06
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'

>>> re.findall('<p>', HTML)
['<p>', '<p>']

>>> re.findall('</p>', HTML)
['</p>', '</p>']

>>> re.findall('</?p>', HTML)
['<p>', '</p>', '<p>', '</p>']


Use Case - 0x07
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'

>>> re.findall('<.+>', HTML)
['<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>']

>>> re.findall('<.+?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']

>>> re.findall('</?.+?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']

>>> re.findall('</?(.+?)>', HTML)
['h1', 'h1', 'p', 'p', 'p', 'p']

>>> tags = re.findall('</?(.+?)>', HTML)
>>> sorted(set(tags))
['h1', 'p']


Use Case - 0x08
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'

>>> re.findall('</?.*>', HTML)
['<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>']

>>> re.findall('</?.*?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']

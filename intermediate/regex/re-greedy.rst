Regex RE Lazy
=============
* Adding ``?`` after the qualifier makes it non-greedy
* Greedy - as many as possible
* Lazy - as few as possible:
* ``?`` - zero or one (greedy)
* ``*`` - zero or more (greedy)
* ``+`` - one or more (greedy)
* ``??`` - zero or one (lazy)
* ``*?`` - zero or more (lazy)
* ``+?`` - one or more (lazy)

Greedy - as many as possible:

    * ``?`` - zero or one (greedy)
    * ``*`` - zero or more (greedy)
    * ``+`` - one or more (greedy)

Lazy - as few as possible:

    * ``??`` - zero or one (lazy)
    * ``*?`` - zero or more (lazy)
    * ``+?`` - one or more (lazy)


Example
-------
Usage of greedy and non-greedy search in ``re.findall()``:

>>> import re
>>>
>>>
>>> TEXT = '<p>First Paragraph</p>'

Greedy:

>>> re.findall(r'<.*>', TEXT)
['<p>First Paragraph</p>']

Lazy:

>>> re.findall(r'<.*?>', TEXT)
['<p>', '</p>']

Usage of greedy and lazy search with groups:

>>> re.findall(r'<(.*)>', TEXT)
['p>First Paragraph</p']

>>> re.findall(r'<(.*?)>', TEXT)
['p', '/p']

>>> re.findall(r'</?(.*?)>', TEXT)
['p', 'p']


Assignments
-----------
.. literalinclude:: assignments/re_greedy_a.py
    :caption: :download:`Solution <assignments/re_greedy_a.py>`
    :end-before: # Solution

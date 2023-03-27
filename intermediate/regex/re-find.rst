Regex RE Findall, Finditer
==========================
* ``re.findall()``
* ``re.finditer()``


Example
-------
Usage of ``re.findall()`` and ``re.finditer()``:

>>> import re
>>>
>>>
>>> HTML = """
...     <h1>Header</h1>
...     <p>First Paragraph</p>
...     <p>Second Paragraph</p>
...     <p>Third Paragraph</p>
... """
>>>
>>> re.findall(r'<h1>(.*)</h1>', HTML)
['Header']
>>>
>>> re.findall(r'<p>(.*)</p>', HTML)
['First Paragraph', 'Second Paragraph', 'Third Paragraph']


Use Case - 0x01
---------------
* Find all JIRA issue keys in commit message

>>> import re
>>>
>>>
>>> TEXT = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
>>> issuekey = r'[A-Z]{2,10}-[0-9]{1,6}'
>>>
>>> re.findall(issuekey, TEXT)
['MYPROJ-1337', 'MYPROJ-997']


Use Case - 0x02
---------------
* Find All Adverbs

>>> import re
>>>
>>>
>>> TEXT = 'He was carefully disguised but captured quickly by police.'
>>> adverbs = r'\w+ly'
>>>
>>> re.findall(adverbs, TEXT)
['carefully', 'quickly']


Assignments
-----------
.. literalinclude:: assignments/re_find_a.py
    :caption: :download:`Solution <assignments/re_find_a.py>`
    :end-before: # Solution

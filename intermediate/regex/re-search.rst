Regex RE Search
===============
* ``re.search()``
* Searches if pattern contains a string


Example
-------
* Usage of ``re.search()``

>>> import re
>>>
>>>
>>> def contains(pattern, text):
...     if re.search(pattern, text):
...         return True
...     else:
...         return False
>>>
>>>
>>> COMMIT_MESSAGE = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
>>> jira_issuekey = r'[A-Z]{2,10}-[0-9]{1,6}'
>>> redmine_number = r'#[0-9]+'
>>>
>>> contains(jira_issuekey, COMMIT_MESSAGE)
True
>>> contains(redmine_number, COMMIT_MESSAGE)
False

>>> import re
>>>
>>>
>>> TEXT = 'We choose to go to the moon.'
>>>
>>> result = re.search(r'moon', TEXT)
>>>
>>> result
<re.Match object; span=(23, 27), match='moon'>
>>>
>>> result.span()
(23, 27)
>>>
>>> result.regs
((23, 27),)
>>>
>>> TEXT[23]
'm'
>>> TEXT[23:27]
'moon'

>>> import re
>>>
>>>
>>> TEXT = 'We choose to go to the moon.'
>>>
>>>
>>> result = re.search(r'Mars', TEXT)
>>>
>>> result.group()
Traceback (most recent call last):
AttributeError: 'NoneType' object has no attribute 'group'
>>>
>>> result = re.search(r'Mars', TEXT)
>>> if result:
...     result.group()
>>>
>>>
>>> if result := re.search(r'Mars', TEXT):
...     result.group()


Assignments
-----------
.. literalinclude:: assignments/re_search_a.py
    :caption: :download:`Solution <assignments/re_search_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_b.py
    :caption: :download:`Solution <assignments/re_search_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_c.py
    :caption: :download:`Solution <assignments/re_search_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_d.py
    :caption: :download:`Solution <assignments/re_search_d.py>`
    :end-before: # Solution

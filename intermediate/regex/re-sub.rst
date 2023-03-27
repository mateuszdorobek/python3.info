Regex RE Substitute
===================
* ``re.sub()``
* Replace matched substring with text


Examples
--------
Usage of ``re.sub()``:

>>> import re
>>>
>>>
>>> DATA = 'Baked Beans And Spam'
>>> pattern = r'\s[a-z]{3}\s'
>>>
>>> re.sub(pattern, ' & ', DATA, flags=re.IGNORECASE)
'Baked Beans & Spam'

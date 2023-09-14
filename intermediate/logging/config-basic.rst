Logging Config Basic
====================
* ``filename`` - Specifies that a ``FileHandler`` be created, using the specified filename, rather than a ``StreamHandler``
* ``filemode`` - If filename is specified, open the file in this mode. Defaults to ``'a'``
* ``format`` - Use the specified format string for the handler
* ``datefmt`` - Use the specified date/time format, as accepted by ``time.strftime()``
* ``style`` - If format is specified, use this style for the format string. One of ``'%'``, ``'{'`` or ``'$'`` for printf-style, ``str.format()`` or ``string.Template`` respectively. Defaults to ``'%'``
* ``level`` - Set the root logger level to the specified level
* ``stream`` - Use the specified stream to initialize the ``StreamHandler``. Note that this argument is incompatible with ``filename`` - if both are present, a ``ValueError`` is raised
* ``handlers`` - If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don't already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with ``filename`` or ``stream`` - if both are present, a ``ValueError`` is raised

>>> import logging
>>>
>>> logging.basicConfig(
...     level='DEBUG',
...     datefmt='%Y-%m-%d %H:%M:%S',
...     format='{asctime} {levelname} {message}',
...     style='{',
...     filename='/tmp/myfile.log',
...     filemode='w',
... )

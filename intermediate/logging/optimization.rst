Logging Optimization
====================
Formatting of message arguments is deferred until it cannot be avoided.
However, computing the arguments passed to the logging method can also be
expensive, and you may want to avoid doing it if the logger will just throw
away your event. To decide what to do, you can call the isEnabledFor() method
which takes a level argument and returns true if the event would be created
by the Logger for that level of call. You can write code like this:

>>> def expensive_func1(): ...
>>> def expensive_func2(): ...

>>> import logging
>>>
>>>
>>> logger = logging.getLogger(__name__)
>>>
>>> if logger.isEnabledFor(logging.DEBUG):
...     logger.debug('Message with %s, %s', expensive_func1(),
...                                         expensive_func2())

so that if the logger's threshold is set above DEBUG, the calls to
``expensive_func1()`` and ``expensive_func2()`` are never made.

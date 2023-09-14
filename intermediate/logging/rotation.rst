Logging Rotation
================
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers


BaseRotatingHandler
-------------------
* ``logging.handlers.BaseRotatingHandler``

is the base class for handlers that rotate log files at a certain point.
It is not meant to be instantiated directly. Instead, use
``RotatingFileHandler`` or ``TimedRotatingFileHandler``.


RotatingFileHandler
-------------------
* ``logging.handlers.RotatingFileHandler``

instances send messages to disk files, with support for maximum log file
sizes and log file rotation.


TimedRotatingFileHandler
------------------------
* ``logging.handlers.TimedRotatingFileHandler``

instances send messages to disk files, rotating the log file at certain
timed intervals.


Example
-------
>>> from logging.handlers import TimedRotatingFileHandler
>>> from logging import Formatter
>>>
>>> handler = TimedRotatingFileHandler(filename='/tmp/myfile.log', when='midnight')
>>> formatter = Formatter('%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d, %H:%M:%S')
>>> handler.setFormatter(formatter)

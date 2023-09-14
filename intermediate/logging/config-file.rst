Logging Config File
===================


File Config
-----------
* ``logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)``
* https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig

.. code-block:: ini
    :caption: Ini file

    [loggers]
    keys=root,simpleExample

    [handlers]
    keys=consoleHandler

    [formatters]
    keys=simpleFormatter

    [logger_root]
    level=DEBUG
    handlers=consoleHandler

    [logger_simpleExample]
    level=DEBUG
    handlers=consoleHandler
    qualname=simpleExample
    propagate=0

    [handler_consoleHandler]
    class=StreamHandler
    level=DEBUG
    formatter=simpleFormatter
    args=(sys.stdout,)

    [formatter_simpleFormatter]
    format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

.. code-block:: yaml
    :caption: yaml file

    version: 1
    formatters:
      simple:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
      console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    loggers:
      simpleExample:
        level: DEBUG
        handlers: [console]
        propagate: no
    root:
      level: DEBUG
      handlers: [console]

``DictConfig``
--------------
* logging.config.dictConfig(config)
* https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
* https://docs.python.org/3/library/logging.config.html#dictionary-schema-details

.. code-block:: python
    :caption: Ini file

    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': True
            },
            'django.request': {
                'handlers': ['default'],
                'level': 'WARN',
                'propagate': False
            },
        }
    }


.. csv-table:: DictConfig
    :header-rows: 1

    "Format", "Description"
    "filename", "Specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler"
    "filemode", "If filename is specified, open the file in this mode. Defaults to 'a'"
    "format", "Use the specified format string for the handler"
    "datefmt", "Use the specified date/time format, as accepted by time.strftime()"
    "style", "If format is specified, use this style for the format string. One of '%', '{' or '$' for printf-style, str.format() or string.Template respectively. Defaults to '%'"
    "level", "Set the root logger level to the specified level"
    "stream", "Use the specified stream to initialize the StreamHandler. Note that this argument is incompatible with filename - if both are present, a ValueError is raised"
    "handlers", "If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don't already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with filename or stream - if both are present, a ValueError is raised"


Handlers
--------
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

In addition to the base Handler class, many useful subclasses are provided:

    ``StreamHandler``
    instances send messages to streams (file-like objects).

    ``FileHandler``
    instances send messages to disk files.

    ``BaseRotatingHandler``
    is the base class for handlers that rotate log files at a certain point.
    It is not meant to be instantiated directly. Instead, use
    ``RotatingFileHandler`` or ``TimedRotatingFileHandler``.

    ``RotatingFileHandler``
    instances send messages to disk files, with support for maximum log file
    sizes and log file rotation.

    ``TimedRotatingFileHandler``
    instances send messages to disk files, rotating the log file at certain
    timed intervals.

    ``SocketHandler``
    instances send messages to TCP/IP sockets. Since 3.4, Unix domain sockets
    are also supported.

    ``DatagramHandler``
    instances send messages to UDP sockets. Since 3.4, Unix domain sockets are
    also supported.

    ``SMTPHandler``
    instances send messages to a designated email address.


    ``SysLogHandler``
    instances send messages to a Unix syslog daemon, possibly on a remote
    machine.

    ``NTEventLogHandler``
    instances send messages to a Windows NT/2000/XP event log.

    ``MemoryHandler``
    instances send messages to a buffer in memory, which is flushed whenever
    specific criteria are met.

    ``HTTPHandler``
    instances send messages to an HTTP server using either GET or POST
    semantics.

    ``WatchedFileHandler``
    instances watch the file they are logging to. If the file changes, it is
    closed and reopened using the file name. This handler is only useful on
    Unix-like systems; Windows does not support the underlying mechanism used.

    ``QueueHandler``
    instances send messages to a queue, such as those implemented in the queue
    or multiprocessing modules.

    ``NullHandler``
    instances do nothing with error messages. They are used by library
    developers who want to use logging, but want to avoid the 'No handlers
    could be found for logger XXX' message which can be displayed if the
    library user has not configured logging. See Configuring Logging for a
    Library for more information.


Rotate
------
* ``logging.handlers.WatchedFileHandler``
* ``logging.handlers.RotatingFileHandler``
* ``logging.handlers.TimedRotatingFileHandler``

.. code-block:: python

    from logging import handlers

    handler = handlers.TimedRotatingFileHandler(filename, when=LOG_ROTATE)

    handler.setFormatter(logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S'))

    #LOG_ROTATE = midnight
    #set your log format


Examples
--------
.. code-block:: python

    import logging
    import os

    logging.basicConfig(
        format='"{asctime}", "{levelname}", "{message}"',
        filename='...',
        style='{'
    )

    log = logging.getLogger(__name__)
    level = os.getenv('LOG_LEVEL', 'INFO')
    log.setLevel(level)


    log.critical('Critical error... finishing')
    log.error('Some problem but can continue')
    log.warning('Warning, this is important')
    log.info('Typical message')
    log.debug('Debug message with extra information')


    logging.getLogger('requests').setLevel('DEBUG')
    logging.getLogger('_tmp').setLevel('ERROR')


Decorators:

.. code-block:: python

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[{levelname}] {message}',
        style='{'
    )


    def timeit(func):
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_end = datetime.now()
            time = time_end - time_start
            logging.debug(f'Time: {time}')
            return result

        return wrapper


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            logging.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            logging.debug(f'Result: {result}')
            return result

        return wrapper


    @timeit
    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # [DEBUG] Calling: function='add_numbers', args=(1, 2), kwargs={}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000105

    add_numbers(1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000042

    add_numbers(a=1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000040


Optimization
------------
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


Further Reading
---------------
* https://pyvideo.org/pycon-au-2018/a-guided-tour-of-python-logging.html
* https://docs.python.org/3/howto/logging.html
* https://docs.python.org/3/library/logging.html#module-logging
* https://docs.python.org/3/library/logging.config.html#module-logging.config
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

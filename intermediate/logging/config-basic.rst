Logging Config Basic
====================


Konfiguracja formatowania logów
-------------------------------
.. todo:: convert table to CSV

+-------------------------+-----------------------------------------------+
| Format                  | Description                                   |
+=========================+===============================================+
| args                    | The tuple of arguments merged into ``msg`` to |
|                         | produce ``message``, or a dict whose values   |
|                         | are used for the merge (when there is only one|
|                         | argument, and it is a dictionary).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(asctime)s``         | Human-readable time when the                  |
|                         | `LogRecord` was created.  By default          |
|                         | this is of the form '2003-07-08 16:49:45,896' |
|                         | (the numbers after the comma are millisecond  |
|                         | portion of the time).                         |
+-------------------------+-----------------------------------------------+
| ``%(created)f``         | Time when the `LogRecord` was created         |
|                         | (as returned by `time.time`).                 |
+-------------------------+-----------------------------------------------+
| exc_info                | Exception tuple (à la ``sys.exc_info``) or,   |
|                         | if no exception has occurred, ``None``.       |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(filename)s``        | Filename portion of ``pathname``.             |
+-------------------------+-----------------------------------------------+
| ``%(funcName)s``        | Name of function containing the logging call. |
+-------------------------+-----------------------------------------------+
| ``%(levelname)s``       | Text logging level for the message            |
|                         | (``'DEBUG'``, ``'INFO'``, ``'WARNING'``,      |
|                         | ``'ERROR'``, ``'CRITICAL'``).                 |
+-------------------------+-----------------------------------------------+
| ``%(levelno)s``         | Numeric logging level for the message         |
|                         | (`DEBUG`, `INFO`,                             |
|                         | `WARNING`, `ERROR`,                           |
|                         | `CRITICAL`).                                  |
+-------------------------+-----------------------------------------------+
| ``%(lineno)d``          | Source line number where the logging call was |
|                         | issued (if available).                        |
+-------------------------+-----------------------------------------------+
| ``%(module)s``          | Module (name portion of ``filename``).        |
+-------------------------+-----------------------------------------------+
| ``%(msecs)d``           | Millisecond portion of the time when the      |
|                         | `LogRecord` was created.                      |
+-------------------------+-----------------------------------------------+
| ``%(message)s``         | The logged message, computed as ``msg %       |
|                         | args``. This is set when                      |
|                         | `Formatter.format` is invoked.                |
+-------------------------+-----------------------------------------------+
| msg                     | The format string passed in the original      |
|                         | logging call. Merged with ``args`` to         |
|                         | produce ``message``, or an arbitrary object   |
|                         | (see `arbitrary-object-messages`).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(name)s``            | Name of the logger used to log the call.      |
+-------------------------+-----------------------------------------------+
| ``%(pathname)s``        | Full pathname of the source file where the    |
|                         | logging call was issued (if available).       |
+-------------------------+-----------------------------------------------+
| ``%(process)d``         | Process ID (if available).                    |
+-------------------------+-----------------------------------------------+
| ``%(processName)s``     | Process name (if available).                  |
+-------------------------+-----------------------------------------------+
| ``%(relativeCreated)d`` | Time in milliseconds when the LogRecord was   |
|                         | created, relative to the time the logging     |
|                         | module was loaded.                            |
+-------------------------+-----------------------------------------------+
| stack_info              | Stack frame information (where available)     |
|                         | from the bottom of the stack in the current   |
|                         | thread, up to and including the stack frame   |
|                         | of the logging call which resulted in the     |
|                         | creation of this record.                      |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(thread)d``          | Thread ID (if available).                     |
+-------------------------+-----------------------------------------------+
| ``%(threadName)s``      | Thread name (if available).                   |
+-------------------------+-----------------------------------------------+

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

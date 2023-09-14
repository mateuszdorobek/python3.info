Logging Handlers
================
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

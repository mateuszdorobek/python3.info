Logging Formatters
==================

Log Format
----------
>>> import logging
>>>
>>>
>>> logging.basicConfig(format='%(asctime).19s %(levelname)s %(message)s')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Date Format
-----------
>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     format='%(asctime)s %(levelname)s %(message)s',
...     datefmt='"%Y-%m-%d" "%H:%M:%S"',)
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Log Style
---------
Logs has three distinct styles:

    * ``{`` - curly brackets; compare to f-string formatting
    * ``%`` - percent sign; compare to formatting string with ``%``
    * ``$`` - dollar sign; compare to template vars from other languages

Default mode is ``%`` percent.

>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     format='%(asctime)s %(levelname)s %(message)s',
...     style='%')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     format='{asctime}, "{levelname}", "{message}"',
...     style='{')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     format='$asctime, "$levelname", "$message"',
...     style='$')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


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


Use Case - 0x01
---------------
* CSV log format

>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     level='DEBUG',
...     datefmt='"%Y-%m-%d" "%H:%M:%S"',
...     format='{asctime}, "{levelname}", "{message}"',
...     style='{',
...     filename='/tmp/myapp-log.csv')
>>>
>>> log = logging.getLogger(__name__)
>>>
>>> log.critical('Error, cannot continue')
>>> log.error('Error, can continue')
>>> log.warning('Information, warn about something')
>>> log.info('Information, inform about something')
>>> log.debug('Debug, show detailed debugging information')

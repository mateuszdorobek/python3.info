Logging Formatters
==================


SetUp:

>>> import logging


General
-------
* ``name`` - Name of the logger used to log the call
* ``levelname`` - Text logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
* ``message`` - The logged message, computed as ``msg % args``. This is set when ``Formatter.format`` is invoked

>>> logging.basicConfig(format='%(levelname)s %(message)s')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Dates
-----
* ``asctime`` - Human-readable time when ``LogRecord`` was created, example: 1969-07-21 02:56:15,123
* ``created`` - Time when the ``LogRecord`` was created (as returned by ``time.time``)
* ``msecs`` - Millisecond portion of the time when the ``LogRecord`` was created

>>> logging.basicConfig(format='%(asctime).19s %(message)s')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


File and Module
---------------
* ``pathname`` - Full pathname of the source file where the logging call was issued (if available)
* ``filename`` - Filename portion of ``pathname``
* ``module`` - Module (name portion of ``filename``)
* ``funcName`` - Name of function containing the logging call
* ``lineno`` - Source line number where the logging call was issued (if available)

>>> logging.basicConfig(format='%(funcName)s:%(lineno)s %(message)s')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Process and Thread
------------------
* ``process`` - Process ID (if available)
* ``processName`` - Process name (if available)
* ``thread`` - Thread ID (if available)
* ``threadName`` - Thread name (if available)


Other
-----
* You shouldn't need to format this yourself
* ``args`` - The tuple of arguments merged into ``msg`` to produce ``message``, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary)
* ``exc_info`` - Exception tuple (à la ``sys.exc_info``) if no exception has occurred, ``None``
* ``msg`` - The format string passed in the original logging call. Merged with ``args`` to produce ``message``, or an arbitrary object
* ``stack_info`` - Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record
* ``levelno`` - Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
* ``relativeCreated`` - Time in milliseconds when the ``LogRecord`` was created, relative to the time the logging module was loaded


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
* ``{`` - curly brackets; compare to f-string formatting
* ``%`` - percent sign; compare to formatting string with ``%``
* ``$`` - dollar sign; compare to template vars from other languages
* Default mode is ``%`` percent

``%`` - percent sign (default):

>>> logging.basicConfig(
...     format='%(asctime)s %(levelname)s %(message)s',
...     style='%')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

``{`` - curly brackets:

>>> logging.basicConfig(
...     format='{asctime} {levelname} {message}',
...     style='{')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

``$`` - dollar sign:

>>> logging.basicConfig(
...     format='$asctime $levelname $message',
...     style='$')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


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
...     filename='/tmp/myfile.csv')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

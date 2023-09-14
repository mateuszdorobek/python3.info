Logging Levels
==============
* Critical - Error, cannot continue
* Error - Error, can continue
* Warning - Warning, will do something important
* Info - I will do something
* Debug - This is how I am doing this


Default Level
-------------
Default level is ``WARNING``, so all the information with level below will
not be displayed.

>>> import logging
>>>
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Change Level
------------
In logging you can set minimum level required. Setting it to ``DEBUG``
will show all the information above ``DEBUG`` level, which means everything.

>>> import logging
>>>
>>>
>>> logging.basicConfig(level='DEBUG')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

Setting it to ``ERROR`` will display only error and critical information.

>>> import logging
>>>
>>>
>>> logging.basicConfig(level='ERROR')
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')

You can also use ``logging.ERROR`` constant. Note, that similar constants
exists for other levels too.

>>> import logging
>>>
>>>
>>> logging.basicConfig(level=logging.ERROR)
>>>
>>> logging.critical('Error, cannot continue')
>>> logging.error('Error, can continue')
>>> logging.warning('Information, warn about something')
>>> logging.info('Information, inform about something')
>>> logging.debug('Debug, show detailed debugging information')


Error vs Critical
-----------------
* Critical - not working, and cannot continue (fatal)
* Error - not working, but can continue (it is not fatal)

For example, if we have files:

>>> TEMPERATURE_DATA_FILES = [
...     '2000-01-01.csv',
...     '2000-01-02.csv',
...     '2000-01-03.csv',
...     '2000-01-04.csv',
...     '2000-01-05.csv',  # corrupted
...     '2000-01-06.csv',
...     '2000-01-07.csv',
...     # ...
...     '2000-01-30.csv',
...     '2000-01-31.csv',
... ]

>>> def mean_temperature_for_jan05():
...     logging.critical('File "2000-01-05.csv" is corrupted')

>>> def mean_temperature_for_month():
...     logging.error('File "2000-01-05.csv" is corrupted')


Use Case - 0x01
---------------
>>> import logging
>>> import sys
>>>
>>>
>>> match sys.argv[1]:
...     case '--error': logging.basicConfig(level='ERROR')
...     case '--warning': logging.basicConfig(level='WARNING')
...     case '--info': logging.basicConfig(level='INFO')
...     case '--debug': logging.basicConfig(level='DEBUG')
...     case _: logging.basicConfig(level='ERROR')
>>>
>>>
>>> logging.critical('Example message')
>>> logging.error('Example message')
>>> logging.warning('Example message')
>>> logging.info('Example message')
>>> logging.debug('Example message')

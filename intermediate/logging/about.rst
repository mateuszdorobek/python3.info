Logging About
=============
* Do not print
* Always use logger
* Logs can be displayed on console
* Logs can be redirected to file
* Logs can be redirected to database
* Logs can be silenced (certain level)
* Logs can be rotated
* Logs can change format

>>> import logging
>>>
>>>
>>> def run():
...     logging.warning('Program start')
...     for number in range(0,3):
...         logging.info(f'Current number: {number}')
...     logging.warning('Program end')
>>>
>>>
>>> run()  # doctest: +SKIP
WARNING:root:Program start
WARNING:root:Program end


Further Reading
---------------
* https://pyvideo.org/pycon-au-2018/a-guided-tour-of-python-logging.html
* https://docs.python.org/3/howto/logging.html
* https://docs.python.org/3/library/logging.html#module-logging
* https://docs.python.org/3/library/logging.config.html#module-logging.config
* https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

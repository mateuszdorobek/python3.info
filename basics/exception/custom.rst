Exception Define
================


Define Custom Exceptions
------------------------
* Class which inherits from ``Exception``
* Exceptions should have ``Error`` at the end of their names

>>> class MyError(Exception):
...     pass
>>>
>>>
>>> raise MyError
Traceback (most recent call last):
MyError
>>>
>>> raise MyError('More verbose description')
Traceback (most recent call last):
MyError: More verbose description


Example
-------
>>> class AstronautsOnlyError(Exception):
...     pass
>>>
>>>
>>> profession = 'pilot'
>>>
>>> if profession != 'astronaut':
...     raise AstronautsOnlyError
Traceback (most recent call last):
AstronautsOnlyError


Use Case - 0x01
---------------
Django Framework Use-case of Custom Exceptions:

>>> # doctest: +SKIP
... from django.contrib.auth.models import User
>>>
>>>
>>> def login(request):
...     username = request.POST.get('username')
...     password = request.POST.get('password')
...
...     try:
...         user = User.objects.get(username, password)
...     except User.DoesNotExist:
...         print('Sorry, no such user in database')


Use Case - 0x02
---------------
* Dragon

>>> class Dragon:
...     def take_damage(self, damage):
...         raise self.IsDead
...
...     class IsDead(Exception):
...         pass
>>>
>>>
>>> wawelski = Dragon()
>>>
>>> try:
...     wawelski.take_damage(10)
... except Dragon.IsDead:
...     print('Dragon is dead')
Dragon is dead


Use Case - 0x03
---------------
>>> from datetime import datetime
>>> from uuid import uuid1
>>> import logging
>>>
>>>
>>> logging.basicConfig(
...     level='WARNING',
...     datefmt='%Y-%m-%d %H:%M:%S',
...     format='[{levelname}] {message}',
...     style='{'
... )
>>>
>>>
>>> class MyError(Exception):
...     def __init__(self, *args, **kwargs):
...         self.name = self.__class__.__name__
...         self.reason = self.args[0]
...
...         # make a UUID based on the host ID and current time
...         self.uuid = str(uuid1())
...
...         # save when exception occurred
...         self.when = datetime.now()
...
...         # run normal processing of the exception
...         super().__init__(*args, **kwargs)
>>>
>>>
>>> def run():
...     raise MyError('Error, because it is not working')
>>>
>>>
>>> try:
...     run()
... except Exception as error:
...     name = self.name
...     reason = self.reason
...     when = error.when.strftime('%Y-%m-%d %H:%M:%S')
...     identifier = error.uuid
...
...     # you can write this error to the database
...     # or print it on the stderr
...     logging.error(f'Error happened: {name=}, {reason=}, {when=}, {identifier=}')  # doctest: +SKIP
[ERROR] Error happened: name='MyError', reason='Error, because it is not working', when='1969-07-21 02:56:15', identifier='886a59c4-8431-11ec-95bc-acde48001122'


Assignments
-----------
.. literalinclude:: assignments/exception_custom_a.py
    :caption: :download:`Solution <assignments/exception_custom_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_custom_b.py
    :caption: :download:`Solution <assignments/exception_custom_b.py>`
    :end-before: # Solution

String Normalization
====================
* Using str methods for cleaning user input
* 80% of machine learning and data science is cleaning data


Normalization
-------------
Comparing not normalized strings will yield invalid or at least
unexpected results:

>>> 'MacGyver' == 'Macgyver'
False

Normalize strings before comparing:

>>> 'MacGyver'.upper() == 'Macgyver'.upper()
True


Numbers
-------
When comparing age, height, temperature etc, the following numbers has
the same meaning. Therefore after converting to ``float()`` it will be
exactly the same.

>>> age = 42
>>> age = 42.0
>>> age = 42.00
>>> age = '42'
>>> age = '42.0'
>>> age = '42.00'

However, when those values indicates for example a version of a program to
find in text their meaning will be different. Version 21 and '21.00' will
be a completely different object, so it should not be treated exactly the
same.

>>> version = 42
>>> version = 42.0
>>> version = 42.00
>>> version = '42'
>>> version = '42.0'
>>> version = '42.00'


Addresses
---------
Address prefix (street, road, court, place, etc.):

>>> prefix = 'ul'
>>> prefix = 'ul.'
>>> prefix = 'Ul.'
>>> prefix = 'UL.'
>>> prefix = 'ulica'
>>> prefix = 'Ulica'
>>>
>>> prefix = 'os'
>>> prefix = 'os.'
>>> prefix = 'Os.'
>>> prefix = 'osiedle'
>>> prefix = 'oś'
>>> prefix = 'oś.'
>>> prefix = 'Oś.'
>>> prefix = 'ośedle'
>>>
>>> prefix = 'pl'
>>> prefix = 'pl.'
>>> prefix = 'Pl.'
>>> prefix = 'plac'
>>>
>>> prefix = 'al'
>>> prefix = 'al.'
>>> prefix = 'Al.'
>>> prefix = 'aleja'
>>> prefix = 'aleia'
>>> prefix = 'alei'
>>> prefix = 'aleii'
>>> prefix = 'aleji'

House and apartment number:

>>> address = 'Ćwiartki 3/4'
>>> address = 'Ćwiartki 3 / 4'
>>> address = 'Ćwiartki 3 m. 4'
>>> address = 'Ćwiartki 3 m 4'
>>> address = 'Brighton Beach 1st apt 2'
>>> address = 'Brighton Beach 1st apt. 2'
>>> address = 'Myśliwiecka 3/5/7'
>>>
>>> address = 'Górczewska 180f/8f'
>>> address = 'Górczewska 180f/8'
>>> address = 'Górczewska 180/8f'
>>>
>>> address = 'Jana Pawła II 1 m. 5'
>>> address = 'Powstańców 13d bud. A piętro II sala 3'


Phone Numbers:
--------------
Which one is mobile, and which is landline?

>>> phone = '+48 (12) 355 5678'
>>> phone = '+48 123 555 678'

Note, the numbers. They are completely the same. Your

>>> phone = '123 555 1337'
>>> phone = '1235551337'
>>> phone = '+11235551337'
>>> phone = '+1 12 3555 1337'
>>> phone = '+1 123 555 1337'
>>> phone = '+1 (123) 555 1337'
>>> phone = '+1 (123) 555-1337'
>>> phone = '+1 (123)-555-1337'
>>> phone = '+1 (123).555.1337'
>>>
>>> phone = '+1 800-python'
>>> phone = '+1 800-798466'
>>>
>>> phone = '+48 123555133,1'
>>> phone = '+48 123555133,1,,2'
>>> phone = '+48 123 555 133 wew. 7'


Date and Time
-------------
>>> date = '1961-04-12'
>>> date = '12.4.1961'
>>> date = '12.04.1961'
>>> date = '12-04-1961'
>>> date = '12/04/1961'
>>> date = '4/12/61'
>>> date = '4.12.1961'
>>> date = 'Apr 12, 1961'
>>> date = 'Apr 12th, 1961'

>>> time = '12:00:00'
>>> time = '12:00'
>>> time = '12:00 pm'

>>> duration = '04:30:00'
>>> duration = '4h 30m'
>>> duration = '4 hours 30 minutes'


Case Study
----------
The following code is an output from real customer relationship management
(CRM) system, that I wrote in 2000s for a swimming pool in Poznan, Poland.
The output is a result of a ``SELECT DISTINCT(address)`` result in SQL.

Note to english speaking users:

    * ``os.`` - stands for ``osiedle``, which means blocks of flats
    * ``ul.`` - stands for ``ulica``, which means street

Is this the same address?

>>> street = 'os. Jana III Sobieskiego'
>>> street = 'ul. Jana III Sobieskiego'
>>> street = 'ul Jana III Sobieskiego'
>>> street = 'ul.Jana III Sobieskiego'
>>> street = 'ulicaJana III Sobieskiego'
>>> street = 'Ul. Jana III Sobieskiego'
>>> street = 'UL. Jana III Sobieskiego'
>>> street = 'ulica Jana III Sobieskiego'
>>> street = 'Ulica. Jana III Sobieskiego'
>>> street = 'Jana Sobieskiego 3'
>>> street = 'Jana Sobieskiego 3ego'
>>> street = 'Jana III Sobieskiego'
>>> street = 'Jana Iii Sobieskiego'
>>> street = 'Jana IIi Sobieskiego'
>>> street = 'Jana lll Sobieskiego'  # three small letters 'L'

Yes, this is the same address. Despite having information about two
different geographical entities (osiedle and ulica), this is the same
address. Why? It is just a simple mistake from people who entered data.

``SELECT DISTINCT(address)`` won't show you the number of occurrences for
each result. What seems to be a high error rate at the first glance, in
further analysis happens to be a superbly few mistakes. How come? Number of
results for ``os. Jana III Sobieskiego`` was around 50 thousands. The other
results was one or two at most. So, few mistakes from 50k results. That's
really good result.

Why we had those errors? Browser autocomplete. User error while imputing
data. And simple shortcuts during conversation: ``Where do you live?``,
``at Sobieskiego``. There is only one place in Poznan, Poland with that
name, so it was precise during the conversation. But, receiving party put
that incorrectly to the database assuming that it was ``ulica`` which is
far more common then ``osiedle`` addresses.


Assignments
-----------
.. literalinclude:: assignments/type_strnormalization_a.py
    :caption: :download:`Solution <assignments/type_strnormalization_a.py>`
    :end-before: # Solution

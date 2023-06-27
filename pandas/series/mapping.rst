Series Mapping
==============
* Using str methods for cleaning user input
* 80% of machine learning and data science is cleaning data
* ``Series.apply`` - apply function to data, function can have args and kwargs
* ``Series.map`` - convert data from one to another using function or dict


Apply
-----
Apply a function along an axis of the DataFrame. Can be ufunc (a NumPy function
that applies to the entire Series) or a Python function that only works on
single values.

>>> # doctest: +SKIP
... def apply(self,
...           func: Any,
...           axis: Any = 0,
...           raw: Any = False,
...           result_type: Any = None,
...           args: Any = (),
...           **kwargs: Any,
... ) -> Any | Series | DataFrame

Objects passed to the function are Series objects whose index is either the
DataFrame's index (axis=0) or the DataFrame's columns (axis=1). By default
(result_type=None), the final return type is inferred from the return type
of the applied function. Otherwise, it depends on the result_type argument.

Functions that mutate the passed object can produce unexpected behavior
or errors and are not supported.

>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> s = pd.Series(
...     index = pd.date_range('2000-01-01', periods=4),
...     data = np.random.randn(4))
>>>
>>> s
2000-01-01    1.764052
2000-01-02    0.400157
2000-01-03    0.978738
2000-01-04    2.240893
Freq: D, dtype: float64
>>>
>>> s.apply(int)
2000-01-01    1
2000-01-02    0
2000-01-03    0
2000-01-04    2
Freq: D, dtype: int64
>>>
>>> s.apply(lambda x: round(x, 2))
2000-01-01    1.76
2000-01-02    0.40
2000-01-03    0.98
2000-01-04    2.24
Freq: D, dtype: float64
>>>
>>> s.apply(round, ndigits=2)
2000-01-01    1.76
2000-01-02    0.40
2000-01-03    0.98
2000-01-04    2.24
Freq: D, dtype: float64
>>>
>>> s.apply(round, args=(2,))
2000-01-01    1.76
2000-01-02    0.40
2000-01-03    0.98
2000-01-04    2.24
Freq: D, dtype: float64

``functools.partial(func, *args, **keywords)``:

>>> from functools import partial
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> s = pd.Series(
...     index = pd.date_range('2000-01-01', periods=4),
...     data = np.random.randn(4))
>>>
>>> s
2000-01-01    1.764052
2000-01-02    0.400157
2000-01-03    0.978738
2000-01-04    2.240893
Freq: D, dtype: float64
>>>
>>> round2 = partial(round, ndigits=2)
>>> square = partial(pow, exp=2)
>>> cube = partial(pow, exp=3)
>>>
>>> s.apply(round2)
2000-01-01    1.76
2000-01-02    0.40
2000-01-03    0.98
2000-01-04    2.24
Freq: D, dtype: float64
>>>
>>> s.apply(square)
2000-01-01    3.111881
2000-01-02    0.160126
2000-01-03    0.957928
2000-01-04    5.021602
Freq: D, dtype: float64
>>>
>>> s.apply(cube)
2000-01-01     5.489520
2000-01-02     0.064075
2000-01-03     0.937561
2000-01-04    11.252875
Freq: D, dtype: float64


Map
---
Map values of Series according to input correspondence.
Used for substituting each value in a Series with another value, that may be
derived from a function, a dict or a Series.

>>> # doctest: +SKIP
... def map(self,
...         arg: Callable | dict | Series,
...         na_action: Literal['ignore']  | None = None,
... ) -> Series

When arg is a dictionary, values in Series that are not in the dictionary
(as keys) are converted to NaN. However, if the dictionary is a dict subclass
that defines __missing__ (i.e. provides a method for default values), then
this default is used rather than NaN.

>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> s = pd.Series(
...     index = pd.date_range('2000-01-01', periods=4),
...     data = np.random.randn(4))
>>>
>>> s
2000-01-01    1.764052
2000-01-02    0.400157
2000-01-03    0.978738
2000-01-04    2.240893
Freq: D, dtype: float64
>>>
>>> s.map(int)
2000-01-01    1
2000-01-02    0
2000-01-03    0
2000-01-04    2
Freq: D, dtype: int64
>>>
>>> s.map(lambda x: round(x, 2))
2000-01-01    1.76
2000-01-02    0.40
2000-01-03    0.98
2000-01-04    2.24
Freq: D, dtype: float64

>>> import pandas as pd
>>>
>>>
>>> s = pd.Series(['Watney', 'Twardowski', pd.NA, 'Lewis'])
>>>
>>> s
0        Watney
1    Twardowski
2          <NA>
3         Lewis
dtype: object
>>>
>>> s.map({'Watney': 'Mark', 'Twardowski': 'Pan'})
0    Mark
1     Pan
2     NaN
3     NaN
dtype: object
>>>
>>> s.map('I am {}'.format)
0        I am Watney
1    I am Twardowski
2          I am <NA>
3         I am Lewis
dtype: object
>>>
>>> s.map('I am {}'.format, na_action='ignore')
0        I am Watney
1    I am Twardowski
2               <NA>
3         I am Lewis
dtype: object


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

>>> version = 21
>>> version = 21.0
>>> version = 21.00
>>> version = '21'
>>> version = '21.0'
>>> version = '21.00'


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


Use Case - 0x01
---------------
String cleaning:

>>> expected = 'Pana Twardowskiego III'
>>> text = 'UL. pana \tTWArdoWskIEGO 3'

Convert to common format:

>>> text = text.upper()

Remove unwanted whitespaces:

>>> text = text.replace('\t', '')

Remove unwanted special characters:

>>> text = text.replace('.', '')

Remove unwanted text:

>>> text = text.replace('UL', '')
>>> text = text.replace('3', 'III')

Formatting:

>>> text = text.title()
>>> text = text.replace('Iii', 'III')
>>> text = text.strip()

Check result:

>>> print('Matched:', text == expected)
Matched: True
>>>
>>> print(text)
Pana Twardowskiego III


Use Case - 0x02
---------------
Remove Polish diacritics:

>>> def pl_to_latin(text):
...     PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...           'ł': 'l', 'ń': 'n', 'ó': 'o',
...           'ś': 's', 'ż': 'z', 'ź': 'z'}
...     result = ''.join(PL.get(x,x) for x in text.lower())
...     return result.capitalize()
>>>
>>>
>>> s = pd.Series(['Poznań', 'Swarzędz', 'Kraków',
...                'Łódź', 'Gdańsk', 'Koło', 'Dęblin'])
>>>
>>> s
0      Poznań
1    Swarzędz
2      Kraków
3        Łódź
4      Gdańsk
5        Koło
6      Dęblin
dtype: object
>>>
>>> s.map(pl_to_latin)
0      Poznan
1    Swarzedz
2      Krakow
3        Lodz
4      Gdansk
5        Kolo
6      Deblin
dtype: object
>>>
>>> s.apply(pl_to_latin)
0      Poznan
1    Swarzedz
2      Krakow
3        Lodz
4      Gdansk
5        Kolo
6      Deblin
dtype: object


Assignments
-----------
.. literalinclude:: assignments/pandas_series_mapping_a.py
    :caption: :download:`Solution <assignments/pandas_series_mapping_a.py>`
    :end-before: # Solution

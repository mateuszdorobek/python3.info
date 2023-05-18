Method Chaining
===============


SetUp
-----
>>> import pandas as pd
>>> import numpy as np
>>>
>>>
>>> DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]


Inplace
-------
>>> s = pd.Series(DATA)
>>> s.fillna(0, inplace=True)
>>> s.drop([2,4,6], inplace=True)
>>> s.drop_duplicates(inplace=True)
>>> s.reset_index(drop=True, inplace=True)
>>> s
0    1.0
1    0.0
2    2.0
3    inf
dtype: float64


Endl
----
>>> s = pd.Series(DATA) \
...       .fillna(0) \
...       .drop([2,4,6]) \
...       .drop_duplicates() \
...       .reset_index(drop=True)
>>>
>>> s
0    1.0
1    0.0
2    2.0
3    inf
dtype: float64


Chain
-----
>>> s = (pd.Series(DATA)
...        .fillna(0)
...        .drop([2,4,6])
...        .drop_duplicates()
...        .reset_index(drop=True))
>>>
>>> s
0    1.0
1    0.0
2    2.0
3    inf
dtype: float64


Further Reading
---------------
* https://stackoverflow.com/a/59335777


Use Case - 0x01
---------------
>>> DATA = [
...     'ul.Mieszka II',
...     'UL. Zygmunta III WaZY',
...     '  bolesława chrobrego ',
...     'ul Jana III SobIESkiego',
...     '\tul. Jana trzeciego Sobieskiego',
...     'ulicaJana III Sobieskiego',
...     'UL. JA    NA 3 SOBIES  KIEGO',
...     'ULICA JANA III SOBIESKIEGO  ',
...     'ULICA. JANA III SOBIeskieGO',
...     ' Jana 3 Sobieskiego  ',
...     'Jana III Sobi  eskiego ',
... ]
>>>
>>>
>>> def clean(text):
...     text = text.strip()
...     text = text.upper()
...     text = text.replace('\t', '')
...     text = text.replace('\n', '')
...     text = text.replace('    ', '')
...     text = text.replace('   ', '')
...     text = text.replace('  ', '')
...     text = text.replace('.', '')
...     text = text.replace(',', '')
...     text = text.replace('\\', '')
...     text = text.replace('ULICA', '')
...     text = text.replace('UL', '')
...     text = text.replace('TRZECIEGO', 'III')
...     text = text.replace('3', 'III')
...     text = text.title()
...     text = text.replace('Iii', 'III')
...     text = text.replace('Ii', 'II')
...     return text.strip()
>>>
>>>
>>> s = pd.Series(DATA)
>>> s.apply(clean)
0               Mieszka II
1        Zygmunta III Wazy
2      Bolesława Chrobrego
3     Jana III Sobieskiego
4     Jana III Sobieskiego
5     Jana III Sobieskiego
6     Jana III Sobieskiego
7     Jana III Sobieskiego
8     Jana III Sobieskiego
9     Jana III Sobieskiego
10    Jana III Sobieskiego
dtype: object

>>> DATA = [
...     'ul.Mieszka II',
...     'UL. Zygmunta III WaZY',
...     '  bolesława chrobrego ',
...     'ul Jana III SobIESkiego',
...     '\tul. Jana trzeciego Sobieskiego',
...     'ulicaJana III Sobieskiego',
...     'UL. JA    NA 3 SOBIES  KIEGO',
...     'ULICA JANA III SOBIESKIEGO  ',
...     'ULICA. JANA III SOBIeskieGO',
...     ' Jana 3 Sobieskiego  ',
...     'Jana III Sobi  eskiego ',
... ]
>>>
>>> def clean(text):
...     return (text
...             .strip()
...             .upper()
...             .replace('\t', '')
...             .replace('\n', '')
...             .replace('    ', '')
...             .replace('   ', '')
...             .replace('  ', '')
...             .replace('.', '')
...             .replace(',', '')
...             .replace('\\', '')
...             .replace('ULICA', '')
...             .replace('UL', '')
...             .replace('TRZECIEGO', 'III')
...             .replace('3', 'III')
...             .title()
...             .replace('Iii', 'III')
...             .replace('Ii', 'II')
...             .strip())
>>>
>>>
>>> s = pd.Series(DATA)
>>> s.apply(clean)
0               Mieszka II
1        Zygmunta III Wazy
2      Bolesława Chrobrego
3     Jana III Sobieskiego
4     Jana III Sobieskiego
5     Jana III Sobieskiego
6     Jana III Sobieskiego
7     Jana III Sobieskiego
8     Jana III Sobieskiego
9     Jana III Sobieskiego
10    Jana III Sobieskiego
dtype: object


.. todo:: Assignments

Read String
===========
* File paths works also with URLs
* `io.StringIO` Converts ``str`` to File-like object


Example
-------
>>> from io import StringIO
>>> import pandas as pd
>>>
>>>
>>> DATA = """
... "Crew", "Role", "Astronaut"
... "Prime", "CDR", "Neil Armstrong"
... "Prime", "LMP", "Buzz Aldrin"
... "Prime", "CMP", "Michael Collins"
... "Backup", "CDR", "James Lovell"
... "Backup", "LMP", "William Anders"
... "Backup", "CMP", "Fred Haise"
... """
>>>
>>> data = StringIO(DATA)
>>> df = pd.read_csv(data)
>>>
>>> df
     Crew  "Role"         "Astronaut"
0   Prime   "CDR"    "Neil Armstrong"
1   Prime   "LMP"       "Buzz Aldrin"
2   Prime   "CMP"   "Michael Collins"
3  Backup   "CDR"      "James Lovell"
4  Backup   "LMP"    "William Anders"
5  Backup   "CMP"        "Fred Haise"

>>> from io import StringIO
>>> import pandas as pd
>>> import requests
>>>
>>>
>>> DATA = 'https://python3.info/_static/astro-order.csv'
>>>
>>> resp = requests.get(DATA)
>>> data = StringIO(resp.text)
>>> df = pd.read_csv(data)
>>>
>>> df.head(n=5)
   Order       Astronaut     Type              Date      Spacecraft
0    1.0    Yuri Gagarin  Orbital     12 April 1961          Vostok
1    2.0    Alan Shepard  Orbital        5 May 1961       Freedom 7
2    3.0  Virgil Grissom  Orbital      21 July 1961  Liberty Bell 7
3    4.0   Gherman Titov  Orbital     6 August 1961        Vostok 2
4    5.0      John Glenn  Orbital  20 February 1962    Friendship 7

Read Clipboard
==============
* ``pd.read_clipboard()``


Example
-------
.. code-block:: text

    Crew	Role	Astronaut
    Prime	CDR	Neil Armstrong
    Prime	LMP	Buzz Aldrin
    Prime	CMP	Michael Collins
    Backup	CDR	James Lovell
    Backup	LMP	William Anders
    Backup	CMP	Fred Haise

>>> # doctest: +SKIP
... import pandas as pd
...
... df = pd.read_clipboard()
...
... df
     Crew Role        Astronaut
0   Prime  CDR   Neil Armstrong
1   Prime  LMP      Buzz Aldrin
2   Prime  CMP  Michael Collins
3  Backup  CDR     James Lovell
4  Backup  LMP   William Anders
5  Backup  CMP       Fred Haise

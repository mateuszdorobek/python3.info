CSV About
=========
* CSV - Comma/Character Separated Values
* No CSV formal standard, just a good practice
* Flat file (2D) without relations
* Relations has to be flatten (serialization, additional columns, etc...)
* Typically first line (header) represents column names
* Rarely first line can also have a structure (nrows, ncols)
* Internationalization: encoding
* Localization: decimal separator, thousands separator, date format
* Parameters: delimiter, quotechar, quoting, lineterminator, dialect

Example CSV file:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor
    6.3, 2.9, 5.6, 1.8, virginica
    6.4, 3.2, 4.5, 1.5, versicolor
    4.7, 3.2, 1.3, 0.2, setosa
    7.0, 3.2, 4.7, 1.4, versicolor
    7.6, 3.0, 6.6, 2.1, virginica
    4.9, 3.0, 1.4, 0.2, setosa
    4.9, 2.5, 4.5, 1.7, virginica


Header
------
File without header:

.. code-block:: text

    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor
    6.3, 2.9, 5.6, 1.8, virginica
    6.4, 3.2, 4.5, 1.5, versicolor
    4.7, 3.2, 1.3, 0.2, setosa
    7.0, 3.2, 4.7, 1.4, versicolor
    7.6, 3.0, 6.6, 2.1, virginica
    4.9, 3.0, 1.4, 0.2, setosa
    4.9, 2.5, 4.5, 1.7, virginica

First line is a header:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor
    6.3, 2.9, 5.6, 1.8, virginica
    6.4, 3.2, 4.5, 1.5, versicolor
    4.7, 3.2, 1.3, 0.2, setosa
    7.0, 3.2, 4.7, 1.4, versicolor
    7.6, 3.0, 6.6, 2.1, virginica
    4.9, 3.0, 1.4, 0.2, setosa
    4.9, 2.5, 4.5, 1.7, virginica

First line is a structure: number of rows (nrows) and columns (ncols):

.. code-block:: text

    10, 5
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor
    6.3, 2.9, 5.6, 1.8, virginica
    6.4, 3.2, 4.5, 1.5, versicolor
    4.7, 3.2, 1.3, 0.2, setosa
    7.0, 3.2, 4.7, 1.4, versicolor
    7.6, 3.0, 6.6, 2.1, virginica
    4.9, 3.0, 1.4, 0.2, setosa
    4.9, 2.5, 4.5, 1.7, virginica

First line is a structure: number of rows (nrows) and features (nfeatures),
followed  by label_encoder values for label column:

.. code-block:: text

    10, 4, virginica, setosa, versicolor
    5.8, 2.7, 5.1, 1.9, 0
    5.1, 3.5, 1.4, 0.2, 1
    5.7, 2.8, 4.1, 1.3, 2
    6.3, 2.9, 5.6, 1.8, 0
    6.4, 3.2, 4.5, 1.5, 2
    4.7, 3.2, 1.3, 0.2, 1
    7.0, 3.2, 4.7, 1.4, 2
    7.6, 3.0, 6.6, 2.1, 0
    4.9, 3.0, 1.4, 0.2, 1
    4.9, 2.5, 4.5, 1.7, 0


Delimiter
---------
* ``csv`` module expects delimeter to be 1-character in length

``delimiter=', '``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``delimiter=','``:

.. code-block:: text

    SepalLength,SepalWidth,PetalLength,PetalWidth,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

``delimiter=';'``:

.. code-block:: text

    SepalLength;SepalWidth;PetalLength;PetalWidth;Species
    5.8;2.7;5.1;1.9;virginica
    5.1;3.5;1.4;0.2;setosa
    5.7;2.8;4.1;1.3;versicolor

``delimiter=':'``:

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
    martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash

``delimiter='|'``:

.. code-block:: text

    | Firstname | Lastname | Role      |
    |-----------|----------|-----------|
    | Mark      | Watney   | Botanist  |
    | Melissa   | Lewis    | Commander |
    | Rick      | Martinez | Pilot     |

``delimiter='\t'``:

.. code-block:: text

    SepalLength	SepalWidth	PetalLength	PetalWidth	Species
    5.8	2.7	5.1	1.9	virginica
    5.1	3.5	1.4	0.2	setosa
    5.7	2.8	4.1	1.3	versicolor


Quotechar
---------
* ``"`` - quote char (best)
* ``'`` - apostrophe

``quotechar='"'``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"

``quotechar="'"``:

.. code-block:: text

    'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'
    '5.8', '2.7', '5.1', '1.9', 'virginica'
    '5.1', '3.5', '1.4', '0.2', 'setosa'
    '5.7', '2.8', '4.1', '1.3', 'versicolor'

``quotechar='|'``:

.. code-block:: text

    |SepalLength|, |SepalWidth|, |PetalLength|, |PetalWidth|, |Species|
    |5.8|, |2.7|, |5.1|, |1.9|, |virginica|
    |5.1|, |3.5|, |1.4|, |0.2|, |setosa|
    |5.7|, |2.8|, |4.1|, |1.3|, |versicolor|

``quotechar='/'``:

.. code-block:: text

    /SepalLength/, /SepalWidth/, /PetalLength/, /PetalWidth/, /Species/
    /5.8/, /2.7/, /5.1/, /1.9/, /virginica/
    /5.1/, /3.5/, /1.4/, /0.2/, /setosa/
    /5.7/, /2.8/, /4.1/, /1.3/, /versicolor/


Quoting
-------
* ``csv.QUOTE_ALL`` (safest)
* ``csv.QUOTE_MINIMAL``
* ``csv.QUOTE_NONE``
* ``csv.QUOTE_NONNUMERIC``

``quoting=csv.QUOTE_ALL``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"

``quoting=csv.QUOTE_MINIMAL``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``quoting=csv.QUOTE_NONE``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``quoting=csv.QUOTE_NONNUMERIC``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    5.8, 2.7, 5.1, 1.9, "virginica"
    5.1, 3.5, 1.4, 0.2, "setosa"
    5.7, 2.8, 4.1, 1.3, "versicolor"


Lineterminator
--------------
* ``\r\n`` - New line on Windows
* ``\n`` - New line on ``*nix``
* ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)


Decimal Separator
-----------------
* ``0.1`` - Decimal point
* ``0,1`` - Decimal comma

.. figure:: img/l10n-decimal-separator.png

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8; 2.7; 5.1; 1.9; virginica
    5.1; 3.5; 1.4; 0.2; setosa
    5.7; 2.8; 4.1; 1.3; versicolor

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5,8; 2,7; 5,1; 1,9; virginica
    5,1; 3,5; 1,4; 0,2; setosa
    5,7; 2,8; 4,1; 1,3; versicolor


Thousands Separator
-------------------
* ``1000000`` - None
* ``1'000'000`` - Apostrophe
* ``1 000 000`` - Space, the internationally recommended thousands separator
* ``1.000.000`` - Period, used in many non-English speaking countries
* ``1,000,000`` - Comma, used in most English-speaking countries


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


Encoding
--------
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Central European encoding on Windows
* ``cp1251`` or ``windows-1251`` - Eastern European encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. code-block:: python

    with open(FILE, encoding='utf-8') as file:
        ...


Dialects
--------
.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* Microsoft Excel 2016-2020:

    * ``quoting=csv.QUOTE_MINIMAL``
    * ``quotechar='"'``
    * ``delimiter=','`` or ``delimiter=';'`` depending on Windows locale decimal separator
    * ``lineterminator='\r\n'``
    * ``encoding='...'`` - depends on Windows locale typically ``windows-*``

* Microsoft Excel macOS:

    * ``quoting=csv.QUOTE_MINIMAL``
    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\r\n'``
    * ``encoding='utf-8'``

* Microsoft export options:

.. figure:: img/csv-standard-dialects.png

.. code-block:: console

    $ file utf8.csv
    utf8.csv: CSV text

    $ cat utf8.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,zażółć gęślą jaźń
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file standard.csv
    standard.csv: CSV text

    $ cat standard.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,za_?__ g__l_ ja__
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file dos.csv
    dos.csv: CSV text

    $ cat dos.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,za_?__ g__l_ ja__
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file macintosh.csv
    macintosh.csv: Non-ISO extended-ASCII text, with CR line terminators

    $ cat macintosh.csv
    ,,"21,5",Some; Comment


Good Practices
--------------
Always specify:

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)


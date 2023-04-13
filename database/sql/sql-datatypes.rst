SQL Data Types
==============
* Python ``None``  -> SQLite3 ``NULL``
* Python ``int``   -> SQLite3 ``INTEGER``
* Python ``float`` -> SQLite3 ``REAL``
* Python ``str``   -> SQLite3 ``TEXT``
* Python ``bytes`` -> SQLite3 ``BLOB``

.. csv-table:: Data Types: Python vs SQLite3
    :header:  "Python Type", "SQLite Type"

    ``None``,   ``NULL``
    ``int``,    ``INTEGER``
    ``float``,  ``REAL``
    ``str``,    ``TEXT``
    ``bytes``,  ``BLOB``


NULL Type
---------
* The value is a undefined value


INTEGER Type
------------
* The value is a signed integer
* Stored in 1, 2, 3, 4, 6, or 8 bytes
* Depending on the magnitude of the value

Aliases:

    * ``INT``
    * ``INTEGER``
    * ``TINYINT``
    * ``SMALLINT``
    * ``MEDIUMINT``
    * ``BIGINT``
    * ``UNSIGNED BIG INT``
    * ``INT2``
    * ``INT8``


REAL Type
---------
* The value is a floating point value
* Stored as an 8-byte IEEE floating point number

Aliases:

    * ``REAL``
    * ``DOUBLE``
    * ``DOUBLE PRECISION``
    * ``FLOAT``


TEXT Type
---------
* The value is a text string
* Stored using the database encoding (ie. UTF-8)

Aliases:

    * ``CHARACTER(20)``
    * ``VARCHAR(255)``
    * ``VARYING CHARACTER(255)``
    * ``NCHAR(55)``
    * ``NATIVE CHARACTER(70)``
    * ``NVARCHAR(100)``
    * ``TEXT``
    * ``CLOB``


BLOB Type
---------
* Binary Large Object
* The value is a blob of data
* Stored exactly as it was input


NUMERIC Affinity
----------------
* May contain values using all five storage classes

When text data is inserted into a ``NUMERIC`` column, the storage class
of the text is converted to ``INTEGER`` or ``REAL`` (in order of preference)
if the text is a well-formed integer or real literal, respectively.

If the ``TEXT`` value is a well-formed integer literal that is too large
to fit in a 64-bit signed integer, it is converted to ``REAL``.

Aliases:

    * ``NUMERIC``
    * ``DECIMAL(10,5)``
    * ``BOOLEAN``
    * ``DATE``
    * ``DATETIME``


DATETIME Affinity
-----------------
SQLite does not have a storage class set aside for storing dates and/or
times. Instead, the built-in date and time functions of SQLite are capable
of storing dates and times as ``TEXT``, ``REAL``, or ``INTEGER`` values.

* ``TEXT`` as ISO8601 strings ('YYYY-MM-DD HH:MM:SS.SSS').
* ``REAL`` as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the Gregorian calendar.
* ``INTEGER`` as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

Applications can chose to store dates and times in any of these formats
and freely convert between formats using the built-in date and time
functions.

SQLite3 Adapter/Converter
=========================
* https://docs.python.org/3.12/library/sqlite3.html#sqlite3-adapter-converter-recipes

The default adapters and converters are deprecated as of Python 3.12.
Instead, use the Adapter and converter recipes and tailor them to your needs.

The deprecated default adapters and converters consist of:

* An adapter for datetime.date objects to strings in ISO 8601 format.
* An adapter for datetime.datetime objects to strings in ISO 8601 format.
* A converter for declared "date" types to datetime.date objects.
* A converter for declared "timestamp" types to datetime.datetime objects. Fractional parts will be truncated to 6 digits (microsecond precision).

The default "timestamp" converter ignores UTC offsets in the database
and always returns a naive datetime.datetime object. To preserve UTC
offsets in timestamps, either leave converters disabled, or register
an offset-aware converter with register_converter().


SetUp
-----
>>> import datetime
>>> import sqlite3


Adapter
-------
>>> def adapt_date_iso(val):
...     """Adapt datetime.date to ISO 8601 date."""
...     return val.isoformat()
>>>
>>> def adapt_datetime_iso(val):
...     """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
...     return val.isoformat()
>>>
>>> def adapt_datetime_epoch(val):
...     """Adapt datetime.datetime to Unix timestamp."""
...     return int(val.timestamp())
>>>
>>>
>>> sqlite3.register_adapter(datetime.date, adapt_date_iso)
>>> sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
>>> sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)


Converter
---------
>>> def convert_date(val):
...     """Convert ISO 8601 date to datetime.date object."""
...     return datetime.date.fromisoformat(val)
>>>
>>> def convert_datetime(val):
...     """Convert ISO 8601 datetime to datetime.datetime object."""
...     return datetime.datetime.fromisoformat(val)
>>>
>>> def convert_timestamp(val):
...     """Convert Unix epoch timestamp to datetime.datetime object."""
...     return datetime.datetime.fromtimestamp(val)
>>>
>>>
>>> sqlite3.register_converter('date', convert_date)
>>> sqlite3.register_converter('datetime', convert_datetime)
>>> sqlite3.register_converter('timestamp', convert_timestamp)

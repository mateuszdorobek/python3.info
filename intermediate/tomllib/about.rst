TOML
====


SetUp
-----
>>> import tomllib


From String
-----------
>>> toml_str = """
... python-version = "3.11.3"
... python-implementation = "CPython"
... """
>>>
>>> data = tomllib.loads(toml_str)
>>> data
{'python-version': '3.11.3', 'python-implementation': 'CPython'}


From File
---------
>>> with open('pyproject.toml', 'rb') as f:  # doctest: +SKIP
...     data = tomllib.load(f)


Conversion Table
----------------

+------------------+--------------------------------------------------------------------------------------+
| TOML             | Python                                                                               |
+==================+======================================================================================+
| table            | dict                                                                                 |
+------------------+--------------------------------------------------------------------------------------+
| string           | str                                                                                  |
+------------------+--------------------------------------------------------------------------------------+
| integer          | int                                                                                  |
+------------------+--------------------------------------------------------------------------------------+
| float            | float (configurable with *parse_float*)                                              |
+------------------+--------------------------------------------------------------------------------------+
| boolean          | bool                                                                                 |
+------------------+--------------------------------------------------------------------------------------+
| offset date-time | datetime.datetime (``tzinfo`` attribute set to an instance of ``datetime.timezone``) |
+------------------+--------------------------------------------------------------------------------------+
| local date-time  | datetime.datetime (``tzinfo`` attribute set to ``None``)                             |
+------------------+--------------------------------------------------------------------------------------+
| local date       | datetime.date                                                                        |
+------------------+--------------------------------------------------------------------------------------+
| local time       | datetime.time                                                                        |
+------------------+--------------------------------------------------------------------------------------+
| array            | list                                                                                 |
+------------------+--------------------------------------------------------------------------------------+


Example
-------
.. code-block:: toml

    [project]
    name = "myproject"
    version = "1.0.0"
    requires-python = ">=3.11"
    authors = [{name = "Mark Watney", email = "mwatney@nasa.gov"}]
    readme = "README.md"
    license = {file = "LICENSE"}
    keywords = ["ares", "mars", "nasa", "human-spaceflight"]
    dependencies = [
        "django == 4.2.*",
        "django-ninja == 0.19.*"]

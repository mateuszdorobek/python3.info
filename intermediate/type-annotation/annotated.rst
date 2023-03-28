Annotated
=========
* Since Python 3.9 :pep:`593` -- Flexible function and variable annotations
* https://docs.python.org/3/library/typing.html#typing.Annotated
* https://github.com/annotated-types/annotated-types
* https://github.com/tiangolo/fastapi/releases/tag/0.95.0

.. note:: ``ValueRange``, ``ctype``, ``MatchesRegex``, ``MaxLen``
          does not exist in Python. It is used only as an example
          both here and in :pep:`593`.


SetUp
-----
>>> from typing import Annotated


Numeric
-------
>>> digit = Annotated[int, ValueRange(0,9)]  # doctest: +SKIP
>>> int8 = Annotated[int, ValueRange(-128, 127), ctype('int8')]  # doctest: +SKIP
>>> uint8 = Annotated[int, ValueRange(0, 255), ctype('uint8')]    # doctest: +SKIP
>>> kelvin = Annotated[float, ValueRange(0.0, float('inf'))]  # doctest: +SKIP
>>> vector = Annotated[list[int], MaxLen(3)]  # doctest: +SKIP


Character
---------
>>> firstname = Annotated[str, MaxLen(10)]  # doctest: +SKIP
>>> lastname = Annotated[str, MinLen(2), MaxLen(10)]  # doctest: +SKIP


Patterns
--------
>>> jira_issuekey = Annotated[str, MatchesRegex('^[A-Z]{2,10}-[0-9]{1,6}$')]  # doctest: +SKIP
>>> email = Annotated[str, MatchesRegex('^[a-z]{1,20}@nasa.gov$')]  # doctest: +SKIP


Use Case - 0x01
---------------
>>> # doctest: +SKIP
... EmailAddress = Annotated[str, MatchesRegex('^[a-z]{1,20}@nasa.gov$')]
...
... def send_email(recipient: EmailAddress):
...     ...
...
...
... send_email('mwatney@nasa.gov')  # ok
... send_email('avogel@esa.int')    # error


Use Case - 0x02
---------------
>>> # doctest: +SKIP
... IssueKey = Annotated[str, MatchesRegex('^[A-Z]{2,10}-[0-9]{1,6}$')]
...
... def comment(issuekey: IssueKey, text: str):
...     ...
...
...
... comment('MYPROJ-1337', 'Issue was resolved successfully.')

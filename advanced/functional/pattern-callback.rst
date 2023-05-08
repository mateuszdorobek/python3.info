Functional Pattern Callback
===========================
* Callback Design Pattern


Example
-------
>>> from urllib.request import urlopen
>>>
>>>
>>> def fetch(url: str,
...           on_success = lambda response: ...,
...           on_error = lambda error: ...,
...           ) -> None:
...     try:
...         result = urlopen(url).read().decode('utf-8')
...     except Exception as error:
...         on_error(error)
...     else:
...         on_success(result)

>>> fetch(
...     url = 'https://python3.info',
...     on_success = lambda resp: print(resp),
...     on_error = lambda err: print(err),
... )  # doctest: +SKIP

>>> def ok(response: str):
...     print(response)
>>>
>>> def err(error: Exception):
...     print(error)
>>>
>>>
>>> fetch(url='https://python3.info')  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_success=ok)  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_error=err)  # doctest: +SKIP
>>> fetch(url='https://python3.info', on_success=ok, on_error=err)  # doctest: +SKIP
>>> fetch(url='https://python3.info/not-existing', on_error=err)  # doctest: +SKIP

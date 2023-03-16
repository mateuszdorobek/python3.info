Callback
========
* EN: Callback Design
* PL:


Solution
--------
>>> from http import HTTPStatus
>>> import requests
>>>
>>>
>>> def noop(*arg, **kwargs):
...     pass
>>>
>>>
>>> def http_request(url, on_success=noop, on_error=noop):
...     result = requests.get(url)
...     if result.status_code == HTTPStatus.OK:
...         on_success(result)
...     else:
...         on_error(result)
>>>
>>>
>>> def success(result):
...     print('Success')
>>>
>>>
>>> def error(result):
...     print('Error')
>>>
>>>
>>> # doctest: +SKIP
... http_request(
...     url='https://python.astrotech.io',
...     on_success=success,
...     on_error=error,
... )


Object
------
>>> import requests
>>> from http import HTTPStatus
>>>
>>>
>>> def http(obj):
...     response = requests.request(
...         method=obj.method,
...         data=obj.data,
...         path=obj.path)
...
...     if response == HTTPStatus.OK:
...         return obj.on_success(response)
...     else:
...         return obj.on_error(response)
>>>
>>>
>>> class Request:
...     method = 'GET'
...     path = '/index'
...     data = None
...
...     def on_success(self, response):
...         print('Success!')
...
...     def on_error(self, response):
...         print('Error')
>>>
>>> http(Request())  # doctest: +SKIP

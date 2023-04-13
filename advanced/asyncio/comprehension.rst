AsyncIO Comprehensions
======================
* Asynchronous Comprehensions https://peps.python.org/pep-0530/


Recap
-----
>>> # doctest: +SKIP
... result = []
... async for i in aiter():
...     if i % 2:
...         result.append(i)


Example
-------
>>> result = [i async for i in aiter() if i % 2]  # doctest: +SKIP

>>> result = [await fun() for fun in funcs]  # doctest: +SKIP
>>> result = {await fun() for fun in funcs}  # doctest: +SKIP
>>> result = {fun: await fun() for fun in funcs}  # doctest: +SKIP

>>> result = [await fun() for fun in funcs if await smth]  # doctest: +SKIP
>>> result = {await fun() for fun in funcs if await smth}  # doctest: +SKIP
>>> result = {fun: await fun() for fun in funcs if await smth}  # doctest: +SKIP

>>> result = [await fun() async for fun in funcs]  # doctest: +SKIP
>>> result = {await fun() async for fun in funcs}  # doctest: +SKIP
>>> result = {fun: await fun() async for fun in funcs}  # doctest: +SKIP

>>> result = [await fun() async for fun in funcs if await smth]  # doctest: +SKIP
>>> result = {await fun() async for fun in funcs if await smth}  # doctest: +SKIP
>>> result = {fun: await fun() async for fun in funcs if await smth}  # doctest: +SKIP

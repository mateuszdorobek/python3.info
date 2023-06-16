Functional Pattern Callback
===========================
* Callback Design Pattern

In Python, a callback pattern is a design pattern where a function is passed
as an argument to another function, and the second function calls the first
function at a later time. The first function is called a callback function,
and it is executed when a certain event occurs or when a certain condition
is met.

The callback pattern is often used in event-driven programming, where a
program waits for events to occur and then responds to them. For example, in
a graphical user interface (GUI) application, a button click event might
trigger a callback function that updates the display or performs some other
action.

Here's an example of using a callback pattern in Python:

>>> def my_function(callback):
...     print('Doing some work...')
...     result = 10 + 20
...     callback(result)
>>>
>>> def my_callback(result):
...     print(f'The result is: {result}')
>>>
>>> my_function(my_callback)
Doing some work...
The result is: 30

In this example, the ``my_function()`` function takes a callback function as
its argument. It does some work (in this case, adding two numbers) and then
calls the callback function, passing the result as an argument.

The ``my_callback()`` function is defined separately and takes the result as
its argument. It simply prints the result to the console.

When the ``my_function()`` function is called with the ``my_callback()``
function as its argument, the callback function is executed with the result
of the original function.

Using the callback pattern allows for more flexible and modular code, as
different functions can be used as callbacks depending on the situation. It
also allows for asynchronous programming, where a program can continue to
run while waiting for a callback to be executed.


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

Generator Send
==============
* ``.send()`` method allows to pass value to the generator
* ``data = yield`` will receive this "sent" value


Example
-------
* After running you have to send ``None`` value to begin processing

>>> def run():
...     print('Starting worker...')
...     while True:
...         work = yield
...         print(f'Processing {work}')
>>>
>>>
>>> worker = run()
>>> worker.send(None)
Starting worker...
>>>
>>> worker.send('job1')
Processing job1
>>>
>>> worker.send('job2')
Processing job2
>>>
>>> worker.send('job3')
Processing job3

>>> from inspect import isgenerator, isgeneratorfunction
>>>
>>>
>>> def run():
...     print('Starting worker...')
...     while True:
...         work = yield
...         print(f'Processing {work}')
>>>
>>> worker = run()
>>> worker.send(None)
Starting worker...
>>>
>>> worker.send(1)
Processing 1
>>>
>>> worker.send('hello')
Processing hello
>>>
>>> worker.send([1,2,3])
Processing [1, 2, 3]
>>>
>>> isgeneratorfunction(run)
True
>>> isgenerator(worker)
True


Why Send None?!
---------------
* After running you have to send ``None`` value to begin processing
* Sending anything other will raise ``TypeError``

>>> def run():
...     print('Starting worker...')
...     while True:
...         work = yield
...         print(f'Processing {work}')
>>>
>>>
>>> worker = run()
>>>
>>> type(worker)
<class 'generator'>
>>>
>>> worker.send('hello')
Traceback (most recent call last):
TypeError: can't send non-None value to a just-started generator


Send Upstream Cascade
---------------------
>>> def worker():
...     print('Starting worker...')
...     while True:
...         work = yield
...         print(f'Processing {work}')
>>>
>>> def run(gen):
...     gen.send(None)
...     while True:
...         x = yield
...         gen.send(x)
>>>
>>>
>>> result = run(worker())
>>> result.send(None)
Starting worker...
>>>
>>> for x in range(0,3):
...     result.send(x)
Processing 0
Processing 1
Processing 2

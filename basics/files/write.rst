File Write
==========
* Creates file if not exists
* Truncate the file before writing
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* ``mode`` parameter to ``open()`` function is required

>>> file = open(r'/tmp/myfile.txt', mode='w')
>>> file.write('hello')
5
>>> file.close()


Line
----
* File must end with a newline ``\n`` character
* POSIX Definition: A sequence of zero or more non-<newline> characters plus a terminating <newline> character.

Line Definition by POSIX [#POSIX]_:

    A sequence of zero or more non-<newline> characters plus a terminating
    <newline> character.

Line definition by ANSI C89 and ISO C99 standards [#C89]_, [#C99]_, [#GCC]_:

    A source file that is not empty shall end in a new-line character, which
    shall not be immediately preceded by a backslash character.


Write to File
-------------
* Always remember to close file

>>> FILE = r'/tmp/myfile.txt'
>>> DATA = 'We choose to go to the Moon...'
>>>
>>> file = open(FILE, mode='w')
>>> file.write(DATA)
30
>>> file.close()


Write One Line
--------------
>>> FILE = r'/tmp/myfile.txt'
>>> DATA = 'We choose to go to the Moon...'
>>>
>>> with open(FILE, mode='w') as file:
...     file.write(DATA)
30


Write Multiple Lines
--------------------
* Write a list of lines to the file.
* ``.writelines()`` does not add a line separator (``\n``)!!
*  Each line must add a separator at the end.

>>> FILE = r'/tmp/myfile.txt'
>>> DATA = [
...     'We choose to go to the Moon.',
...     'We choose to go to the Moon in this decade and do the other things.',
...     'Not because they are easy, but because they are hard.',
... ]
>>>
>>> result = '\n'.join(DATA)
>>>
>>> with open(FILE, mode='w') as file:
...     file.write(result)
150

>>> FILE = r'/tmp/myfile.txt'
>>> DATA = [
...     'We choose to go to the Moon.',
...     'We choose to go to the Moon in this decade and do the other things.',
...     'Not because they are easy, but because they are hard.',
... ]
>>>
>>> result = [line+'\n' for line in DATA]
>>>
>>> with open(FILE, mode='w') as file:
...     file.writelines(result)


Write Non-Str Data
------------------
* Join works only for strings
* Conversion to ``str`` must be performed before adding a separator and
  writing to file.

>>> FILE = r'/tmp/myfile.txt'
>>> DATA = [1, 2, 3]
>>>
>>> result = ','.join(str(x) for x in DATA) + '\n'
>>>
>>> with open(FILE, mode='w') as file:
...     file.write(result)
6

When writing output to the stream, if newline is ``None``, any ``'\n'``
characters written are translated to the system default line separator,
``os.linesep``. If newline is ``''`` or ``'\n'``, no translation takes place.
If newline is any of the other legal values, any ``'\n'`` characters written
are translated to the given string. [#pydocIO]_


Reading From One File and Writing to Another
--------------------------------------------
>>> FILE_READ = r'/tmp/my-infile.txt'
>>> FILE_WRITE = r'/tmp/my-outfile.txt'
>>>
>>> # doctest: +SKIP
... with open(FILE_READ) as infile, \
...     open(FILE_WRITE, mode='w') as outfile:
...
...     for line in infile:
...         outfile.write(line)


References
----------
.. [#POSIX] Section 3.206 IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008). Open Group Base Specifications Issue 7. Year: 2018. Retrieved: 2020-12-17. URL: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206
.. [#C89] Section 2.1.1.2 of the ANSI C 1989 standard
.. [#C99] Section 5.1.1.2 of the ISO C 1999 standard
.. [#GCC] https://gcc.gnu.org/legacy-ml/gcc/2003-11/msg01568.html
.. [#pydocIO] https://docs.python.org/3/library/io.html#io.TextIOWrapper


Assignments
-----------
.. literalinclude:: assignments/file_write_a.py
    :caption: :download:`Solution <assignments/file_write_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_b.py
    :caption: :download:`Solution <assignments/file_write_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_c.py
    :caption: :download:`Solution <assignments/file_write_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_d.py
    :caption: :download:`Solution <assignments/file_write_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_e.py
    :caption: :download:`Solution <assignments/file_write_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_f.py
    :caption: :download:`Solution <assignments/file_write_f.py>`
    :end-before: # Solution

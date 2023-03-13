"""
* Assignment: Protocol ContextManager Buffer
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Define class attribute `BUFFER_LIMIT: int = 100` bytes
    2. File has to be written to disk every X bytes of buffer
    3. Writing and reading takes time,
       how to make buffer save data in the background,
       but it could be still used?
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasowy atrybut `BUFFER_LIMIT: int = 100` bajtów
    2. Plik na dysku ma być zapisywany co X bajtów bufora
    3. Operacje zapisu i odczytu trwają, jak zrobić,
       aby do bufora podczas zapisu na dysk,
       nadal można było pisać?
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sys.getsizeof(obj)` returns `obj` size in bytes

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from inspect import isclass, ismethod

    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, 'BUFFER_LIMIT')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)
    >>> assert File.BUFFER_LIMIT == 100

    >>> with File('_temporary.txt') as file:
    ...    file.append('One')
    ...    file.append('Two')
    ...    file.append('Three')
    ...    file.append('Four')
    ...    file.append('Five')
    ...    file.append('Six')

    >>> open('_temporary.txt').read()
    'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'

    >>> remove('_temporary.txt')
"""

from sys import getsizeof
from typing import ClassVar


class File:
    ...


# Solution
class File:
    BUFFER_LIMIT: ClassVar[int] = 100
    filename: str
    buffer: list[str]

    def __init__(self, filename):
        self.filename = filename
        self.buffer = []

    def append(self, line: str):
        to_append = line + '\n'
        if getsizeof(to_append) >= self.BUFFER_LIMIT:
            raise BufferError('Cannot fit data into buffer (even empty)')
        if getsizeof(self.buffer) + getsizeof(to_append) >= self.BUFFER_LIMIT:
            self.write(mode='a')
        self.buffer.append(to_append)

    def write(self, mode):
        to_write, self.buffer = self.buffer, []
        with open(self.filename, mode=mode) as file:
            file.writelines(to_write)

    def __enter__(self):
        self.write(mode='w')
        return self

    def __exit__(self, *args):
        self.write(mode='a')

"""
* Assignment: Protocol Context Manager AutoSave
* Complexity: hard
* Lines of code: 13 lines
* Time: 8 min

English:
    1. Modify class `File`
    2. Add class configuration attribute `AUTOSAVE_SECONDS: float = 1.0`
    3. Save buffer content to file every `AUTOSAVE_SECONDS` seconds
    4. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `File`
    2. Dodaj klasowy atrybut konfiguracyjny `AUTOSAVE_SECONDS: float = 1.0`
    3. Zapisuj zawartość bufora do pliku co `AUTOSAVE_SECONDS` sekund
    4. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `from threading import Timer`
    * `timer = Timer(interval, function)`
    * `timer.start()`
    * `timer.cancel()`
    * `ctrl+c` or stop button kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from inspect import isclass, ismethod

    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, 'AUTOSAVE_SECONDS')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)
    >>> assert File.AUTOSAVE_SECONDS == 1.0

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

from threading import Timer


class File:
    ...


# Solution
class File:
    filename: str
    buffer: list[str]
    timer: Timer
    AUTOSAVE_SECONDS: float = 1.0

    def __init__(self, filename):
        self.filename = filename
        self.buffer = []

    def append(self, line):
        self.buffer.append(line + '\n')

    def write(self, mode='a'):
        to_write = self.buffer.copy()
        self.buffer = []
        with open(self.filename, mode=mode) as file:
            file.writelines(to_write)
        self.set_timer()

    def set_timer(self):
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.timer = Timer(self.AUTOSAVE_SECONDS, self.write)
        self.timer.start()

    def __enter__(self):
        self.write(mode='w')
        return self

    def __exit__(self, *args):
        self.write()
        self.timer.cancel()

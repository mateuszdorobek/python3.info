"""
* Assignment: Protocol ContextManager File
* Complexity: easy
* Lines of code: 14 lines
* Time: 8 min

English:
    1. Define class `File` with parameter: `filename: str`
    2. `File` must implement Context Manager protocol
    3. `File` buffers lines added using `File.append(text: str)` method
    4. On `with` block exit, `File` class:
        a. Creates file (if not exists)
        b. Opens file
        c. Writes buffer to file
        d. Clears buffer
        e. Closes file
    5. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `File` z parametrem: `filename: str`
    2. `File` ma implementować protokół Context Manager
    3. `File` buforuje linie dodawane za pomocą metody `File.append(text: str)`
    4. Na wyjściu z bloku `with`, klasa `File`:
        a. Tworzy plik (jeżeli nie istnieje)
        b. Otwiera plik
        c. Zapisuje bufor do pliku
        d. Czyści bufor
        e. Zamyka plik
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Append newline character (`\n`) before adding to buffer

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from inspect import isclass, ismethod

    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)

    >>> with File('_temporary.txt') as file:
    ...    file.append('One')
    ...    file.append('Two')

    >>> open('_temporary.txt').read()
    'One\\nTwo\\n'

    >>> remove('_temporary.txt')
"""

class File:
    ...


# Solution
class File:
    filename: str
    buffer: list[str]

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.buffer = []

    def append(self, line: str) -> None:
        self.buffer.append(line + '\n')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.filename, mode='w') as file:
            file.writelines(self.buffer)

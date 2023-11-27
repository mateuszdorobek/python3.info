"""
* Assignment: File Path Abspath
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Define `path` with converted `filename` to absolute path
    2. To `result` assgin string:
        a. `file` if path is a file
        b. `directory` if path is a directory
        c. `missing` if path does not exist
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `path` z przekonwertowym `filename` do ścieżki bezwzględnej
    2. Do `result` przypisz ciąg znaków:
        a. `file` jeżeli ścieżka jest plikiem
        b. `directory` jeżeli ścieżka jest katalogiem
        c. `missing` jeżeli ścieżka nie istnieje
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `from pathlib import Path`
    * `Path.cwd()`
    * `Path()`
    * `Path.is_dir()`
    * `Path.is_file()`
    * `Path.exists()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert isinstance(result, str), \
    'Result must be a str with: `file`, `directory` or `missing`'

    >>> assert isinstance(abspath, Path), \
    'Use Path class from pathlib library to create a filepath'

    >>> current_directory = Path.cwd()
    >>> assert str(current_directory) in str(abspath), \
    'File Path must be absolute, check if you have current directory in path'

    >>> result
    'missing'
"""

from pathlib import Path


FILENAME = 'myfile.txt'

# Absolute path to FILENAME
# type: Path
abspath = ...

# File, directory or missing
# type: str
result = ...

# Solution
abspath = Path.cwd() / FILENAME

if abspath.is_file():
    result = 'file'
elif abspath.is_dir():
    result = 'directory'
elif not abspath.exists():
    result = 'missing'

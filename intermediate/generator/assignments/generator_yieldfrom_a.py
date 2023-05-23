"""
* Assignment: Generator YieldFrom Path
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create function `get_files()`
    2. Using `Pathlib.glob()` return files in `path: Path`:
       a. Python files (extension: `*.py`)
       b. ReST files (extension: `*.rst`)
    3. Return result as `Iterator[Path]` using `yield from`

Polish:
    1. Stwórz funkcję `get_files()`
    2. Używając `Pathlib.glob()` zwróć pliki w katalogu `path: Path`:
       a. Pliki Python (rozszerzenie: `*.py`)
       b. Pliki ReST (rozszerzenie: `*.rst`)
    3. Zwróć wyniki jako `Iterator[Path]` używając `yield from`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isgenerator, isgeneratorfunction

    >>> path = Path.cwd()
    >>> file = get_files(path)

    >>> assert isgeneratorfunction(get_files)
    >>> assert isgenerator(file)
    >>> assert isinstance(next(file), Path)
"""

from pathlib import Path
from typing import Iterator


def get_files(path: Path) -> Iterator[Path]:
    ...


# Solution
def get_files(path: Path) -> Iterator[Path]:
    yield from path.glob(f'*.py')
    yield from path.glob(f'*.rst')

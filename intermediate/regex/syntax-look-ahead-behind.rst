Regex Syntax Look Ahead/Behind
==============================


Syntax
------
* ``(?=)`` - Lookahead
* ``(?<=)`` - Lookbehind
* ``(?!foo)`` - Negative Lookahead
* ``(?<!foo)`` - Negative Lookbehind
* ``\K`` - Stop Look Behind


Example
-------
* ``(?=foo)`` - asserts that what immediately follows the current position in the string is ``foo``
* ``(?<=foo)`` - asserts that what immediately precedes the current position in the string is ``foo``
* ``(?!foo)`` - Asserts that what immediately follows the current position in the string is not foo
* ``(?<!foo)`` - Asserts that what immediately precedes the current position in the string is not foo
* ``^\s+sh '\K.+(?=')`` - if line starts with ``sh`` at any indentation, then take the content of whats inside of apostrophes
* ``d(?=r)`` - matches a ``d`` only if is followed by ``r``, but ``r`` will not be part of the overall regex match
* ``(?<=r)d`` - matches a ``d`` only if is preceded by an ``r``, but ``r`` will not be part of the overall regex match

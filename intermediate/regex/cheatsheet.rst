Regex Cheatsheet
================
* Also known as: "Regular Expressions", "Regular Expr", "regexp", "regex" or "re"
* ``a`` - exact
* ``a|b`` - alternative
* ``[abc]`` - enumerated character class
* ``[a-z]`` - range character class
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)
* ``[^]`` - negation
* ``\d`` - digit (alias to ``[0-9]``)
* ``\D`` - anything but digit (alias to ``[^0-9]``)
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\b`` - word boundary
* ``\B`` - anything but word boundary
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
* ``{n}`` - exactly `n` repetitions, exact
* ``{,n}`` - maximum `n` repetitions, greedy (prefer longest)
* ``{n,}`` - minimum `n` repetitions, greedy (prefer longest)
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, greedy (prefer longest)
* ``*`` - minimum 0 repetitions, no maximum, greedy (prefer longest), alias to ``{0,}``
* ``+`` - minimum 1 repetitions, no maximum, greedy (prefer longest), alias to ``{1,}``
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, greedy (prefer longest), alias to ``{0,1}``
* ``{,n}?`` - maximum `n` repetitions, lazy (prefer shorter)
* ``{n,}?`` - minimum `n` repetitions, lazy (prefer shorter)
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, lazy (prefer shorter)
* ``*?`` - minimum 0 repetitions, no maximum, lazy (prefer shorter), alias to ``{0,}?``
* ``+?`` - minimum 1 repetitions, no maximum, lazy (prefer shorter), alias to ``{1,}?``
* ``??`` - minimum 0 repetitions, maximum 1 repetition, lazy (prefer shorter), alias to ``{0,1}?``
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group (positional)
* ``(?P<mygroup>...)`` - named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment
* ``(?P=name)`` - backreferencing by group name
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation

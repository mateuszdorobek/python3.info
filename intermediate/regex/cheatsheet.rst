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


Literals
--------
* Also known as "Literal Characters"
* Occurrence of that character in the string

Syntax:

* ``a`` - exact
* ``a|b`` - alternative

Example:

* ``1`` - number 1 anywhere in text
* ``1|2|3`` - numbers 1, 2 or 3 anywhere in text


Classes
-------
* Also known as "Character Classes"
* One out of several characters

Syntax:

* ``[abc]`` - enumeration
* ``[a-z]`` - range

Examples:

* ``[12345]`` - numbers 1,2,3,4 or 5 anywhere in text
* ``[0-9]`` - numbers from 0 to 9 anywhere in text
* ``[a-z]`` - lowercase letters from a to z anywhere in text
* ``[A-Z]`` - uppercase letters from A to Z anywhere in text
* ``[a-zA-Z0-9]`` - uppercase and lowercase letters (from a to z) anywhere in text


Metacharacters
--------------
* Special characters

* ``\`` - backslash
* ``^`` - caret
* ``$`` - dollar sign
* ``.`` - period or dot
* ``|`` - vertical bar or pipe symbol
* ``?`` - question mark
* ``*`` - asterisk or star
* ``+`` - plus sign
* ``(`` - opening parenthesis
* ``)`` - closing parenthesis
* ``[`` - opening square bracket
* ``[`` - closing square bracket
* ``{`` - opening curly brace
* ``}`` - closing curly brace

Example:

* ``.`` - Any character anywhere in text, by default does not match a newline (this changes with ``re.DOTALL``)


Anchors
-------
* Match a position before, after, or between characters

Syntax:

* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)

Examples:

* ``^[0-9]`` - digit at the line start
* ``[0-9]$`` - digit at the line end
* ``\A[0-9]`` - digit at the text start
* ``[0-9]\Z`` - digit at the text end


Negation
--------
* Negation logically inverts qualifier

Syntax:

* ``[^]`` - negation

Examples:

* ``[0-9]`` - digit anywhere in text
* ``[^0-9]`` - anything but a digit anywhere in text
* ``^[0-9]`` - digit at the beginning of a line
* ``^[^0-9]`` - not-a-digit at the beginning of a line


Shorthands
----------
* Shorthand Character Classes

Syntax:

* ``\d`` - digit anywhere in text, alias to ``[0-9]``
* ``\D`` - anything but a digit anywhere in text, alias to ``[^0-9]``
* ``\s`` - whitespace character (space, tab, newline, non-breaking space), alias to ``[ \t\v\f\n\r\n]``
* ``\S`` - anything but a whitespace
* ``\btodo\b`` - word boundary, string "todo" being a separate word, but non alphabet characters can precede or follow: 'todo:', 'todo()'
* ``\Btodo\B`` - anything but word boundary, string "todo" being a part of other word, such as: 'mastodont' or 'autodoc'
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes, brackets)


Quantifiers
-----------
* Repetition
* How many occurrences of preceding token
* Exact - exactly number of times
* Greedy - prefer longest match, works better with numbers, (default)
* Lazy - prefer shortest matches - works better with text

Exact:

* ``{n}`` - exactly `n` repetitions

Greedy:

* ``{,n}`` - maximum `n` repetitions, prefer longer (greedy)
* ``{n,}`` - minimum `n` repetitions, prefer longer (greedy)
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer (greedy)
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``) (greedy)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``) (greedy)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer  (alias to ``{0,1}``) (greedy)

Lazy:

* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)

Examples:

* ``\d{4}`` - digit exactly 4 times (exact)
* ``\d{2,4}`` - digit from 2 to 4 times (greedy, prefer longest)
* ``\d{2,}`` - digit from 2 to infinity times (greedy, prefer longest)
* ``\d{,4}`` - digit from 0 to 4 times (greedy, prefer longest)
* ``\d{1,}`` - at least one digit (greedy, prefer longest)
* ``\d+`` - at least one digit, alias to ``\d{1,}`` (greedy, prefer longest)
* ``\d{0,}`` - at least zero digit (greedy, prefer longest)
* ``\d*`` - at least zero digit, alias to ``\d{0,}`` (greedy, prefer longest)
* ``\d{0,1}`` - optional digit (greedy, prefer longest)
* ``\d?`` - optional digit, alias to ``\d{0,1}`` (greedy, prefer longest)
* ``\d{2,4}?`` - digit from 2 to 4 times (lazy, prefer shortest)
* ``\d{2,}?`` - digit from 2 to infinity times (lazy, prefer shortest)
* ``\d{,4}?`` - digit from 0 to 4 times (lazy, prefer shortest)
* ``\d{1,}?`` - at least one digit (lazy, prefer shortest)
* ``\d+?`` - at least one digit, alias to ``\d{1,}`` (lazy, prefer shortest)
* ``\d{0,}?`` - at least zero digit (lazy, prefer shortest)
* ``\d*?`` - at least zero digit, alias to ``\d{0,}`` (lazy, prefer shortest)
* ``\d{0,1}?`` - optional digit (lazy, prefer shortest)
* ``\d??`` - optional digit, alias to ``\d{0,1}`` (lazy, prefer shortest)


Groups
------
* Catch expression results
* Can be named or positional

Syntax:

* ``(...)`` - unnamed group (positional)
* ``(?P<mygroup>...)`` - named group (with name: `mygroup`)
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment

Examples:

* ``(\d{1,2})`` - group with 1 or 2 digits (unnamed group)
* ``(?P<year>\d{4})`` - 4 digits in a group named "year" (named group)
* ``(?P<month>\w+)`` - three word characters in a group named "month" (named group)
* ``(?P<day>\d{1,2})`` - 1 or 2 digits in a group named "day" (named group)
* ``Nov (\d{1,2})`` - text "Nov" followed by 1 or 2 digits (unnamed group)
* ``Nov \d{2}(st|nd|th|rd)`` - text "Nov" followed by by 1 or 2 digits and one of: "st", "nd", "th" or "rd" - match the ordinal
* ``Nov \d{2}(?:st|nd|th|rd)`` - text "Nov" followed by by 1 or 2 digits and one of: "st", "nd", "th" or "rd" - do not match the ordinal
* ``Nov \d{2}st(?#ordinal)`` - text "Nov" followed by by 1 or 2 digits and one of: "st", "nd", "th" or "rd" and comment "ordinal"


Backreference
-------------
* Match the same text as previously matched by a capturing group

Syntax:

* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``(?P=name)`` - backreferencing by group name

Examples:

* ``\g<2> \g<1> \g<3>``
* ``\g<day> \g<month> \g<year>``
* ``<(?P<tagname>[a-z]+)>(.*)</(?P=tagname)>``


Flags
-----
* ``re.ASCII`` - perform ASCII-only matching instead of full Unicode matching
* ``re.IGNORECASE`` - case-insensitive search
* ``re.LOCALE`` - case-insensitive matching dependent on the current locale (deprecated)
* ``re.MULTILINE`` - match can start in one line, and end in another
* ``re.DOTALL`` - dot (``.``) matches also newline characters
* ``re.UNICODE`` - turns on unicode character support for ``\w``
* ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``
* ``re.DEBUG`` - display debugging information during pattern compilation


Python
------
* ``re.findall()`` - all matches at once, returns ``list[str]``
* ``re.finditer()`` - all matches one at a time, returns ``Iterator[re.Match]``
* ``re.search()`` - whether text contains (stop after first match), returns ``re.Match | None``
* ``re.match()`` - whether text matches pattern (validation, np. email, ssn, tax id, phone), returns ``re.Match | None``
* ``re.split()`` - splits text by pattern, returns ``list[str]``
* ``re.sub()`` - replaces group matches in text (works best with named groups), returns ``str``
* ``re.compile()`` - prepares pattern for further use (match against it), returns ``re.Pattern``


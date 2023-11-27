"""
* Assignment: String Define Quotes
* Type: homework
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. To print use f-string formatting
    2. Note, that second line starts with tab
    3. Value `NAME` in double quotes is a name read from user
    4. Mind the different quotes, apostrophes, tabs and newlines
    5. Do not use neither space not enter - use `\n` and `\t`
    6. Do not use string addition (`str + str`)
    7. Run doctests - all must succeed

Polish:
    1. Do wypisania użyj f-string formatting
    2. Zauważ, że druga linijka zaczyna się od tabulacji
    3. Wartość `NAME` w podwójnych cudzysłowach to ciąg od użytkownika
    4. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
    5. Nie używaj spacji ani klawisza enter - użyj `\n` i `\t`
    6. Nie korzystaj z dodawania stringów (`str + str`)
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    '''My name... "José Jiménez".
        I'm an \"\"\"astronaut!\"\"\"'''
"""

NAME = 'José Jiménez'

# Add whitespace and quotes to: My name... José Jiménez. I'm an astronaut!
# type: str
result = ...

# Solution
result = f"""'''My name... "{NAME}".\n\tI\'m an \"\"\"astronaut!\"\"\"'''"""

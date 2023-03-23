"""
* Assignment: Mapping Switch Value
* Required: no
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create translator of pilot's alphabet
    2. Each letter has it's phonetic counterpart
    3. Ask user to input letter
    4. User will always put only one capitalized letter or number
    5. Define `result: str` with phonetic letter pronunciation
    6. If character not existing in alphabet, print: 'Not found'
    7. Do not use `if`, `try`, and `except`
    8. `MagicMock` will simulate inputting a letter by user
    9. Use `input()` function as normal
    10. Run doctests - all must succeed

Polish:
    1. Stwórz tłumacza alfabetu pilotów
    2. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    3. Poproś użytkownika o wprowadzenie litery
    4. Użytkownik zawsze poda tylko jedną dużą literę lub cyfrę
    5. Zdefiniuj `result: str` z fonetyczną wymową litery
    6. Jeżeli znak nie występuje w alfabecie, wypisz: 'Not found'
    7. Nie używaj `if`, `try` ani `except`
    8. `MagicMock` zasymuluje wpisanie litery przez użytkownika
    9. Skorzytaj z funkcji `input()` tak jak normalnie
    10. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `input()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import string

    >>> assert letter is not Ellipsis, \
    'Ask user to input letter and assign it to: `letter`'

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Mike'
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['M'])

ALPHABET = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whisky',
    'X': 'X-Ray',
    'Z': 'Zulu',
}

# String with letter from user
# type: str
letter = ...

# String with converted letter to Pilot alphabet or 'Not found'
# type: str
result = ...

# Solution
letter = input('Type letter: ')
result = ALPHABET.get(letter, 'Not found')

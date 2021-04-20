"""
* Assignment: Loop While Translate
* Status: required
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `while` to iterate over `DATA`
    3. If letter is in `PL` then use conversion value as letter
    4. Add letter to `result`
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `while` do iteracji po `DATA`
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. Dodaj literę do `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> type(result)
    <class 'str'>
    >>> result
    'zazolc gesla jazn'
"""

# Given
PL = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

DATA = 'zażółć gęślą jaźń'

result = ...  # str: DATA with substituted PL diacritic chars to ASCII letters

# Solution
result = ''
i = 0

while i < len(DATA):
    letter = DATA[i]
    result += PL.get(letter, letter)
    i += 1

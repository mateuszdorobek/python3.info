"""
* Assignment: Loop For Translate
* Status: required
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: str`
    3. Use `for` to iterate over `DATA`
    4. If letter is in `PL` then use conversion value as letter
    5. Add letter to `result`
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: list`
    3. Użyj `for` do iteracji po `DATA`
    4. Jeżeli litera jest w `PL` to użyj przekonwertowanej wartości jako litera
    5. Dodaj literę do `result`
    6. Uruchom doctesty - wszystkie muszą się powieść

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

for letter in DATA:
    result += PL.get(letter, letter)

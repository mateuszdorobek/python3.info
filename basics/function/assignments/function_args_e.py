"""
* Assignment: Function Arguments Clean
* Type: homework
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Write function cleaning up data
    2. Function takes one argument of type `str`
    3. Function returns cleaned text
    4. Run doctests - all must succeed

Polish:
    1. Napisz funkcję czyszczącą dane
    2. Funkcja przyjmuje jeden argument typu `str`
    3. Funkcja zwraca oczyszczony tekst
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert clean is not Ellipsis, \
    'Write solution inside `clean` function'
    >>> assert isfunction(clean), \
    'Object `clean` must be a function'

    >>> clean('ul.Mieszka II')
    'Mieszka II'
    >>> clean('UL. Zygmunta III WaZY')
    'Zygmunta III Wazy'
    >>> clean('  bolesława chrobrego ')
    'Bolesława Chrobrego'
    >>> clean('ul Jana III SobIESkiego')
    'Jana III Sobieskiego'
    >>> clean('\tul. Jana trzeciego Sobieskiego')
    'Jana III Sobieskiego'
    >>> clean('ulicaJana III Sobieskiego')
    'Jana III Sobieskiego'
    >>> clean('UL. JA    NA 3 SOBIES  KIEGO')
    'Jana III Sobieskiego'
    >>> clean('ULICA JANA III SOBIESKIEGO  ')
    'Jana III Sobieskiego'
    >>> clean('ULICA. JANA III SOBIeskieGO')
    'Jana III Sobieskiego'
    >>> clean(' Jana 3 Sobieskiego  ')
    'Jana III Sobieskiego'
    >>> clean('Jana III Sobi  eskiego ')
    'Jana III Sobieskiego'

TODO: Translate input data to English
"""


# Solution
def clean(text):
    return (text

            # Convert to common format
            .upper()

            # Remove unwanted whitespaces
            .replace('\n', '')
            .replace('\t', '')
            .replace('     ', '')
            .replace('    ', '')
            .replace('   ', '')
            .replace('  ', '')

            # Remove unwanted special characters
            .replace('.', '')
            .replace(',', '')
            .replace('-', '')
            .replace('|', '')

            # Remove unwanted text
            .replace('ULICA', '')
            .replace('UL', '')
            .replace('TRZECIEGO', 'III')
            .replace('3', 'III')

            # Formatting
            .title()
            .replace('Iii', 'III')
            .replace('Ii', 'II')
            .strip())

"""
* Assignment: Function Arguments Translate
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define function `translate` with parameter `text`
    2. Use `str.join()` with generator expression to iterate over `text`
    3. If letter is in `PL` then use conversion value as letter,
       otherwise take letter
    4. Return from function translated `text`
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `translate` przyjmującą parametr `text`
    2. Użyj `str.join()` z wyrażeniem generatorowym do iteracji po `text`
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera,
       w przeciwnym przypadku to weź literę
    4. Zwróć z funkcji przetłumaczony `text`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert translate is not Ellipsis, \
    'Write solution inside `translate` function'
    >>> assert isfunction(translate), \
    'Object `translate` must be a function'

    >>> translate('zażółć')
    'zazolc'
    >>> translate('gęślą')
    'gesla'
    >>> translate('jaźń')
    'jazn'
    >>> translate('zażółć gęślą jaźń')
    'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}


# Solution
def translate(text):
    return ''.join(PL.get(x, x) for x in text)

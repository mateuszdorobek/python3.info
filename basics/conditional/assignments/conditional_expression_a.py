"""
* Assignment: Conditional Expression Underage/Adult
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str` with:
       a. 'underage' if user age is less than 18
       b. 'adult' if user age is equal or greater than 18
    2. Non-functional requirements:
       a. Use one line `if`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z:
       a. 'underage' jeżeli wiek użytkownika jest mniejszy niż 18
       b. 'adult' jeżeli wiek użytkownika jest równy lub większy 18
    2. Wymagania niefunkcjonalne:
       a. Wykorzystaj jednolinikowego `if`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `>=`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert result in ('underage', 'adult'), \
    'Variable `result` must be either `underage` or `adult`'
"""

ADULT = 18
AGE = 12

# Whether 'adult' or 'underage'
# type: str
result = ...

# Solution
result = 'adult' if AGE >= ADULT else 'underage'

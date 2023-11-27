"""
* Assignment: Comprehension Nested Dict
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Convert to `result: dict[str, str]`
    2. Use nested dict comprehension
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj do `result: dict[str, str]`
    2. Użyj zagnieżdżonego rozwinięcia słownikowego
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * nested `for`
    * `dict.items()`
    * `str()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Doctorate': 6,
     'Prof-school': 6,
     'Masters': 5,
     'Bachelor': 5,
     'Engineer': 5,
     'HS-grad': 4,
     'Junior High': 3,
     'Primary School': 2,
     'Kindergarten': 1}
"""

DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

# Converted DATA. Note values are str not int!
# type: dict[str,str]
result = ...

# Solution
result = {title: lvl
          for lvl, titles in DATA.items()
          for title in titles}

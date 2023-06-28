"""
* Assignment: DataFrame Create
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Create `result: pd.DataFrame` for input data
    2. Name columns: `Crew`, `Role`, `Astronaut`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz `result: pd.DataFrame` dla danych wejściowych
    2. Name columns: `Crew`, `Role`, `Astronaut`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use selection with `alt` key in your IDE

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
         Crew Role        Astronaut
    0   Prime  CDR   Neil Armstrong
    1   Prime  LMP      Buzz Aldrin
    2   Prime  CMP  Michael Collins
    3  Backup  CDR     James Lovell
    4  Backup  LMP   William Anders
    5  Backup  CMP       Fred Haise
"""

import pandas as pd

"""
"commander", "Melissa", "Lewis"
"botanist", "Mark", "Watney"
"pilot", "Rick", "Martinez"
"chemist", "Alex", "Vogel"
"engineer", "Beth", "Johanssen"
"CMP", "Chris", "Back"
"""


# type: pd.DataFrame
result = ...


# Solution
result = pd.DataFrame({
    'Crew': ['Prime', 'Prime', 'Prime', 'Backup', 'Backup', 'Backup'],
    'Role': ['CDR', 'LMP', 'CMP', 'CDR', 'LMP', 'CMP'],
    'Astronaut': ['Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'James Lovell', 'William Anders', 'Fred Haise'],
})


# Alternative Solution
# result = pd.DataFrame([
#     {'Crew': 'Prime', 'Role': 'CDR', 'Astronaut': 'Neil Armstrong'},
#     {'Crew': 'Prime', 'Role': 'LMP', 'Astronaut': 'Buzz Aldrin'},
#     {'Crew': 'Prime', 'Role': 'CMP', 'Astronaut': 'Michael Collins'},
#     {'Crew': 'Backup', 'Role': 'CDR', 'Astronaut': 'James Lovell'},
#     {'Crew': 'Backup', 'Role': 'LMP', 'Astronaut': 'William Anders'},
#     {'Crew': 'Backup', 'Role': 'CMP', 'Astronaut': 'Fred Haise'},
# ])

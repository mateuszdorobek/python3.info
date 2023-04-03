"""
* Assignment: Pandas Read HTML
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `data: pd.DataFrame`
    2. Define `result` with active European Space Agency astronauts
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `data: pd.DataFrame`
    2. Zdefiniuj `result` z aktywnymi astronautami Europejskiej Agencji Kosmicznej
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pip install --upgrade lxml`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result['Name']
    0    Samantha Cristoforetti
    1           Alexander Gerst
    2          Andreas Mogensen
    3            Luca Parmitano
    4             Timothy Peake
    5            Thomas Pesquet
    6           Matthias Maurer
    Name: Name, dtype: object
"""

import pandas as pd


DATA = 'https://python3.info/_static/european-astronaut-corps.html'


# Read DATA, select active ESA astronauts
# type: pd.DataFrame
result = ...

# Solution
data = pd.read_html(DATA)
result = data[0]

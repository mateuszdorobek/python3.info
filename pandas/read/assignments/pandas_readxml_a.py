"""
* Assignment: Pandas Read XML
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `pd.DataFrame`
    2. Define `result: float` with calculated mean cost of flower
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `pd.DataFrame`
    2. Zdefiniuj `result: float` z wyliczonym średnią ceną kwiatów
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pip install --upgrade lxml`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import numpy

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is numpy.float64, \
    'Variable `result` has invalid type, should be `numpy.float64`'

    >>> result
    7.125
"""

import pandas as pd

DATA = """
    <catalog>
        <plant>
            <common>bloodroot</common>
            <botanical>sanguinaria canadensis</botanical>
            <zone>4</zone>
            <light>mostly shady</light>
            <price>2.40 USD</price>
            <availability>031599</availability>
        </plant>
        <plant>
            <common>columbine</common>
            <botanical>aquilegia canadensis</botanical>
            <zone>3</zone>
            <light>mostly shady</light>
            <price>9.40 USD</price>
            <availability>030699</availability>
        </plant>
        <plant>
            <common>marsh marigold</common>
            <botanical>caltha palustris</botanical>
            <zone>4</zone>
            <light>mostly sunny</light>
            <price>6.80 USD</price>
            <availability>051799</availability>
        </plant>
        <plant>
            <common>cowslip</common>
            <botanical>caltha palustris</botanical>
            <zone>4</zone>
            <light>mostly shady</light>
            <price>9.90 USD</price>
            <availability>030699</availability>
        </plant>
    </catalog>
"""


# read DATA from XML
# calculate mean price
# type: pd.DataFrame
result = ...

# Solution
result = (
    pd
    .read_xml(DATA)
    .loc[:, 'price']
    .str.removesuffix(' USD')
    .astype('float64')
    .mean()
)

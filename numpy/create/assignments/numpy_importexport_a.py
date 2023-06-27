"""
* Assignment: Numpy Loadtext
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Load text from `DATA`
    2. Define variables:
        a. `species: np.ndarray[str]` - first row, columns 2, 3, 4
        b. `features: np.ndarray[float]` - all rows except the first one, columns 0, 1, 2, 3
        c. `labels: np.ndarray[int]` - all rows except the first one, column 4
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj tekst z `DATA`
    2. Zdefiniuj zmienne:
        a. `species: np.ndarray[str]` - pierwszy wiersz, kolumny 2, 3, 4
        b. `features: np.ndarray[float]` - wszystkie wiersze poza pierwszym, kolumny 0, 1, 2, 3
        c. `labels: np.ndarray[int]` - wszystkie wiersze poza pierwszym, kolumna 4
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert species is not Ellipsis, \
    'Assign result to variable: `species`'
    >>> assert labels is not Ellipsis, \
    'Assign result to variable: `labels`'
    >>> assert features is not Ellipsis, \
    'Assign result to variable: `features`'

    >>> assert type(species) is np.ndarray, \
    'Variable `species` has invalid type, expected: np.ndarray'
    >>> assert type(features) is np.ndarray, \
    'Variable `features` has invalid type, expected: np.ndarray'
    >>> assert type(labels) is np.ndarray, \
    'Variable `labels` has invalid type, expected: np.ndarray'

    >>> assert species.dtype == np.dtype('<U10'), \
    'Variable `species` has invalid type, expected: str'
    >>> assert features.dtype is np.dtype('float64'), \
    'Variable `features` has invalid type, expected: float'
    >>> assert labels.dtype is np.dtype('int64'), \
    'Variable `labels` has invalid type, expected: int'

    >>> assert len(species) == 3, \
    'Variable `species` length should be 3'
    >>> assert len(features) == 151, \
    'Variable `features` length should be 151'
    >>> assert len(labels) == 151, \
    'Variable `labels` length should be 151'

    >>> species
    array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

    >>> features[:3]
    array([[5.4, 3.9, 1.3, 0.4],
           [5.9, 3. , 5.1, 1.8],
           [6. , 3.4, 4.5, 1.6]])

    >>> features[-3:]
    array([[4.9, 2.5, 4.5, 1.7],
           [6.3, 2.8, 5.1, 1.5],
           [6.8, 3.2, 5.9, 2.3]])

    >>> labels
    array([0, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 1,
           1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 2,
           0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0,
           0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1,
           0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2,
           0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1,
           0, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2])
"""

import numpy as np


DATA = 'https://python3.info/_static/iris-dirty.csv'

species = ...
features = ...
labels = ...


# Solution
species = np.loadtxt(DATA, delimiter=',', dtype='str', max_rows=1, usecols=(2, 3, 4))
features = np.loadtxt(DATA, delimiter=',', dtype='float', skiprows=1, usecols=(0, 1, 2, 3))
labels = np.loadtxt(DATA, delimiter=',', dtype='int', skiprows=1, usecols=4)

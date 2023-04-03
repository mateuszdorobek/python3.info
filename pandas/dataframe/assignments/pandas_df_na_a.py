"""
* Assignment: DataFrame NaN
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Pomiń pierwszą linię z metadanymi
    3. Zmień nazwy kolumn na:
        a. Sepal length
        b. Sepal width
        c. Petal length
        d. Petal width
        e. Species
    4. Podmień wartości w kolumnie species
        a. 0 -> 'setosa',
        b. 1 -> 'versicolor',
        c. 2 -> 'virginica'
    5. Wybierz wartości w kolumnie 'Petal length' mniejsze od 4
    6. Wybrane wartości ustaw na `NaN`
    7. Interpoluj liniowo wszystkie wartości `NaN`
    8. Usuń wiersze z pozostałymi wartościami `NaN`
    9. Zdefiniuj `result` jako dwa pierwsze wiersze
    10. Uruchom doctesty - wszystkie muszą się powieść

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
       Sepal length  Sepal width  Petal length  Petal width     Species
    1           5.9          3.0           5.1          1.8   virginica
    2           6.0          3.4           4.5          1.6  versicolor
"""

import pandas as pd
import numpy as np


DATA = 'https://python3.info/_static/iris-dirty.csv'
COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']

# type: pd.DataFrame
result = ...


# Solution
class_labels = pd.read_csv(DATA, nrows=0).columns[2:]
label_encoder = dict(enumerate(class_labels))

result = (
    pd.read_csv(DATA, skiprows=1, names=COLUMNS)
      .replace({'Species': label_encoder})
)

query = result['Petal length'] < 4
result.loc[query, 'Petal length'] = np.nan
result = result.interpolate('linear')
result = result.dropna(how='any', axis='rows')
result = result.head(n=2)

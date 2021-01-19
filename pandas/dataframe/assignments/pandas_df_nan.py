"""
* Assignment: DataFrame NaN
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    TODO: English Translation

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. Pomiń pierwszą linię z metadanymi
    4. Zmień nazwy kolumn na:
        a. Sepal length
        b. Sepal width
        c. Petal length
        d. Petal width
        e. Species
    5. Podmień wartości w kolumnie species
        a. 0 -> 'setosa',
        b. 1 -> 'versicolor',
        c. 2 -> 'virginica'
    6. Wybierz wartości w kolumnie 'Petal length' mniejsze od 4
    7. Wybrane wartości ustaw na `NaN`
    8. Interpoluj liniowo wszystkie wartości `NaN`
    9. Usuń wiersze z pozostałymi wartościami `NaN`
    10. Zdefiniuj `result` jako dwa pierwsze wiersze

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
       Sepal length  Sepal width  Petal length  Petal width     Species
    1           5.9          3.0           5.1          1.8   virginica
    2           6.0          3.4           4.5          1.6  versicolor
"""


# Given
import pandas as pd
import numpy as np


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'
COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']

result = ...


# Solution
df = pd.read_csv(DATA)
species = dict(enumerate(df.columns[2:]))
df.columns = COLUMNS
df['Species'].replace(species, inplace=True)
df.loc[df['Petal length'] < 4.0, 'Petal length'] = np.nan
df = df.interpolate('linear')
df.dropna(inplace=True)
result = df.head(2)

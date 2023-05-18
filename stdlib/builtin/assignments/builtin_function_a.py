"""
* Assignment: Builtin Function Average
* Complexity: easy
* Lines of code: 12 lines
* Time: 13 min

English:
    1. Separate header and rows
    2. Define dict `result: dict[str, list]`, keys are column names from header
    3. For each row, add values to proper lists in `result`
    4. Define function `mean()`, calculating mean for arbitrary number of arguments
    5. Return `None` if any argument to the function is not `float` or `int`
    6. To calculate mean use built-in functions
    7. Iterating over `result` print column name and calculated average
    8. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od wierszy danych
    2. Zdefiniuj słownik `result: dict[str, list]`, klucze to nazwy kolumn z nagłówka
    3. Dla każdego wiersza, dodawaj wartości do odpowiednich list w `result`
    4. Zdefiniuj funkcję `mean()`, liczącą średnią dla dowolnej ilości argumentów
    5. Zwróć `None` jeżeli którykolwiek z argumentów do funkcji nie jest `float` lub `int`
    6. Do wyliczenia średniej wykorzystaj wbudowane funkcje
    7. Iterując po `result` wypisz nazwę kolumny oraz wyliczoną średnią
    8. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': 5.666666666666667,
     'sepal_width': 3.0500000000000003,
     'petal_length': 3.6666666666666665,
     'petal_width': 1.1500000000000001,
     'species': None}
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),]

result = {}


# Solution
def average(args):
    if all(isinstance(x, float) for x in args):
        return sum(args) / len(args)


header, *rows = DATA
result = {x:list() for x in header}

for row in rows:
    for i, head in enumerate(header):
        result[head].append(row[i])

result = {key: average(value)
          for key, value in result.items()}

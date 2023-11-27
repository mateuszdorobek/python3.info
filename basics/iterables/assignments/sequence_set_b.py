"""
* Assignment: Iterable Set Many
* Type: class assignment
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Non-functional requirements:
        a. Assignmnet verifies creation of `set()` and method `.add()` and
           `.update()` usage
        b. For simplicity numerical values type as `floats`, and not `str`
        c. Example: instead of '5.8' just type 5.8
        d. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or
           any other control-flow statement
    2. Create set `result` representing row with index 1
    3. Values from row at index 2 add to `result` using `.add()` (five calls)
    4. From row at index 3 create `set` and add it to `result` using
       `.update()` (one call)
    5. From row at index 4 `tuple` and add it to `result` using `.update()`
       (one call)
    6. From row at index 5 `list` and add it to `result` using `.update()` (
       one call)
    7. Run doctests - all must succeed

Polish:
    1. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `set()` oraz użycie metod `.add()` i
           `.update()`
        b. Dla uproszczenia wartości numeryczne wypisuj jako `float`,
        a nie `str`
        c. Przykład: zamiast '5.8' zapisz 5.8
        d. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub
           jakiejkolwiek innej instrukcji sterującej
    2. Stwórz zbiór `result` reprezentujący wiersz o indeksie 1
    3. Wartości z wiersza o indeksie 2 dodawaj do `result` używając `.add()`
       (pięć wywołań)
    4. Na podstawie wiersza o indeksie 3 stwórz `set` i dodaj go do `result`
       używając `.update()` (jedno wywołanie)
    5. Na podstawie wiersza o indeksie 4 stwórz `tuple` i dodaj go do
       `result` używając `.update()` (jedno wywołanie)
    6. Na podstawie wiersza o indeksie 5 stwórz `list` i dodaj go do
       `result` używając `.update()` (jedno wywołanie)
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is set, \
    'Variable `result` has invalid type, should be set'
    >>> assert len(result) == 22, \
    'Variable `result` length should be 22'

    >>> assert ('sepal_length' not in result
    ...     and 'sepal_width' not in result
    ...     and 'petal_length' not in result
    ...     and 'petal_width' not in result
    ...     and 'species' not in result)

    >>> assert result >= {5.8, 2.7, 5.1, 1.9, 'virginica'}
    >>> assert result >= {5.1, 3.5, 1.4, 0.2, 'setosa'}
    >>> assert result >= {5.7, 2.8, 4.1, 1.3, 'versicolor'}
    >>> assert result >= {6.3, 2.9, 5.6, 1.8, 'virginica'}
    >>> assert result >= {6.4, 3.2, 4.5, 1.5, 'versicolor'}
"""

DATA = [
    'sepal_length,sepal_width,petal_length,petal_width,species',
    '5.8,2.7,5.1,1.9,virginica',
    '5.1,3.5,1.4,0.2,setosa',
    '5.7,2.8,4.1,1.3,versicolor',
    '6.3,2.9,5.6,1.8,virginica',
    '6.4,3.2,4.5,1.5,versicolor',
]

# Set with row at DATA[1] (manually converted to float and str)
# type: set[float|str]
result = ...

# Add to result float 5.1
...

# Add to result float 3.5
...

# Add to result float 1.4
...

# Add to result float 0.2
...

# Add to result str setosa
...

# Update result with set 5.7, 2.8, 4.1, 1.3, 'versicolor'
...

# Update result with tuple 6.3, 2.9, 5.6, 1.8, 'virginica'
...

# Update result with list 6.4, 3.2, 4.5, 1.5, 'versicolor'
...

# Solution
result = {5.8, 2.7, 5.1, 1.9, 'virginica'}

result.add(5.1)
result.add(3.5)
result.add(1.4)
result.add(0.2)
result.add('setosa')

result.update({5.7, 2.8, 4.1, 1.3, 'versicolor'})
result.update((6.3, 2.9, 5.6, 1.8, 'virginica'))
result.update([6.4, 3.2, 4.5, 1.5, 'versicolor'])

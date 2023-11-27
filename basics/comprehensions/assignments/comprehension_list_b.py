"""
* Assignment: Comprehension List Split
* Type: homework
* Complexity: medium
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Using List Comprehension split `DATA` into:
        a. `features_train: list[tuple]` - 60% of first features in `DATA`
        b. `features_test: list[tuple]` - 40% of last features in `DATA`
        c. `labels_train: list[str]` - 60% of first labels in `DATA`
        d. `labels_test: list[str]` - 40% of last labels in `DATA`
    2. In order to do so, calculate pivot point:
        a. length of `DATA` times given percent (60% = 0.6)
        b. remember, that slice indicies must be `int`, not `float`
        c. for example: if dataset has 10 rows, then 6 rows will be for
           training, and 4 rows for test
    3. Run doctests - all must succeed

Polish:
    1. Używając List Comprehension podziel `DATA` na:
        a. `features_train: list[tuple]` - 60% pierwszych features w `DATA`
        b. `features_test: list[tuple]` - 40% ostatnich features w `DATA`
        c. `labels_train: list[str]` - 60% pierwszych labels w `DATA`
        d. `labels_test: list[str]` - 40% ostatnich labels w `DATA`
    2. Aby to zrobić, wylicz punkt podziału:
        a. długość `DATA` razy zadany procent (60% = 0.6)
        b. pamiętaj, że indeksy slice muszą być `int` a nie `float`
        c. na przykład: if zbiór danych ma 10 wierszy, to 6 wierszy będzie
        do treningu, a 4 do testów
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `iterable[:split]`
    * `iterable[split:]`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(features_train) is list, \
    'make sure features_train is a list'

    >>> assert type(features_test) is list, \
    'make sure features_test is a list'

    >>> assert type(labels_train) is list, \
    'make sure labels_train is a list'

    >>> assert type(labels_test) is list, \
    'make sure labels_test is a list'

    >>> assert all(type(x) is tuple for x in features_train), \
    'all elements in features_train should be tuple'

    >>> assert all(type(x) is tuple for x in features_test), \
    'all elements in features_test should be tuple'

    >>> assert all(type(x) is str for x in labels_train), \
    'all elements in labels_train should be str'

    >>> assert all(type(x) is str for x in labels_test), \
    'all elements in labels_test should be str'

    >>> features_train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]

    >>> features_test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4),
     (7.6, 3.0, 6.6, 2.1),
     (4.9, 3.0, 1.4, 0.2),
     (4.9, 2.5, 4.5, 1.7)]

    >>> labels_train
    ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']

    >>> labels_test
    ['versicolor', 'virginica', 'setosa', 'virginica']
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

ratio = 0.6
header, *rows = DATA
split = int(len(rows) * ratio)

# Solution
features_train = [row[0:4] for row in rows[:split]]
features_test = [row[0:4] for row in rows[split:]]
labels_train = [row[4] for row in rows[:split]]
labels_test = [row[4] for row in rows[split:]]

# Alternative Solution
features = [row[0:4] for row in rows]
labels = [row[4] for row in rows]
features_train = features[:split]
features_test = features[split:]
labels_train = labels[:split]
labels_test = labels[split:]

# Alternative Solution
train = rows[:split]
test = rows[split:]
features_train = [row[0:4] for row in train]
features_test = [row[0:4] for row in test]
labels_train = [row[4] for row in train]
labels_test = [row[4] for row in test]

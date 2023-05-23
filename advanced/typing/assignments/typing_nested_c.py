"""
* Assignment: Typing Annotations List of Dict
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Declare proper types for variable
    2. Run doctests - all must succeed

Polish:
    1. Zadeklaruj odpowiedni typ zmiennej
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert data == [
    ...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
    ...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
    ...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ... ], \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare proper types for variable
data: ...

# Do not modify lines below
data = [
    {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
    {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
    {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
]

# Solution
data: list[dict[str, str|list[float]]]

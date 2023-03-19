"""
* Assignment: Sequence List Many
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Create list `a` with data from row 1
    2. Create list `b` with data from row 2
    3. Create list `c` with data from row 3
    4. Rewrite data manually:
        a. Do not automate by writing code
        b. Do not use `str.split()`, `slice`, `getitem`, `for`, `while`
           or any other control-flow statement
        c. Objective is to learn the syntax, not automation
        d. Convert numerical values to float (manually)
    5. Run doctests - all must succeed

Polish:
    1. Stwórz listę `a` z danymi z wiersza 1
    2. Stwórz listę `b` z danymi z wiersza 2
    3. Stwórz listę `c` z danymi z wiersza 3
    4. Przepisz dane ręcznie:
        a. Nie automatyzuj pisząc kod
        b. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while`
           lub jakiejkolwiek innej instrukcji sterującej
        c. Celem jest nauka składni, a nie automatyzacja
        d. Przekonwertuj wartości numeryczne do float (ręcznie)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert type(a) is list, \
    'Variable `a` has invalid type, should be list'

    >>> assert type(b) is list, \
    'Variable `b` has invalid type, should be list'
    >>> assert type(c) is list, \
    'Variable `c` has invalid type, should be list'
    >>> assert len(a) == 5, \
    'Variable `a` length should be 5'
    >>> assert len(b) == 5, \
    'Variable `b` length should be 5'
    >>> assert len(c) == 5, \
    'Variable `c` length should be 5'

    >>> assert (5.8 in a
    ...     and 2.7 in a
    ...     and 5.1 in a
    ...     and 1.9 in a
    ...     and 'virginica' in a)

    >>> assert (5.1 in b
    ...     and 3.5 in b
    ...     and 1.4 in b
    ...     and 0.2 in b
    ...     and 'setosa' in b)

    >>> assert (5.7 in c
    ...     and 2.8 in c
    ...     and 4.1 in c
    ...     and 1.3 in c
    ...     and 'versicolor' in c)
"""

DATA = ['sepal_length,sepal_width,petal_length,petal_width,species',
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
        '6.3,2.9,5.6,1.8,virginica',
        '6.4,3.2,4.5,1.5,versicolor']

# With data from row[1]: 5.8, 2.7, 5.1, 1.9 and virginica
# type: list[float|str]
a = ...

# With data from row[2]: 5.1, 3.5, 1.4, 0.2 and setosa
# type: list[float|str]
b = ...

# With data from row[3]: 5.7, 2.8, 4.1, 1.3 and versicolor
# type: list[float|str]
c = ...

# Solution
a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']

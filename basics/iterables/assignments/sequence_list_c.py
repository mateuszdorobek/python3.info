"""
* Assignment: Iterable List Modify
* Type: homework
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Insert at the beginning of `a` letter 'x'
    2. Append to the `b` last element popped from `a`
    3. For getting elements use `list.pop()`
    4. From list `c` using `del` delete last element
    5. Run doctests - all must succeed

Polish:
    1. Na początek `a` wstaw literę 'x'
    2. Na koniec `b` wstaw ostatni element wyciągnięty z `a`
    3. Do wyciągnięcia używaj `list.pop()`
    4. Z listy `c` za pomocą `del` usuń ostatni element
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

    >>> a
    ['x', 4.7, 3.2, 1.3, 0.2]
    >>> b
    [7.0, 3.2, 4.7, 1.4, 'versicolor', 'setosa']
    >>> c
    [7.6, 3.0, 6.6, 2.1]
"""

a = [4.7, 3.2, 1.3, 0.2, 'setosa']
b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
c = [7.6, 3.0, 6.6, 2.1, 'virginica']

# insert at the beginning of `a` letter 'x'
...

# append to the `b` last element popped from `a`
# for getting elements use `list.pop()`
...

# from list `c` using `del` delete last element
...

# Solution
a.insert(0, 'x')
b.append(a.pop())
del c[4]

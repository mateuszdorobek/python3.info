"""
* Assignment: Performance Compexity Segmentation
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 5 min

English:
    1. Count occurrences of each group
    2. Define groups:
        a. `small` - numbers in range [0-3)
        b. `medium` - numbers in range [3-7)
        c. `large` - numbers in range [7-10)
    3. Print `result: dict[str, int]`:
        a. key - group
        b. value - number of occurrences
    4. Run doctests - all must succeed

Polish:
    1. Policz wystąpienia każdej z group
    2. Zdefiniuj grupy
        a. `small` - liczby z przedziału <0-3)
        b. `medium` - liczby z przedziału <3-7)
        c. `large` - liczby z przedziału <7-10)
    3. Wypisz `result: dict[str, int]`:
        a. klucz - grupa
        b. wartość - liczba wystąpień
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())

    >>> result
    {'small': 16, 'medium': 19, 'large': 15}
"""

DATA = [
    1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
    0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
    2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
    1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
    4, 8, 1, 9, 6, 3,
]

# dict[str,int] number of digit occurrences in segments
result = {'small': 0, 'medium': 0, 'large': 0}

# Solution
SMALL = {0, 1, 2}
MEDIUM = {3, 4, 5, 6}
LARGE = {7, 8, 9}

for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# Alternative Solution
"""
# 7.14 µs ± 765 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if 0 <= digit < 3:
        result['small'] += 1
    elif 3 <= digit < 7:
        result['medium'] += 1
    elif 7 <= digit < 10:
        result['large'] += 1


# 5.24 µs ± 633 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit < 3:
        result['small'] += 1
    elif digit < 7:
        result['medium'] += 1
    elif digit < 10:
        result['large'] += 1


# 5.09 µs ± 809 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit < 3:
        result['small'] += 1
    elif digit < 7:
        result['medium'] += 1
    else:
        result['large'] += 1


# 7.03 µs ± 1.04 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit in [0,1,2]:
        result['small'] += 1
    elif digit in [3,4,5,6]:
        result['medium'] += 1
    elif digit in [7,8,9]:
        result['large'] += 1

# 6.72 µs ± 897 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit in (0,1,2):
        result['small'] += 1
    elif digit in (3,4,5,6):
        result['medium'] += 1
    elif digit in (7,8,9):
        result['large'] += 1


# 5.26 µs ± 666 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit in {0,1,2}:
        result['small'] += 1
    elif digit in {3,4,5,6}:
        result['medium'] += 1
    elif digit in {7,8,9}:
        result['large'] += 1


# 19.7 µs ± 2.07 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
for digit in DATA:
    if digit in range(0, 3):
        result['small'] += 1
    elif digit in range(3, 7):
        result['medium'] += 1
    elif digit in range(7, 10):
        result['large'] += 1



# 7.14 µs ± 823 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = [0,1,2]
MEDIUM = [3,4,5,6]
LARGE = [7,8,9]
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# 6.76 µs ± 670 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = (0,1,2)
MEDIUM = (3,4,5,6)
LARGE = (7,8,9)
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1


# 7.04 µs ± 1.2 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = {0,1,2}
MEDIUM = {3,4,5,6}
LARGE = {7,8,9}
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# 8.69 µs ± 908 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = range(0, 3)
MEDIUM = range(3, 7)
LARGE = range(7, 10)
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1


# 6.58 µs ± 647 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = {x for x in range(0, 3)}
MEDIUM = {x for x in range(3, 7)}
LARGE = {x for x in range(7, 10)}
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1


# 7.99 µs ± 886 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = [x for x in range(0, 3)]
MEDIUM = [x for x in range(3, 7)]
LARGE = [x for x in range(7, 10)]
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1


# 5.65 µs ± 682 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = (x for x in range(0, 3))
MEDIUM = (x for x in range(3, 7))
LARGE = (x for x in range(7, 10))
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1


# 6.13 µs ± 700 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = {x for x in {0,1,2}}
MEDIUM = {x for x in {3,4,5,6}}
LARGE = {x for x in {7,8,9}}
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# 7.82 µs ± 876 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = [x for x in [0,1,2]]
MEDIUM = [x for x in [3,4,5,6]]
LARGE = [x for x in [7,8,9]]
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

# 5.04 µs ± 568 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = {'small': 0, 'medium': 0, 'large': 0}
SMALL = (x for x in (0,1,2))
MEDIUM = (x for x in (3,4,5,6))
LARGE = (x for x in (7,8,9))
for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1
"""

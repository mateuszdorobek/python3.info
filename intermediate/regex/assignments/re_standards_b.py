"""
* Assignment: RE Standards IsPeselWoman
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Write implementation of `is_pesel_woman`:
       a. Pesel belongs to a woman if second to last digit is even
       b. Do not use regex
    2. Run doctests - all must succeed

Polish:
    1. Napisz implementację `is_pesel_woman`:
       a. Pesel należy do kobiety, jeżeli przed ostatnia cyfra jest parzysta
       a. Nie korzystaj z regex
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_pesel_woman(69072101234)
    False
    >>> is_pesel_woman(18220812345)
    True
"""

PATTERN = r'^\d{11}$'
WOMAN = {0,2,4,6,8}
MAN = {1,3,5,7,9}


# type: Callable[[int], bool]
def is_pesel_woman(pesel):
    """
    Check whether PESEL is woman's.
    If the second to last number is even,
    then PESEL is woman's, in other case PESEL is man's.
    """
    ...


# Solution
def is_pesel_woman(pesel):
    pesel = str(pesel)
    gender_digit = int(pesel[-2])
    return gender_digit in WOMAN

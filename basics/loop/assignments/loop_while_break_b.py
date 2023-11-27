"""
* Assignment: Loop While Input
* Type: homework
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Define `grades: list[float]`
    2. Using `input()` ask user about grade, one at a time
    3. User will type only valid `int` or `float`
    4. To iterate use only `while` loop
    5. If grade is in `GRADE_SCALE` - add it to `grades`
    6. If grade is not in `GRADE_SCALE`, skip this iteration
    7. If user pressed Enter key, end inserting data
    8. Define `result: float` with arithmetic mean of `grades`
    9. Test case when report list is empty
    10. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `grades: list[float]`
    2. Do iterowania użyj tylko pętli `while`
    3. Używając `input()` poproś użytkownika o ocenę, jedną na raz
    4. Użytkownik poda tylko poprawne `int` lub `float`
    5. Jeżeli ocena jest w `GRADE_SCALE` - dodaj ją do `grades`
    6. Jeżeli oceny nie ma w `GRADE_SCALE`, pomiń tą iterację
    7. Jeżeli użytkownik wcisnął Enter, zakończ wprowadzanie danych
    8. Zdefiniuj `result: float` ze średnią arytmetyczą `grades`
    9. Przetestuj przypadek, gdy dzienniczek jest pusty
    10. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop
    * `mean = sum(...) / len(...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from statistics import mean

    >>> type(grades)
    <class 'list'>
    >>> type(result)
    <class 'float'>

    >>> assert all(type(x) is float for x in grades)

    >>> mean(grades) == result  # doctest: +SKIP
    True

    >>> result
    3.5
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['1', '2', '2.5', '3', '3.5', '4', '5', '6', ''])

GRADE_SCALE = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)

# All user grades
# type: list[float]
grades = ...

# Arithmetic mean of grades
# type: float
result = ...

# Solution
grades = []

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        grades.append(grade)

if grades:
    result = sum(grades) / len(grades)

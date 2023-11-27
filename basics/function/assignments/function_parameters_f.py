"""
* Assignment: Function Parameters BloodPressure
* Type: class assignment
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Table contains Blood Pressure classification according to American Heart Association [1]
    2. User inputs blood pressure in `XXX/YY` or `XXX/YYY` format
    3. User will not try to input invalid data
    4. Data format:
        a. `XXX: int` systolic pressure
        b. `YY: int` or `YYY: int` diastolic pressure
    5. Print status of given blood pressure
    6. If systolic and diastolic values are in different categories, assume worst case
    7. Run doctests - all must succeed

Polish:
    1. Tabela zawiera klasyfikację ciśnienia krwi wg American Heart Association [1]
    2. Użytkownik wprowadza ciśnienie krwi w formacie `XXX/YY` lub `XXX/YYY`
    3. Użytkownik nie będzie próbował wprowadzać danych niepoprawnych
    4. Format danych:
        a. `XXX: int` to wartość ciśnienia skurczowego (ang. systolic)
        b. `YY: int` lub `YYY: int` to wartość ciśnienia rozkurczowego (ang. diastolic)
    5. Wypisz status wprowadzonego ciśnienia krwi
    6. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek
    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `and`
    * `or`

References:
    [1] Whelton, Paul K. and et al.
        2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the
        Prevention, Detection, Evaluation, and Management of High Blood Pressure
        in Adults: Executive Summary: A Report of the American College of
        Cardiology/American Heart Association Task Force on Clinical Practice Guidelines.
        Journal of Hypertension. vol 71. pages 1269–1324. 2018. doi: 10.1161/HYP.0000000000000066

Tests:
    TODO: Better Tests

    >>> import sys; sys.tracebacklimit = 0
    >>> result = blood_pressure(0,0)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result in (STATUS_NORMAL, STATUS_ELEVATED, STATUS_HYPERTENSION_STAGE_1,
    ...            STATUS_HYPERTENSION_STAGE_2, STATUS_HYPERTENSIVE_CRISIS)
    True

    >>> blood_pressure(115, 75)
    'Normal'
    >>> blood_pressure(125, 75)
    'Elevated'
    >>> blood_pressure(135, 85)
    'Hypertension stage 1'
    >>> blood_pressure(145, 95)
    'Hypertension stage 2'
    >>> blood_pressure(195, 135)
    'Hypertensive Crisis'

    >>> blood_pressure(119, 0)
    'Normal'
    >>> blood_pressure(120, 0)
    'Elevated'
    >>> blood_pressure(0, 79)
    'Normal'
    >>> blood_pressure(0, 80)
    'Hypertension stage 1'
    >>> blood_pressure(120, 80)
    'Hypertension stage 1'

    >>> blood_pressure(129, 0)
    'Elevated'
    >>> blood_pressure(130, 0)
    'Hypertension stage 1'
    >>> blood_pressure(0, 79)
    'Normal'
    >>> blood_pressure(0, 80)
    'Hypertension stage 1'
    >>> blood_pressure(130, 80)
    'Hypertension stage 1'

    >>> blood_pressure(139, 0)
    'Hypertension stage 1'
    >>> blood_pressure(140, 0)
    'Hypertension stage 2'
    >>> blood_pressure(0, 89)
    'Hypertension stage 1'
    >>> blood_pressure(0, 90)
    'Hypertension stage 2'
    >>> blood_pressure(140, 90)
    'Hypertension stage 2'

    >>> blood_pressure(180, 0)
    'Hypertension stage 2'
    >>> blood_pressure(181, 0)
    'Hypertensive Crisis'
    >>> blood_pressure(0, 120)
    'Hypertension stage 2'
    >>> blood_pressure(0, 121)
    'Hypertensive Crisis'
    >>> blood_pressure(181, 121)
    'Hypertensive Crisis'
"""

STATUS_NORMAL = 'Normal'
STATUS_ELEVATED = 'Elevated'
STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'

# | Blood Pressure Category | Systolic [mm Hg] | Operator | Diastolic [mm Hg] |
# |-------------------------|------------------|----------|-------------------|
# | Normal                  | Less than 120    | and      | Less than 80      |
# | Elevated                | 120-129          | and      | Less than 80      |
# | Hypertension stage 1    | 130-139          | or       | 80-89             |
# | Hypertension stage 2    | 140 or higher    | or       | 90 or higher      |
# | Hypertensive Crisis     | Higher than 180  | and/or   | Higher than 120   |

# One of the STATUS_*
# type: Callable[[int,int], str]
def blood_pressure(systolic, diastolic):
    return ...


# Solution
def blood_pressure(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        result = STATUS_NORMAL
    elif 120 <= systolic <= 129 and diastolic < 80:
        result = STATUS_ELEVATED
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        result = STATUS_HYPERTENSION_STAGE_1
    elif 140 <= systolic or 90 <= diastolic:
        result = STATUS_HYPERTENSION_STAGE_2
    if 180 < systolic or 120 < diastolic:
        result = STATUS_HYPERTENSIVE_CRISIS
    return result


# Alternative Solution
def blood_pressure(systolic, diastolic):
    NORMAL = systolic < 120 and diastolic < 80
    ELEVATED = 120 <= systolic <= 129 and diastolic < 80
    STAGE1 = 130 <= systolic <= 139 or 80 <= diastolic <= 89
    STAGE2 = systolic >= 140 or diastolic >= 90
    CRISIS = systolic > 180 or diastolic > 120
    if NORMAL: result = STATUS_NORMAL
    elif ELEVATED: result = STATUS_ELEVATED
    elif STAGE1: result = STATUS_HYPERTENSION_STAGE_1
    elif STAGE2: result = STATUS_HYPERTENSION_STAGE_2
    if CRISIS: result = STATUS_HYPERTENSIVE_CRISIS
    return result

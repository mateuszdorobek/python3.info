"""
* Assignment: CSV DictWriter Fixed
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Using `csv.DictWriter()` save `DATA` to `FILE`
    2. Open file in your spreadsheet program like:
       Microsoft Excel, Libre Office or Numbers etc.
    3. Open file in simple in your IDE and simple text editor like:
       Notepad, vim, gedit
    4. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        d. Use Unix `\n` line terminator
    5. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz `DATA` do `FILE`
    2. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj.
       Microsoft Excel, Libre Office lub Numbers itp
    3. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj.
       Notepad, vim lub gedit
    4. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        d. Użyj zakończenia linii Unix `\n`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)   # doctest: +NORMALIZE_WHITESPACE
    "firstname","lastname","age"
    "Mark","Watney","42"
    "Melissa","Lewis","41"
    "Rick","Martinez","40"
    "Alex","Vogel","42"
    "Beth","Johanssen","29"
    "Chris","Beck","36"
    <BLANKLINE>
"""
import csv


DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'age': 42},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 41},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'age': 40},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'age': 42},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'age': 29},
    {'firstname': 'Chris', 'lastname': 'Beck', 'age': 36},
]

FILE = r'_temporary.csv'

# Write DATA to FILE, generate header from DATA
# type: ContextManager
with open(FILE, mode='w') as file:
    ...


# Solution
with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=['firstname', 'lastname', 'age'],
                          delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,
                          lineterminator='\n')

    writer.writeheader()
    writer.writerows(DATA)

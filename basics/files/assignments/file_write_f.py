"""
* Assignment: File Write CSV
* Required: yes
* Complexity: medium
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Separate header from data
    2. Write data to file `FILE`:
        a. First line in file must be a header (first line of `DATA`)
        b. For each row, convert it's values to `str`
        c. Use coma (`,`) as a value separator
        d. Add line terminator (`\n`) to each row
        e. Save row values to file
    8. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od danych
    2. Zapisz dane do pliku `FILE`:
        a. Pierwsza linia w pliku musi być nagłówkiem (pierwsza linia `DATA`)
        b. Dla każdego wiersza przekonwertuj jego wartości do `str`
        c. Użyj przecinka (`,`) jako separatora wartości
        d. Użyj `\n` jako koniec linii w każdym wierszu
        e. Zapisz do pliku wartości z wiersza
    8. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `','.join(...)`
    * `[str(x) for x in ...]`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    <BLANKLINE>
"""

FILE = '_temporary.csv'
DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# Solution
data = []
for row in DATA:
    row = ','.join(str(x) for x in row)
    data.append(row + '\n')

with open(FILE, mode='w') as file:
    file.writelines(data)

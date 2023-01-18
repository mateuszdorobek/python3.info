"""
* Assignment: RE Syntax Patterns
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use regular expressions find in text
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście
    2. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14
"""

import re

TEXT = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named Tranquility
Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg)
of lunar material to bring back to Earth as pilot Michael Collins (CMP)
flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""


# Find all digits in text
# Example: '1', '1', '2', '0', '1', '9', '6', ...
# type: list[str]
result_a = re.findall(r'[0-9]', TEXT)
['1', '1', '2', '0', '1', '9', '6', '9', '2', '0', '1', '7', '6', '3', '9', '2', '1', '1', '9', '6', '9', '0', '2', '5', '6', '1', '9', '2', '3', '1', '4', '7', '5', '2', '1', '5', '2', '1', '3', '6']

# Find all uppercase letters in text
# Example: 'A', 'A', 'M', 'C', 'C', 'D', 'R', ...
# type: list[str]
result_b = re.findall(r'[A-Z]', TEXT)
['A', 'A', 'M', 'C', 'C', 'D', 'R', 'N', 'A', 'L', 'M', 'P', 'B', 'A', 'A', 'L', 'M', 'L', 'M', 'E', 'J', 'U', 'T', 'C', 'A', 'E', 'V', 'A', 'M', 'E', 'V', 'A', 'J', 'U', 'T', 'C', 'A', 'T', 'T', 'B', 'A', 'A', 'E', 'M', 'C', 'C', 'M', 'P', 'C', 'M', 'C', 'M', 'C', 'M', 'C']

# Find all lowercase letters in text
# Example: 'p', 'o', 'l', 'l', 'o', ...
# type: list[str]
result_b = re.findall(r'[a-z]', TEXT)
['p', 'o', 'l', 'l', 'o', 'w', 'a', 's', 't', 'h', 'e', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 's', 'p', 'a', 'c', 'e', 'f', 'l', 'i', 'g', 'h', 't', 't', 'h', 'a', 't', 'f', 'i', 'r', 's', 't', 'l', 'a', 'n', 'd', 'e', 'd', 'h', 'u', 'm', 'a', 'n', 's', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 'o', 'm', 'm', 'a', 'n', 'd', 'e', 'r', 'e', 'i', 'l', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'u', 'n', 'a', 'r', 'm', 'o', 'd', 'u', 'l', 'e', 'p', 'i', 'l', 'o', 't', 'u', 'z', 'z', 'l', 'd', 'r', 'i', 'n', 'l', 'a', 'n', 'd', 'e', 'd', 't', 'h', 'e', 'p', 'o', 'l', 'l', 'o', 'u', 'n', 'a', 'r', 'o', 'd', 'u', 'l', 'e', 'a', 'g', 'l', 'e', 'o', 'n', 'u', 'l', 'y', 'a', 't', 'a', 'n', 'd', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'b', 'e', 'c', 'a', 'm', 'e', 't', 'h', 'e', 'f', 'i', 'r', 's', 't', 'p', 'e', 'r', 's', 'o', 'n', 't', 'o', 's', 't', 'e', 'p', 'o', 'n', 't', 'o', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'o', 'n', 'u', 'l', 'y', 'a', 't', 'l', 'd', 'r', 'i', 'n', 'j', 'o', 'i', 'n', 'e', 'd', 'h', 'i', 'm', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'h', 'e', 'y', 's', 'p', 'e', 'n', 't', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'e', 'x', 'p', 'l', 'o', 'r', 'i', 'n', 'g', 't', 'h', 'e', 's', 'i', 't', 'e', 't', 'h', 'e', 'y', 'h', 'a', 'd', 'n', 'a', 'm', 'e', 'd', 'r', 'a', 'n', 'q', 'u', 'i', 'l', 'i', 't', 'y', 'a', 's', 'e', 'u', 'p', 'o', 'n', 'l', 'a', 'n', 'd', 'i', 'n', 'g', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'd', 'r', 'i', 'n', 'c', 'o', 'l', 'l', 'e', 'c', 't', 'e', 'd', 'p', 'o', 'u', 'n', 'd', 's', 'k', 'g', 'o', 'f', 'l', 'u', 'n', 'a', 'r', 'm', 'a', 't', 'e', 'r', 'i', 'a', 'l', 't', 'o', 'b', 'r', 'i', 'n', 'g', 'b', 'a', 'c', 'k', 't', 'o', 'a', 'r', 't', 'h', 'a', 's', 'p', 'i', 'l', 'o', 't', 'i', 'c', 'h', 'a', 'e', 'l', 'o', 'l', 'l', 'i', 'n', 's', 'f', 'l', 'e', 'w', 't', 'h', 'e', 'o', 'm', 'm', 'a', 'n', 'd', 'o', 'd', 'u', 'l', 'e', 'o', 'l', 'u', 'm', 'b', 'i', 'a', 'i', 'n', 'l', 'u', 'n', 'a', 'r', 'o', 'r', 'b', 'i', 't', 'a', 'n', 'd', 'w', 'e', 'r', 'e', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'f', 'o', 'r', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'l', 'i', 'f', 't', 'i', 'n', 'g', 'o', 'f', 'f', 't', 'o', 'r', 'e', 'j', 'o', 'i', 'n', 'o', 'l', 'u', 'm', 'b', 'i', 'a']

# Find all digits and lowercase letters in text
# Example: 'p', 'o', 'l', 'l', 'o', '1', '1', ...
# type: list[str]
result_b = re.findall(r'[a-z0-9]', TEXT)
['p', 'o', 'l', 'l', 'o', '1', '1', 'w', 'a', 's', 't', 'h', 'e', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 's', 'p', 'a', 'c', 'e', 'f', 'l', 'i', 'g', 'h', 't', 't', 'h', 'a', 't', 'f', 'i', 'r', 's', 't', 'l', 'a', 'n', 'd', 'e', 'd', 'h', 'u', 'm', 'a', 'n', 's', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 'o', 'm', 'm', 'a', 'n', 'd', 'e', 'r', 'e', 'i', 'l', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'u', 'n', 'a', 'r', 'm', 'o', 'd', 'u', 'l', 'e', 'p', 'i', 'l', 'o', 't', 'u', 'z', 'z', 'l', 'd', 'r', 'i', 'n', 'l', 'a', 'n', 'd', 'e', 'd', 't', 'h', 'e', 'p', 'o', 'l', 'l', 'o', 'u', 'n', 'a', 'r', 'o', 'd', 'u', 'l', 'e', 'a', 'g', 'l', 'e', 'o', 'n', 'u', 'l', 'y', '2', '0', 't', 'h', '1', '9', '6', '9', 'a', 't', '2', '0', '1', '7', 'a', 'n', 'd', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'b', 'e', 'c', 'a', 'm', 'e', 't', 'h', 'e', 'f', 'i', 'r', 's', 't', 'p', 'e', 'r', 's', 'o', 'n', 't', 'o', 's', 't', 'e', 'p', 'o', 'n', 't', 'o', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', '6', 'h', 'o', 'u', 'r', 's', '3', '9', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'o', 'n', 'u', 'l', 'y', '2', '1', 's', 't', '1', '9', '6', '9', 'a', 't', '0', '2', '5', '6', '1', '5', 'l', 'd', 'r', 'i', 'n', 'j', 'o', 'i', 'n', 'e', 'd', 'h', 'i', 'm', '1', '9', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'h', 'e', 'y', 's', 'p', 'e', 'n', 't', '2', 'h', 'o', 'u', 'r', 's', '3', '1', 'm', 'i', 'n', 'u', 't', 'e', 's', 'e', 'x', 'p', 'l', 'o', 'r', 'i', 'n', 'g', 't', 'h', 'e', 's', 'i', 't', 'e', 't', 'h', 'e', 'y', 'h', 'a', 'd', 'n', 'a', 'm', 'e', 'd', 'r', 'a', 'n', 'q', 'u', 'i', 'l', 'i', 't', 'y', 'a', 's', 'e', 'u', 'p', 'o', 'n', 'l', 'a', 'n', 'd', 'i', 'n', 'g', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'd', 'r', 'i', 'n', 'c', 'o', 'l', 'l', 'e', 'c', 't', 'e', 'd', '4', '7', '5', 'p', 'o', 'u', 'n', 'd', 's', '2', '1', '5', 'k', 'g', 'o', 'f', 'l', 'u', 'n', 'a', 'r', 'm', 'a', 't', 'e', 'r', 'i', 'a', 'l', 't', 'o', 'b', 'r', 'i', 'n', 'g', 'b', 'a', 'c', 'k', 't', 'o', 'a', 'r', 't', 'h', 'a', 's', 'p', 'i', 'l', 'o', 't', 'i', 'c', 'h', 'a', 'e', 'l', 'o', 'l', 'l', 'i', 'n', 's', 'f', 'l', 'e', 'w', 't', 'h', 'e', 'o', 'm', 'm', 'a', 'n', 'd', 'o', 'd', 'u', 'l', 'e', 'o', 'l', 'u', 'm', 'b', 'i', 'a', 'i', 'n', 'l', 'u', 'n', 'a', 'r', 'o', 'r', 'b', 'i', 't', 'a', 'n', 'd', 'w', 'e', 'r', 'e', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'f', 'o', 'r', '2', '1', 'h', 'o', 'u', 'r', 's', '3', '6', 'm', 'i', 'n', 'u', 't', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'l', 'i', 'f', 't', 'i', 'n', 'g', 'o', 'f', 'f', 't', 'o', 'r', 'e', 'j', 'o', 'i', 'n', 'o', 'l', 'u', 'm', 'b', 'i', 'a']


# Find uppercase letter at the beginning of a line
# Example: 'A'
# type: list[str]
result_b = re.findall(r'^[A-Z]', TEXT)
['A']

# Find uppercase letter at the beginning of each line
# Example: 'A', 'C', 'T'
# type: list[str]
result_b = re.findall(r'^[A-Z]', TEXT, flags=re.MULTILINE)
['A', 'C', 'T']

# Find unique: non-letters and non-digit characters
# Example: '\n', ' ', "'", '(', ')', ',', '.', ':'
# type: list[str]
result_b = set(re.findall(r'[^a-zA-Z0-9]', TEXT))
{'\n', ' ', "'", '(', ')', ',', '.', ':'}

# Find any character at the beginning of a text
# Example: 'A'
# type: list[str]
result_b = re.findall(r'\A.', TEXT)
['A']

# Find any character at the beginning of each line
# Example: 'A', 'C', 'T'
# type: list[str]
result_b = re.findall(r'^.', TEXT, flags=re.MULTILINE)
['A', 'C', 'T']

# Find any character at the end of a line
# Example: '.'
# type: list[str]
result_b = re.findall(r'.\Z', TEXT, flags=re.MULTILINE)
['.']

# Find any character at the end of each line
# Example: ' ', ' ', '.'
# type: list[str]
result_b = re.findall(r'.$', TEXT, flags=re.MULTILINE)
[' ', ' ', '.']


# Find all three letter acronyms in text (standalone word with three capitalized letters)
# Example: 'CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP'
# type: list[str]
result_b = re.findall(r'[A-Z]{3}', TEXT)
['CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP']

# Find all integers in text (as long as possible)
# Example: '11', '20', '1969', ...
# type: list[str]
result_b = re.findall(r'[0-9]+', TEXT)
['11', '20', '1969', '20', '17', '6', '39', '21', '1969', '02', '56', '19', '2', '31', '47', '5', '21', '5', '21', '36']

# Find all times in text
# Example: '20:17', '02:56'
# type: list[str]
result_b = re.findall(r'[0-9]+:[0-9]+', TEXT)
['20:17', '02:56']

# Find all floats in text
# Example: '47.5', '21.5'
# type: list[str]
result_b = re.findall(r'[0-9]+\.[0-9]+', TEXT)
['47.5', '21.5']


# Find unique whitespace characters in text
# Example: '\n', ' '
# type: list[str]
result_b = set(re.findall(r'\s', TEXT))
{'\n', ' '}

# Find unique digits in text
# Example: '0', '1', '2', '3', '4', '5', '6', '7', '9'
# type: list[str]
result_b = set(re.findall(r'\d', TEXT))
{'0', '1', '2', '3', '4', '5', '6', '7', '9'}

# Find unique word characters in text
# Example: 'g', '9', 'w', 'J', 'E', '5', 'f', ...
# type: list[str]
result_b = set(re.findall(r'\w', TEXT))
{'g', '9', 'w', 'J', 'E', '5', 'f', 'x', 't', 'p', 'C', 'R', 'k', 'q', '4', 'c', '3', 'b', 's', 'j', 'n', 'a', 'N', 'u', 'V', 'U', 'z', 'i', 'e', 'P', '0', '1', 'd', 'M', 'L', 'm', 'D', 'B', 'T', 'h', '2', '7', 'r', '6', 'A', 'o', 'l', 'y'}


# Find unique non-word (special) characters in text
# Example: '\n', ' ', "'", '(', ')', ',', '.', ':'
# type: list[str]
result_b = set(re.findall(r'\W', TEXT))
{'\n', ' ', "'", '(', ')', ',', '.', ':'}

# Find all capitalized words
# Example: 'Apollo', 'Moon', 'Commander', 'Neil', 'Armstrong', ...
# type: list[str]
result_b = re.findall(r'[A-Z][a-z]+', TEXT)
['Apollo', 'American', 'Moon', 'Commander', 'Neil', 'Armstrong', 'Buzz', 'Aldrin', 'Apollo', 'Lunar', 'Module', 'Eagle', 'July', 'Armstrong', 'Moon', 'July', 'Aldrin', 'They', 'Tranquility', 'Base', 'Armstrong', 'Aldrin', 'Earth', 'Michael', 'Collins', 'Command', 'Module', 'Columbia', 'Moon', 'Columbia']

# Find all names (two capitalized words) in text
# Example: 'Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Tranquility Base', ...
# type: list[str]
result_b = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', TEXT)
['Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Tranquility Base', 'Michael Collins', 'Command Module']

# Find all names with numbers (capitalized word followed by number)
# Example: 'Apollo 11', 'July 20', 'July 21'
# type: list[str]
result_b = re.findall(r'[A-Z][a-z]+ [0-9]+', TEXT)
['Apollo 11', 'July 20', 'July 21']

# Find all dates in US long format
# Example: 'July 20, 1969', 'July 21, 1969'
# type: list[str]
result_b = re.findall(r'[A-Z][a-z]+ [0-9]+, [0-9]+', TEXT)
['July 20, 1969', 'July 21, 1969']

# Find all dates (month name followed by day number)
# Example: 'July 20', 'July 21'
# type: list[str]
result_b = re.findall(r'([A-Z][a-z]+ [0-9]+),', TEXT)
['July 20', 'July 21']

# Find all durations in text
# Example: '6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes'
# type: list[str]
result_b = re.findall(r'[0-9]+ hours [0-9]+ minutes', TEXT)
['6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes']

# Find all two-letter conjunctives in text (two-letter words)
# Example: 'on', 'on', 'at', 'to', ...
# type: list[str]
result_b = re.findall(r'\b[a-z]{2}\b', TEXT)
['on', 'on', 'at', 'to', 'on', 'at', 'kg', 'of', 'to', 'to', 'as', 'in', 'on', 'to']

# Find all three-letter conjunctives in text (three-letter words)
# Example: 'was', 'the', 'the', 'and', ...
# type: list[str]
result_b = re.findall(r'\b[a-z]{3}\b', TEXT)
['was', 'the', 'the', 'and', 'the', 'and', 'the', 'the', 'him', 'the', 'had', 'and', 'the', 'and', 'the', 'for', 'off']

# Find all conjunctives in text (both two- and three-letter words)
# Example: 'was', 'the', 'on', 'the', 'and', ...
# type: list[str]
result_b = re.findall(r'\b[a-z]{2,3}\b', TEXT)
['was', 'the', 'on', 'the', 'and', 'the', 'on', 'at', 'and', 'the', 'to', 'the', 'on', 'at', 'him', 'the', 'had', 'and', 'kg', 'of', 'to', 'to', 'as', 'the', 'in', 'and', 'on', 'the', 'for', 'off', 'to']

# Find all three letter acronyms in text (standalone word with three capitalized letters)
# Example: 'CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP'
# type: list[str]
result_b = re.findall(r'[A-Z]{3}', TEXT)
['CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP']

# Find all two letter acronyms in text (standalone word with two capitalized letters)
# Example: 'LM', 'CM'
# type: list[str]
result_b = re.findall(r'\b[A-Z]{2}\b', TEXT)
['LM', 'CM']

# Find all acronyms in text (standalone words with two or three capitalized letters)
# Example: 'CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM'
# type: list[str]
result_b = re.findall(r'\b[A-Z]{2,3}\b', TEXT)
['CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM']

# Extract duration values from text in list[tuple] format
# Example: ('6', '39'), ('2', '31'), ('21', '36')
# type: list[str]
result_b = re.findall(r'(?P<hours>[0-9]+) hours (?P<minutes>[0-9]+) minutes', TEXT)
[('6', '39'), ('2', '31'), ('21', '36')]

# Extract duration values from text in list[dict] format
# Example: [{'hours': '6', 'minutes': '39'}, {'hours': '2', 'minutes': '31'}, ...]
# type: list[str]
data = re.finditer(r'(?P<hours>[0-9]+) hours (?P<minutes>[0-9]+) minutes', TEXT)
result = [x.groupdict() for x in data]
[{'hours': '6', 'minutes': '39'},
 {'hours': '2', 'minutes': '31'},
 {'hours': '21', 'minutes': '36'}]



# Solution

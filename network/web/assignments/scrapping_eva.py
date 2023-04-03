"""
>>> result[:5]  # doctest: +NORMALIZE_WHITESPACE
[{'Number': 1, 'ISS': '', 'Mission': 'Voskhod 2', 'Participants': 'Alexi Leonov', 'Duration': '23m', 'Date': datetime.date(1965, 3, 18), 'Notes': 'First spacewalk'},
 {'Number': 2, 'ISS': '', 'Mission': 'Gemini IV', 'Participants': 'Edward White, James McDivitt', 'Duration': '46m', 'Date': datetime.date(1966, 6, 3), 'Notes': None},
 {'Number': 3, 'ISS': '', 'Mission': 'Gemini IX-A', 'Participants': 'Eugene Cernan, Thomas Stafford', 'Duration': '2h 8m', 'Date': datetime.date(1966, 6, 5), 'Notes': 'No egress by Stafford'},
 {'Number': 4, 'ISS': '', 'Mission': 'Gemini X', 'Participants': 'Michael Collins, John Young', 'Duration': '50m', 'Date': datetime.date(1966, 7, 19), 'Notes': 'No egress by Young'},
 {'Number': 5, 'ISS': '', 'Mission': 'Gemini X', 'Participants': 'Michael Collins, John Young', 'Duration': '40m', 'Date': datetime.date(1966, 7, 20), 'Notes': 'No egress by Young'}]
"""

from pathlib import Path
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


DATA = 'https://python3.info/_static/astro-eva.html'
# DATA = 'https://www.worldspaceflight.com/bios/eva/eva.php'


BASE_DIR = Path(__file__).parent.parent.parent.parent
FILE_HTML = BASE_DIR.joinpath('_data/html/astro-eva.html')
FILE_CSV = BASE_DIR.joinpath('_data/csv/astro-eva1.csv')


# When you dump page for the first time, you can test parsing on local file
# It saves bandwidth, and speeds you development
# Then comment following `with` context manager

if not FILE_HTML.exists():
    with open(FILE_HTML, mode='w', encoding='utf-8') as file:
        response = requests.get(DATA)
        file.write(response.text)


# Parser content below

with open(FILE_HTML, mode='r', encoding='utf-8') as file:
    content = file.read()

html = BeautifulSoup(content, 'html.parser')
table = html.find_all('table')[1]


def clean_Date(text):
    try:
        return datetime.strptime(text, '%d %B %Y').date()
    except ValueError:
        return text


def clean_Number(text):
    return int(text)


def clean_ISS(text):
    if text == '\xa0':
        return ''
    return text


def clean_Mission(text):
    return text


def clean_Participants(text):
    return ', '.join(x.string for x in text)


def clean_Duration(text):
    hours, minutes = text.split(':')
    result = ''

    if int(hours) != 0:
        result += f'{hours}h '

    if int(minutes[0]) == 0:
        minutes = minutes[1]

    result += f'{minutes}m'
    return result


def clean_Notes(text):
    if text == '\xa0':
        return ''
    return text


result = []

for row in table.find_all('tr')[1:]:
    td = row.find_all('td')

    result.append({
        'Number': clean_Number(td[0].string),
        'ISS': clean_ISS(td[1].string),
        'Mission': clean_Mission(td[2].string),
        'Participants': clean_Participants(td[3].find_all('a')),
        'Duration': clean_Duration(td[4].string),
        'Date': clean_Date(td[5].string),
        'Notes': clean_Notes(td[6].string),
    })


with open(FILE_CSV, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=result[0].keys(),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in result:
        writer.writerow(row)

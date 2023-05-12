from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re

URL = 'file:///tmp/Harmonogramy_zajec.html'
GODZINY = re.compile(r'\d\d:\d\d-\d\d:\d\d')

def ma_dane(table):
    return 'Sala:' in str(table)

def get_data(table):
    content = table.find('td').contents
    if len(content) == 1:
        return [x for x in content[0] if type(x) is NavigableString]
    else:
        return [x for x in content if type(x) is NavigableString]

def is_godzina(element):
    return GODZINY.match(element) is not None

def get_nazwa(row):
    if is_godzina(row[1]):
        return None
    else:
        return row[0]

def get_prowadzacy(row):
    if is_godzina(row[1]):
        return row[0]
    else:
        return row[1]

def get_godziny(row):
    for element in row:
        if is_godzina(element):
            return element

def get_sala(row):
    for element in row:
        if element.startswith('Sala'):
            return element.removeprefix('Sala: ')

def get_plan(row):
    for element in row:
        if element.startswith('Plan'):
            return element.removeprefix('Plan: ')

def get_grupa(row):
    for element in row:
        if element.startswith('Grupa'):
            return element.removeprefix('Grupa ')

def get_semestr(row):
    for element in row:
        if element.startswith('semestr'):
            return element.removeprefix('semestr ')

def get_zajecia(zajecie):
    return {
        'nazwa': get_nazwa(zajecie),
        'prowadzacy': get_prowadzacy(zajecie),
        'godziny': get_godziny(zajecie),
        'sala': get_sala(zajecie),
        'plan': get_plan(zajecie),
        'grupa': get_grupa(zajecie),
        'semestr': get_semestr(zajecie),
    }

def run():
    html = BeautifulSoup(urlopen(URL).read(), features='lxml')
    all_tables = html.find_all('table')
    tabelka_na_dole = all_tables[2]
    tables = filter(ma_dane, all_tables[3:])
    data = map(get_data, tables)
    zajecia = map(get_zajecia, data)
    return pd.DataFrame(zajecia).convert_dtypes()


if __name__ == '__main__':
    result = run()

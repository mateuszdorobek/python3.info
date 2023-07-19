from datetime import datetime, date
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)

DATA = 'https://python3.info/_static/tablice-{voivodeship}.html'
# DATA = 'https://wptr.pl/dobazy/expind.php?w={voivodeship}'

VOIVODESHIP = {
    'B': 'podlaskie',
    'C': 'kujawsko-pomorskie',
    'D': 'dolnośląskie',
    'E': 'łódzkie',
    'F': 'lubuskie',
    'G': 'pomorskie',
    'K': 'małopolskie',
    'L': 'lubelskie',
    'N': 'warmińsko-mazurskie',
    'O': 'opolskie',
    'P': 'wielkopolskie',
    'R': 'podkarpackie',
    'S': 'śląskie',
    'T': 'świętokrzyskie',
    'W': 'mazowieckie',
    'Z': 'zachodniopomorskie',
}


def get_plates(plate) -> tuple[date, str, str]:
    since = datetime.strptime(plate.find_all('div')[0].text, '%d.%m.%Y').date()
    number = plate.find_all('div')[1].text.replace('\xa0', ' ').strip()
    text = number.split()[1]
    return since, number, text

result = []
for letter, voivodeship in VOIVODESHIP.items():
    url = DATA.format(voivodeship=letter.lower())
    resp = requests.get(url)
    html = BeautifulSoup(resp.text, features='lxml')
    plates = html.find_all('div', class_='BoxLF')
    data = (pd
        .DataFrame(
            data=map(get_plates, plates),
            columns=['registered', 'number', 'text'])
        .assign(
            letter=letter,
            voivodeship=voivodeship,
            country='Poland'))
    result.append(data)

result = pd.concat(result)

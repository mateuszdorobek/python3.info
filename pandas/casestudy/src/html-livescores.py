import pandas as pd
import requests
from bs4 import BeautifulSoup


DATA = 'https://www.livescores.com'


html = requests.get(DATA).text
html = BeautifulSoup(html, features='lxml')
tables = html.find(id='leagueTableBodyContainer')


def get(name):
    df = tables.find(attrs={'data-name': name})
    result = []
    for row in df.find_all(attrs={'data-type': 'team-data'}):
        result.append({
                'rank': int(row.find(attrs={'data-type': 'rank'}).text),
                'team': row.find(attrs={'data-type': 'name'}).text,
                'goaldiff': int(
                    row.find(attrs={'data-type': 'goaldiff'}).text),
                'points': int(row.find(attrs={'data-type': 'points'}).text),
        })
    return pd.DataFrame(result).set_index('rank')


en = get('england-premier-league-0')
es = get('spain-laliga-santander-0')
de = get('germany-bundesliga-0')
it = get('italy-serie-a-0')
fr = get('france-ligue-1-0')

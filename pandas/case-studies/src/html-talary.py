from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging


# DATA = 'https://wcn.pl/archive?q=talar+lewkowy'
DATA = 'https://python3.info/_static/talary.html'


source_code = requests.get(DATA).text
html = BeautifulSoup(source_code, features='lxml')

pagination = html.find(attrs={'class': 'pagination'})
last = pagination.find(attrs={'rel': 'last'})
last_page = int(last.get('href').split('&page=')[1])
first_page = 1

result = []

for page_number in range(first_page, last_page+1):
    url = f'{DATA}&page={page_number}'
    logging.warning(f'Fetching URL: {url}')
    df = pd.read_html(DATA)[0]
    result.append(df)


result = pd.concat(result).reset_index(drop=True)
result[['Zakończenie Aukcji', 'Data Zakończenia']] = result['Data'].str.split(':', expand=True)
result = result.drop(columns=['Data'])

result['Zakończenie Aukcji'] = result['Zakończenie Aukcji'].replace({'Zakończenie': 'W trakcie'}).apply(pd.to_datetime, errors='coerce')
result['Data Zakończenia'] = result['Data Zakończenia'].replace({'None', pd.NaT}).apply(pd.to_datetime, errors='coerce')

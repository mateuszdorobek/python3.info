"""
>>> result[:5]  # doctest: +NORMALIZE_WHITESPACE
[{'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'},
 {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'},
 {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'},
 {'sepal_length': '7.3', 'sepal_width': '2.9', 'petal_length': '6.3', 'petal_width': '1.8', 'species': 'virginica'},
 {'sepal_length': '5.6', 'sepal_width': '2.5', 'petal_length': '3.9', 'petal_width': '1.1', 'species': 'versicolor'}]"""

from bs4 import BeautifulSoup
import requests


DATA = 'https://github.com/AstroMatt/book-python/blob/master/_data/csv/iris-dirty.csv'
HEADER = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
result = []


with open('/tmp/iris-dirty.html', mode='w') as file:
    response = requests.get(DATA)
    file.write(response.text)

with open('/tmp/iris-dirty.html', mode='r') as file:
    html = BeautifulSoup(file, 'lxml')


table = html.find_all('table')[0]

table_rows = table.find_all('tr')
table_header = table_rows[0]
table_body = table_rows[1:]

species = table_header.text.split()[2:]

for cell in table_body:
    values = cell.text.split()
    values = dict(zip(HEADER, values))
    species_id = int(values['species'])
    values['species'] = species[species_id]
    result.append(values)

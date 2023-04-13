import json
from multiprocessing.connection import Client


ADDRESS = ('localhost', 6000)
PASSWORD = b'My voice is my password, verify me.'

DATA = dict(
    sepal_length=5.1,
    sepal_width=3.5,
    petal_length=1.4,
    petal_width=0.2,
    species='setosa')

data = json.dumps(DATA)

def run():
    connection = Client(ADDRESS, authkey=PASSWORD)
    connection.send(data)
    connection.send('close')
    connection.close()

# Solution

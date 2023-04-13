import json
from multiprocessing.connection import Listener


ADDRESS = ('localhost', 6000)
PASSWORD = b'My voice is my password, verify me.'


def run():
    listener = Listener(ADDRESS, authkey=PASSWORD)
    connection = listener.accept()

    while True:
        payload = connection.recv()

        if payload == 'close':
            connection.close()
            break

        data = json.loads(payload)
        print(data)

    listener.close()

# Solution

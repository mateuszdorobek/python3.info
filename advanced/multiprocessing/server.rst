Multiprocessing Server
======================


SetUp
-----
``iris.py``:

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            return self.sepal_area() + self.petal_area()


Server
------
* Obiekt nasłuchujący na połączenia ``multiprocessing-listener.py``:

.. code-block:: python

    import pickle
    from multiprocessing.connection import Listener
    from iris import Iris


    ADDRESS = ('localhost', 6000)
    PASSWORD = b'My voice is my password, verify me.'

    listener = Listener(ADDRESS, authkey=PASSWORD)
    connection = listener.accept()

    while True:
        payload = connection.recv()

        if payload == 'close':
            connection.close()
            break

        flower = pickle.loads(payload)
        area = flower.total_area()
        print(f'Area: {area}')

    listener.close()


Assignments
-----------
.. literalinclude:: assignments/multiprocessing_server.py
    :caption: :download:`Solution <assignments/multiprocessing_server.py>`
    :end-before: # Solution

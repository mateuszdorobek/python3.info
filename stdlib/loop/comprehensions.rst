Comprehensions Nesting
======================


Nested Comprehensions
---------------------
.. code-block:: python

    DATA = [
        {'lastname': 'Watney'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'firstname': 'Rick'},
        {'firstname': 'Beth', 'lastname': 'Johanssen'},
        {'firstname': 'Chris', 'lastname': 'Beck', 'born': 1961},
    ]

    fieldnames = set(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}

.. code-block:: python

    DATA = [
        {'lastname': 'Watney'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'firstname': 'Rick'},
        {'firstname': 'Beth', 'lastname': 'Johanssen'},
        {'firstname': 'Chris', 'lastname': 'Beck', 'born': 1961},
    ]

    fieldnames = set()
    fieldnames.update(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}

.. code-block:: python

    DATA = [
        {'lastname': 'Watney'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'firstname': 'Rick'},
        {'firstname': 'Beth', 'lastname': 'Johanssen'},
        {'firstname': 'Chris', 'lastname': 'Beck', 'born': 1961},
    ]

    fieldnames = set()
    fieldnames.update(key for row in DATA for key in row.keys())

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}


Generator comprehensions
------------------------
.. code-block:: python

    DATA = [
        {'lastname': 'Watney'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'firstname': 'Rick'},
        {'firstname': 'Beth', 'lastname': 'Johanssen'},
        {'firstname': 'Chris', 'lastname': 'Beck', 'born': 1961},
    ]

    fieldnames = set()

    fieldnames.add(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {<generator object <genexpr> at 0x1179a0a50>}


.. todo:: Assignments

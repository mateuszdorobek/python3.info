Basic Debugging
===============


Run in the console
------------------
* Execute cell
* Run File in the console


``print``
---------
.. code-block:: python

    DATA = ['a', 'b', 'c', [1, 2, 3]]

    for element in DATA:
        print(element)
        # a
        # b
        # c
        # [1, 2, 3]

Use cases
---------
One element tuple (``ADMINISTRATORS``) has comma at the end:

.. code-block:: python

    ## Content of the ``settings.py`` file
    ADMINISTRATORS = 'mwatney@nasa.gov',


    ## Content of the ``script.py`` file
    from settings import ADMINISTRATORS

    for admin in ADMINISTRATORS:
        print(admin)

    # mwatney@nasa.gov

Problem with missing coma for ``ADMINISTRATORS`` tuple:

.. code-block:: python

    ## Content of the ``settings.py`` file
    ADMINISTRATORS = 'mwatney@nasa.gov'


    ## Content of the ``script.py`` file
    from settings import ADMINISTRATORS

    for admin in ADMINISTRATORS:
        print(admin)

    # m
    # w
    # a
    # t
    # n
    # e
    # y
    # @
    # n
    # a
    # s
    # a
    # .
    # g
    # o
    # v


``pprint``
----------
.. code-block:: python

    from pprint import pprint

    pprint(...)

.. code-block:: python

    import json
    from pprint import pprint

    DATA = '{"contacts": [{"id": 1, "created": "2018-06-13T09:57:55.405Z", "modified": "2018-06-13T10:16:13.975Z", "reporter_id": 1, "is_deleted": false, "firstname": "Mark", "lastname": "Watney", "date_of_birth": "1969-07-24", "email": "mwatney@nasa.gov", "bio": "", "image": "mwatney.jpg", "status": null, "gender": null}, {"id": 2, "created": "2018-06-13T10:26:46.948Z", "modified": "2018-06-13T10:26:46.948Z", "reporter_id": 1, "is_deleted": false, "firstname": "Melissa", "lastname": "Lewis", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 3, "created": "2018-06-13T10:26:55.820Z", "modified": "2018-06-13T10:26:55.820Z", "reporter_id": 1, "is_deleted": false, "firstname": "Rick", "lastname": "Martinez", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 15, "created": "2018-06-13T14:34:42.353Z", "modified": "2018-06-13T14:34:43.638Z", "reporter_id": null, "is_deleted": false, "firstname": "Alex", "lastname": "Vogel", "date_of_birth": null, "email": null, "bio": null, "image": "", "status": null, "gender": null}]}'

    data = json.loads(DATA)
    pprint(data)

.. code-block:: python

    pprint(globals())

.. code-block:: python

    from pprint import pprint

    print(globals())
    pprint(globals())

    def hello(a, b, text='My name...'):
        firstname = 'José'
        lastname = 'Jiménez'
        pprint(locals())
        return locals()


    hello(1, 2)

``pformat``
-----------
.. code-block:: python

    from pprint import pformat


    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return pformat(self.__dict__, indent=1, width=120, compact=False)

    p = Point(1, 2)

    repr(p)
    # <__main__.Point object at 0x10378a470>

    str(p)
    # {'x': 1, 'y': 2}

    print(p)
    # {'x': 1, 'y': 2}


``locals()``
------------
.. code-block:: python

    def hello(a, b, text='My name...'):
        firstname = 'José'
        lastname = 'Jiménez'
        my_vars = locals()
        del my_vars['text']
        return my_vars


Using debugger in IDE
---------------------

Setting Break Points
--------------------

Inspecting variable values
--------------------------

Resume Program
--------------

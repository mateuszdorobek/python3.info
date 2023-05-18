JSON About
==========
* JavaScript Object Notation
* The most popular format for data exchange

Python ``dict``:

.. code-block:: python

    {"name": "Mark Watney", "age": 42, "is_astronaut": True, "friends": None}

JSON ``object``:

.. code-block:: json

    {"name": "Mark Watney", "age": 42, "is_astronaut": true, "friends": null}


JSON or Python?
---------------
* JSON format is similar to ``dict`` notation in Python
* Fields are always enclosed only by double quote ``"`` character
* Instead of ``True`` there is ``true`` (lowercase)
* Instead of ``False`` there is ``false`` (lowercase)
* Instead of ``None`` there is ``null``
* ``list`` is known as ``array`` (despite the same syntax)
* ``dict`` is known as ``object`` (despite the same syntax)
* There is no ``tuple`` or ``set``
* Coma ``,`` is not allowed after the last element in list or object
* ``camelCase`` is convention, although ``snake_case`` is also valid
* Unicode characters are stored as unicode entities (``"cze\\u015b\\u0107"``)

Is the following listing a JSON object or Python ``list[dict]``?

.. code-block:: python

    {'mission': 'Ares 3',
     'launch_date': datetime(2035, 6, 29),
     'destination': 'Mars',
     'destination_landing': datetime(2035, 11, 7),
     'destination_location': 'Acidalia Planitia',
     'crew': [{'name': 'Melissa Lewis', 'born': date(1995, 7, 15)},
              {'name': 'Rick Martinez', 'born': date(1996, 1, 21)},
              {'name': 'Alex Vogel', 'born': date(1994, 11, 15)},
              {'name': 'Chris Beck', 'born': date(1999, 8, 2)},
              {'name': 'Beth Johanssen', 'born': date(2006, 5, 9)},
              {'name': 'Mark Watney', 'born': date(1994, 10, 12)}]}

Is the following listing a JSON object or Python ``list[dict]``?

.. code-block:: json

    {"mission": "Ares 3",
     "launch_date": "2035-06-29T00:00:00",
     "destination": "Mars",
     "destination_landing": "2035-11-07T00:00:00",
     "destination_location": "Acidalia Planitia",
     "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"},
              {"name": "Rick Martinez", "born": "1996-01-21"},
              {"name": "Alex Vogel", "born": "1994-11-15"},
              {"name": "Chris Beck", "born": "1999-08-02"},
              {"name": "Beth Johanssen", "born": "2006-05-09"},
              {"name": "Mark Watney", "born": "1994-10-12"}]}


Pretty Printing JSON
--------------------
* JSON can be minified to save space for network transmission
* It is not very readable

Minified JSON file:

.. code-block:: console

    $ curl https://python3.info/_static/iris.json
    [{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2,
    "species":"setosa"},{"sepal_length":4.9,"sepal_width":3,"petal_length":1.4,
    "petal_width":0.2,"species":"setosa"},{"sepal_length":4.7,"sepal_width":3.2,
    "petal_length":1.3,"petal_width":0.2,"species":"setosa"},{"sepal_length":4.6,
    "sepal_width":3.1,"petal_length":1.5,"petal_width":0.2,"species":"setosa"},
    {"sepal_length":5,"sepal_width":3.6,"petal_length":1.4,"petal_width":0.2,
    "species":"setosa"},{"sepal_length":5.4,"sepal_width":3.9,"petal_length":1.7,
    "petal_width":0.4,"species":"setosa"},{"sepal_length":4.6,"sepal_width":3.4,
    "petal_length":1.4,"petal_width":0.3,"species":"setosa"},{"sepal_length":5,
    "sepal_width":3.4,"petal_length":1.5,"petal_width":0.2,"species":"setosa"},
    {"sepal_length":4.4,"sepal_width":2.9,"petal_length":1.4,"petal_width":0.2,
    "species":"setosa"},{"sepal_length":4.9,"sepal_width":3.1,"petal_length":1.5,
    "petal_width":0.1,"species":"setosa"},{"sepal_length":7,"sepal_width":3.2,
    "petal_length":4.7,"petal_width":1.4,"species":"versicolor"},
    {"sepal_length":6.4,"sepal_width":3.2,"petal_length":4.5,"petal_width":1.5,
    "species":"versicolor"},{"sepal_length":6.9,"sepal_width":3.1,"petal_length":
    4.9,"petal_width":1.5,"species":"versicolor"},{"sepal_length":5.5,
    "sepal_width":2.3,"petal_length":4,"petal_width":1.3,"species":"versicolor"},
    {"sepal_length":6.5,"sepal_width":2.8,"petal_length":4.6,"petal_width":1.5,
    "species":"versicolor"},{"sepal_length":5.7,"sepal_width":2.8,"petal_length"
    :4.5,"petal_width":1.3,"species":"versicolor"},{"sepal_length":6.3,
    "sepal_width":3.3,"petal_length":4.7,"petal_width":1.6,"species":
    "versicolor"},{"sepal_length":4.9,"sepal_width":2.4,"petal_length":3.3,
    "petal_width":1,"species":"versicolor"},{"sepal_length":6.6,"sepal_width":2.9,
    "petal_length":4.6,"petal_width":1.3,"species":"versicolor"},{"sepal_length":
    5.2,"sepal_width":2.7,"petal_length":3.9,"petal_width":1.4,"species":
    "versicolor"},{"sepal_length":6.3,"sepal_width":3.3,"petal_length":6,
    "petal_width":2.5,"species":"virginica"},{"sepal_length":5.8,"sepal_width":
    2.7,"petal_length":5.1,"petal_width":1.9,"species":"virginica"},
    {"sepal_length":7.1,"sepal_width":3,"petal_length":5.9,"petal_width":2.1,
    "species":"virginica"},{"sepal_length":6.3,"sepal_width":2.9,"petal_length":
    5.6,"petal_width":1.8,"species":"virginica"},{"sepal_length":6.5,"sepal_width"
    :3,"petal_length":5.8,"petal_width":2.2,"species":"virginica"},{"sepal_length"
    :7.6,"sepal_width":3,"petal_length":6.6,"petal_width":2.1,"species":
    "virginica"},{"sepal_length":4.9,"sepal_width":2.5,"petal_length":4.5,
    "petal_width":1.7,"species":"virginica"},{"sepal_length":7.3,"sepal_width":
    2.9,"petal_length":6.3,"petal_width":1.8,"species":"virginica"},
    {"sepal_length":6.7,"sepal_width":2.5,"petal_length":5.8,"petal_width":1.8,
    "species":"virginica"},{"sepal_length":7.2,"sepal_width":3.6,"petal_length":
    6.1,"petal_width":2.5,"species":"virginica"}]

Pretty Printing JSON:

.. code-block:: console

    $ curl https://python3.info/_static/iris.json |python -m json.tool
    [
        {
            "petal_length": 1.4,
            "petal_width": 0.2,
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "species": "setosa"
        },
        {
            "petal_length": 1.4,
            "petal_width": 0.2,
            "sepal_length": 4.9,
            "sepal_width": 3,
            "species": "setosa"
        },
    ...

``json.tool`` checks JSON syntax validity:

.. code-block:: console

    $ echo '{"sepal_length":5.1,"sepal_width":3.5,}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 37 (char 36)


Use Case - 0x01
---------------
.. code-block:: text

    [
        {"firstname": "Mark", "lastname": "Watney", "groups": [
            {"gid": 1, "name": "staff"}]},

        {"firstname": "Melissa", "lastname": "Lewis", "groups": [
            {"gid": 1, "name": "staff"},
            {"gid": 2, "name": "admins"}]},

        {"firstname": "Rick", "lastname": "Martinez", "groups": []},
    ]


Use Case - 0x02
---------------
.. code-block:: json

    [{"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

     {"firstname": "Melissa", "lastname": "Lewis", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

     {"firstname": "Rick", "lastname": "Martinez", "addresses": []},

     {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}]

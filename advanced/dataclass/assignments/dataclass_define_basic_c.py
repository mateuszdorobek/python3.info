"""
* Assignment: Dataclass DefineBasic Nested
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. You received input data in JSON format from the API
    2. Using `dataclass` model `DATA` to create class `Pet`
       a. Leave `category` as `dict`
       b. Leave `tags` as `list[dicts]`
    3. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
    2. Wykorzystując `dataclass` zamodeluj `DATA` aby stwórzyć klasę `Pet`
       a. Pozostaw `category` jako `dict`
       b. Pozostaw `tags` jako `list[dicts]`
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1]: https://petstore.swagger.io/#/pet/getPetById

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass
    >>> import json

    >>> assert isclass(Pet)
    >>> assert is_dataclass(Pet)

    >>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
    >>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
    f'Invalid fields, your fields should be: {fields}'

    >>> data = json.loads(DATA)
    >>> result = Pet(**data)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    Pet(id=0, category={'id': 0, 'name': 'dogs'}, name='doggie',
        photoUrls=['img/dogs/0.png'], tags=[{'id': 0, 'name': 'dog'},
                                            {'id': 1, 'name': 'hot-dog'}],
        status='available')
"""

from dataclasses import dataclass


DATA = """
{
  "id": 0,
  "category": {
    "id": 0,
    "name": "dogs"
  },
  "name": "doggie",
  "photoUrls": [
    "img/dogs/0.png"
  ],
  "tags": [
    {
      "id": 0,
      "name": "dog"
    },
    {
      "id": 1,
      "name": "hot-dog"
    }
  ],
  "status": "available"
}
"""


# Using `dataclass` model data to create class `Pet`
# type: type
@dataclass
class Pet:
    ...


# Solution
@dataclass
class Pet:
    id: int
    category: dict
    name: str
    photoUrls: list[str]
    tags: list[dict]
    status: str

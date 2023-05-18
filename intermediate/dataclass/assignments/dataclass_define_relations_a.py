"""
* Assignment: Dataclass DefineRelations Syntax
* Complexity: easy
* Lines of code: 16 lines
* Time: 5 min

English:
    1. You received input data in JSON format from the API
    2. Using `dataclass` model `DATA`:
       a. Create class `Pet`
       b. Create class `Category`
       c. Create class `Tags`
    3. Model relations between classes
    4. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
    2. Wykorzystując `dataclass` zamodeluj `DATA`:
       a. Stwórz klasę `Pet`
       b. Stwórz klasę `Category`
       c. Stwórz klasę `Tags`
    3. Zamodeluj relacje między klasami
    4. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1]: https://petstore.swagger.io/#/pet/getPetById

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass
    >>> import json

    >>> assert isclass(Pet)
    >>> assert isclass(Category)
    >>> assert isclass(Tag)
    >>> assert is_dataclass(Pet)
    >>> assert is_dataclass(Category)
    >>> assert is_dataclass(Tag)

    >>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
    >>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
    f'Invalid fields, your fields should be: {fields}'

    >>> data = json.loads(DATA)
    >>> result = Pet(**data)
    >>> result.category = Category(**result.category)
    >>> result.tags = [Tag(**tag) for tag in result.tags]

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    Pet(id=0, category=Category(id=0, name='dogs'), name='doggie',
        photoUrls=['img/dogs/0.png'], tags=[Tag(id=0, name='dog'),
                                            Tag(id=1, name='hot-dog')],
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


# Using `dataclass` model `DATA`, create class `Category`
# type: type
@dataclass
class Category:
    ...


# Using `dataclass` model `DATA`, create class `Tag`
# type: type
@dataclass
class Tag:
    ...


# Using `dataclass` model `DATA`, create class `Pet`
# type: type
@dataclass
class Pet:
    ...


# Solution
@dataclass
class Category:
    id: int
    name: str


@dataclass
class Tag:
    id: int
    name: str


@dataclass
class Pet:
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str

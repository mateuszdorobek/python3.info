Pydantic Types Constrained
==========================
* Source: https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
* ``conbytes`` - type method for constraining bytes
* ``condecimal`` - type method for constraining Decimals
* ``confloat`` - type method for constraining floats
* ``confrozenset`` - type method for constraining frozen sets
* ``conint`` - type method for constraining ints
* ``conlist`` - type method for constraining lists
* ``conset`` - type method for constraining sets
* ``constr`` - type method for constraining strs

The value of numerous common types can be restricted using ``con*``
type functions.


Arguments to ``conbytes``
-------------------------
* type method for constraining bytes
* ``strip_whitespace: bool = False``: removes leading and trailing whitespace
* ``to_lower: bool = False``: turns all characters to lowercase
* ``min_length: int = None``: minimum length of the byte string
* ``max_length: int = None``: maximum length of the byte string
* ``strict: bool = False``: controls type coercion


Arguments to ``condecimal``
---------------------------
* type method for constraining Decimals
* ``gt: Decimal = None``: enforces decimal to be greater than the set value
* ``ge: Decimal = None``: enforces decimal to be greater than or equal to the set value
* ``lt: Decimal = None``: enforces decimal to be less than the set value
* ``le: Decimal = None``: enforces decimal to be less than or equal to the set value
* ``max_digits: int = None``: maximum number of digits within the decimal. it does not include a zero before the decimal point or trailing decimal zeroes
* ``decimal_places: int = None``: max number of decimal places allowed. it does not include trailing decimal zeroes
* ``multiple_of: Decimal = None``: enforces decimal to be a multiple of the set value


Arguments to ``confloat``
-------------------------
* type method for constraining floats
* ``strict: bool = False``: controls type coercion
* ``gt: float = None``: enforces float to be greater than the set value
* ``ge: float = None``: enforces float to be greater than or equal to the set value
* ``lt: float = None``: enforces float to be less than the set value
* ``le: float = None``: enforces float to be less than or equal to the set value
* ``multiple_of: float = None``: enforces float to be a multiple of the set value


Arguments to ``confrozenset``
-----------------------------
* type method for constraining frozen sets
* ``item_type: type[T]``: type of the frozenset items
* ``min_items: int = None``: minimum number of items in the frozenset
* ``max_items: int = None``: maximum number of items in the frozenset


Arguments to ``conint``
-----------------------
* type method for constraining ints
* ``strict: bool = False``: controls type coercion
* ``gt: int = None``: enforces integer to be greater than the set value
* ``ge: int = None``: enforces integer to be greater than or equal to the set value
* ``lt: int = None``: enforces integer to be less than the set value
* ``le: int = None``: enforces integer to be less than or equal to the set value
* ``multiple_of: int = None``: enforces integer to be a multiple of the set value


Arguments to ``conlist``
------------------------
* type method for constraining lists
* ``item_type: type[T]``: type of the list items
* ``min_items: int = None``: minimum number of items in the list
* ``max_items: int = None``: maximum number of items in the list
* ``unique_items: bool = None``: enforces list elements to be unique


Arguments to ``conset``
-----------------------
* type method for constraining sets
* ``item_type: type[T]``: type of the set items
* ``min_items: int = None``: minimum number of items in the set
* ``max_items: int = None``: maximum number of items in the set


Arguments to ``constr``
-----------------------
* type method for constraining strs
* ``strip_whitespace: bool = False``: removes leading and trailing whitespace
* ``to_lower: bool = False``: turns all characters to lowercase
* ``strict: bool = False``: controls type coercion
* ``min_length: int = None``: minimum length of the string
* ``max_length: int = None``: maximum length of the string
* ``curtail_length: int = None``: shrinks the string length to the set value when it is longer than the set value
* ``regex: str = None``: regex to validate the string against


Example
-------
>>> from decimal import Decimal
>>>
>>> from pydantic import (
...     BaseModel,
...     NegativeFloat,
...     NegativeInt,
...     PositiveFloat,
...     PositiveInt,
...     NonNegativeFloat,
...     NonNegativeInt,
...     NonPositiveFloat,
...     NonPositiveInt,
...     conbytes,
...     condecimal,
...     confloat,
...     conint,
...     conlist,
...     conset,
...     constr,
...     Field,
... )
>>>
>>>
>>> class Model(BaseModel):
...     lower_bytes: conbytes(to_lower=True)
...     short_bytes: conbytes(min_length=2, max_length=10)
...     strip_bytes: conbytes(strip_whitespace=True)
...
...     lower_str: constr(to_lower=True)
...     short_str: constr(min_length=2, max_length=10)
...     regex_str: constr(regex=r'^apple (pie|tart|sandwich)$')
...     strip_str: constr(strip_whitespace=True)
...
...     big_int: conint(gt=1000, lt=1024)
...     mod_int: conint(multiple_of=5)
...     pos_int: PositiveInt
...     neg_int: NegativeInt
...     non_neg_int: NonNegativeInt
...     non_pos_int: NonPositiveInt
...
...     big_float: confloat(gt=1000, lt=1024)
...     unit_interval: confloat(ge=0, le=1)
...     mod_float: confloat(multiple_of=0.5)
...     pos_float: PositiveFloat
...     neg_float: NegativeFloat
...     non_neg_float: NonNegativeFloat
...     non_pos_float: NonPositiveFloat
...
...     short_list: conlist(int, min_items=1, max_items=4)
...     short_set: conset(int, min_items=1, max_items=4)
...
...     decimal_positive: condecimal(gt=0)
...     decimal_negative: condecimal(lt=0)
...     decimal_max_digits_and_places: condecimal(max_digits=2, decimal_places=2)
...     mod_decimal: condecimal(multiple_of=Decimal('0.25'))
...
...     bigger_int: int = Field(..., gt=10000)

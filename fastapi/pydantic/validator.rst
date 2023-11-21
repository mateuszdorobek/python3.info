Pydantic Validator
==================
* Source: https://pydantic-docs.helpmanual.io/usage/validators/
* validators are "class methods", so the first argument value they receive is the UserModel class, not an instance of UserModel.
* the second argument is always the field value to validate; it can be named as you please
* you can also add any subset of the following arguments to the signature (the names must match):
* values: a dict containing the name-to-value mapping of any previously-validated fields
* config: the model config
* field: the field being validated. Type of object is pydantic.fields.ModelField.
* kwargs: if provided, this will include the arguments above not explicitly listed in the signature
* validators should either return the parsed value or raise a ValueError, TypeError, or AssertionError (assert statements may be used).


Validator
---------
* Validation is done in the order fields are defined. E.g. in the example above, password2 has access to password1 (and name), but password1 does not have access to password2. See Field Ordering for more information on how fields are ordered
* If validation fails on another field (or that field is missing) it will not be included in values, hence if 'password1' in values and ... in this example.

>>> from pydantic import BaseModel, ValidationError, field_validator
>>>
>>>
>>> class UserModel(BaseModel):
...     name: str
...     username: str
...     password1: str
...     password2: str
...
...     @field_validator('name')
...     def name_must_contain_space(cls, v):
...         if ' ' not in v:
...             raise ValueError('must contain a space')
...         return v.title()
...
...     @field_validator('password2')
...     def passwords_match(cls, v, values, **kwargs):
...         if 'password1' in values and v != values['password1']:
...             raise ValueError('passwords do not match')
...         return v
...
...     @field_validator('username')
...     def username_alphanumeric(cls, v):
...         assert v.isalnum(), 'must be alphanumeric'
...         return v
>>>
>>>
>>> user = UserModel(  # doctest: +SKIP
...     name='samuel colvin',
...     username='scolvin',
...     password1='zxcvbn',
...     password2='zxcvbn',
... )
>>> print(user)  # doctest: +SKIP
name='Samuel Colvin' username='scolvin' password1='zxcvbn' password2='zxcvbn'
>>>
>>> try:  # doctest: +SKIP
...     UserModel(
...         name='samuel',
...         username='scolvin',
...         password1='zxcvbn',
...         password2='zxcvbn2',
...     )
... except ValidationError as e:
...     print(e)
2 validation errors for UserModel
name
  must contain a space (type=value_error)
password2
  passwords do not match (type=value_error)


Root Validator
--------------
* Validation performed on the entire model's data.

As with field validators, root validators can have pre=True, in which case they're called before field validation occurs (and are provided with the raw input data), or pre=False (the default), in which case they're called after field validation.

Field validation will not occur if pre=True root validators raise an error. As with field validators, "post" (i.e. pre=False) root validators by default will be called even if prior validators fail; this behaviour can be changed by setting the skip_on_failure=True keyword argument to the validator. The values argument will be a dict containing the values which passed field validation and field defaults where applicable.


.. code-block:: python

    from pydantic import BaseModel, ValidationError, model_validator


    class UserModel(BaseModel):
        username: str
        password1: str
        password2: str

        @model_validator
        def check_card_number_omitted(cls, values):
            assert 'card_number' not in values, 'card_number should not be included'
            return values

        @model_validator
        def check_passwords_match(cls, values):
            pw1, pw2 = values.get('password1'), values.get('password2')
            if pw1 is not None and pw2 is not None and pw1 != pw2:
                raise ValueError('passwords do not match')
            return values


    print(UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn'))
    #> username='scolvin' password1='zxcvbn' password2='zxcvbn'
    try:
        UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn2')
    except ValidationError as e:
        print(e)
        """
        1 validation error for UserModel
        __root__
          passwords do not match (type=value_error)
        """

    try:
        UserModel(
            username='scolvin',
            password1='zxcvbn',
            password2='zxcvbn',
            card_number='1234',
        )
    except ValidationError as e:
        print(e)
        """
        1 validation error for UserModel
        __root__
          card_number should not be included (type=assertion_error)
        """


Pre and Per-item Validator
--------------------------
.. code-block:: python

    from typing import List
    from pydantic import BaseModel, ValidationError, field_validator


    class DemoModel(BaseModel):
        square_numbers: List[int] = []
        cube_numbers: List[int] = []

        # '*' is the same as 'cube_numbers', 'square_numbers' here:
        @field_validator('*', pre=True)
        def split_str(cls, v):
            if isinstance(v, str):
                return v.split('|')
            return v

        @field_validator('cube_numbers', 'square_numbers')
        def check_sum(cls, v):
            if sum(v) > 42:
                raise ValueError('sum of numbers greater than 42')
            return v

        @field_validator('square_numbers', each_item=True)
        def check_squares(cls, v):
            assert v ** 0.5 % 1 == 0, f'{v} is not a square number'
            return v

        @field_validator('cube_numbers', each_item=True)
        def check_cubes(cls, v):
            # 64 ** (1 / 3) == 3.9999999999999996 (!)
            # this is not a good way of checking cubes
            assert v ** (1 / 3) % 1 == 0, f'{v} is not a cubed number'
            return v


    print(DemoModel(square_numbers=[1, 4, 9]))
    #> square_numbers=[1, 4, 9] cube_numbers=[]
    print(DemoModel(square_numbers='1|4|16'))
    #> square_numbers=[1, 4, 16] cube_numbers=[]
    print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))
    #> square_numbers=[16] cube_numbers=[8, 27]
    try:
        DemoModel(square_numbers=[1, 4, 2])
    except ValidationError as e:
        print(e)
        """
        1 validation error for DemoModel
        square_numbers -> 2
          2 is not a square number (type=assertion_error)
        """

    try:
        DemoModel(cube_numbers=[27, 27])
    except ValidationError as e:
        print(e)
        """
        1 validation error for DemoModel
        cube_numbers
          sum of numbers greater than 42 (type=value_error)
        """

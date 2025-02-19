Pydantic Models
===============
* Source: https://pydantic-docs.helpmanual.io/usage/models/#private-model-attributes

The primary means of defining objects in ``pydantic`` is via models
(models are simply classes which inherit from ``BaseModel``). You can
think of models as similar to types in strictly typed languages,
or as the requirements of a single endpoint in an API. Untrusted data
can be passed to a model, and after parsing and validation ``pydantic``
guarantees that the fields of the resultant model instance will conform
to the field types defined on the model.

``pydantic`` is primarily a parsing library, **not a validation
library**. Validation is a means to an end: building a model which
conforms to the types and constraints provided. In other words,
``pydantic`` guarantees the types and constraints of the output model,
not the input data. This might sound like an esoteric distinction,
but it is not. If you're unsure what this means or how it might affect
your usage you should read the section about Data Conversion below.
Although validation is not the main purpose of ``pydantic``, you can
use this library for custom validation.


Basic model usage
-----------------
>>> from pydantic import BaseModel
>>>
>>>
>>> class User(BaseModel):
...     id: int
...     name: str = 'Mark Watney'

``User`` here is a model with two fields ``id`` which is an integer and
is required, and ``name`` which is a string and is not required (it has
a default value). The type of ``name`` is inferred from the default
value, and so a type annotation is not required (however note
field-ordering warning about field order when some fields do not have
type annotations).

>>> user = User(id='123')

``user`` here is an instance of ``User``. Initialisation of the object
will perform all parsing and validation, if no ``ValidationError`` is
raised, you know the resulting model instance is valid.

>>> assert user.id == 123

Fields of a model can be accessed as normal attributes of the user
object. The string '123' has been cast to an int as per the field type

>>> assert user.name == 'Mark Watney'

``name`` wasn't set when user was initialised, so it has the default
value

>>> assert user.__fields_set__ == {'id'}

The fields which were supplied when user was initialised.

>>> assert user.dict() == dict(user) == {'id': 123, 'name': 'Mark Watney'}

Either ``.dict()`` or ``dict(user)`` will provide a dict of fields, but
``.dict()`` can take numerous other arguments.

>>> user.id = 321
>>> assert user.id == 321

This model is mutable so field values can be changed.


Model properties
----------------
* ``dict()`` - returns a dictionary of the model's fields and values
* ``json()`` - returns a JSON string representation ``dict()``
* ``copy()`` - returns a copy (by default, shallow copy) of the model
* ``parse_obj()`` - a utility for loading any object into a model with error handling if the object is not a dictionary
* ``parse_raw()`` - a utility for loading strings of numerous formats
* ``parse_file()`` - like ``parse_raw()`` but for file paths
* ``from_orm()`` - loads data into a model from an arbitrary class
* ``schema()`` - returns a dictionary representing the model as JSON Schema
* ``schema_json()`` - returns a JSON string representation of ``schema()``
* ``construct()`` - a class method for creating models without running validation
* ``_fields_set__`` - Set of names of fields which were set when the model instance was initialised
* ``_fields__`` - a dictionary of the model's fields
* ``_config__`` - the configuration class for the model

The example above only shows the tip of the iceberg of what models can
do. Models possess the various methods and attributes.


Recursive Models
----------------
More complex hierarchical data structures can be defined using models
themselves as types in annotations.


ORM Mode (aka Arbitrary Class Instances)
----------------------------------------
Pydantic models can be created from arbitrary class instances to support
models that map to ORM objects.

To do this:

1. The ``Config`` property ``from_attributes`` must be set to ``True``.
2. The special constructor ``from_orm`` must be used to create the model
   instance.

The example here uses SQLAlchemy, but the same approach should work for
any ORM.

>>> from pydantic import BaseModel
>>>
>>>
>>> class User(BaseModel):
...     id: int
...     name: str = 'Mark Watney'
...
...     class Config:
...         from_attributes = True


Reserved names
--------------
You may want to name a Column after a reserved SQLAlchemy field. In that
case, Field aliases will be convenient.

The example above works because aliases have priority over field names for
field population. Accessing ``SQLModel``'s ``metadata`` attribute would
lead to a ``ValidationError``.


Recursive ORM models
--------------------
ORM instances will be parsed with ``from_orm`` recursively as well as at
the top level.


Data binding
------------
Arbitrary classes are processed by ``pydantic`` using the ``GetterDict``
class (see `utils.py <https://github.com/samuelcolvin/pydantic/blob/master/pydantic/utils.py>`_),
which attempts to provide a dictionary-like interface to any class. You
can customise how this works by setting your own sub-class of ``GetterDict``
as the value of ``Config.getter_dict``.

You can also customise class validation using ``model_validator`` with
``pre=True``. In this case your validator function will be passed a
``GetterDict`` instance which you may copy and modify.

The ``GetterDict`` instance will be called for each field with a
sentinel as a fallback (if no other default value is set). Returning
this sentinel means that the field is missing. Any other value will be
interpreted as the value of the field.


Error Handling
--------------
* ``pydantic`` will raise ``ValidationError`` whenever it finds an error in the data it's validating.

Validation code should not raise ``ValidationError`` itself,
but rather raise ``ValueError``, ``TypeError`` or ``AssertionError`` (or
subclasses of ``ValueError`` or ``TypeError``) which will be caught and
used to populate ``ValidationError``.

One exception will be raised regardless of the number of errors found,
that ``ValidationError`` will contain information about all the errors
and how they happened. You can access these errors in a several ways:

* ``e.errors()`` - method will return list of errors found in the input data
* ``e.json()`` - method will return a JSON representation of ``errors``
* ``str(e)`` - method will return a human readable representation of the errors

Each error object contains:

* ``loc`` - the error's location as a list. The first item in the list will be the field where the error occurred, and if the field is a `sub-model`, subsequent items will be present to indicate the nested location of the error.
* ``type`` - a computer-readable identifier of the error type.
* ``msg`` - a human readable explanation of the error.
* ``ctx`` - an optional object which contains values required to render the error message.

``json()`` has ``indent=2`` set by default, but I've tweaked the JSON here and below to
make it slightly more concise.)


Custom Errors
-------------
In your custom data types or validators you should use ``ValueError``,
``TypeError`` or ``AssertionError`` to raise errors. See `Pydantic Validators`
for more details on use of the ``@field_validator`` decorator. You can also
define your own error classes, which can specify a custom error code, message
template, and context.


Helper Functions
----------------
``pydantic`` provides three ``classmethod`` helper functions on models for
parsing data:

* ``parse_obj`` this is very similar to the ``_init__`` method of
   the model, except it takes a dict rather than keyword arguments. If
   the object passed is not a dict a ``ValidationError`` will be raised.

* ``parse_raw`` this takes a ``str`` or ``bytes`` and parses it as
   ``json``, then passes the result to ``parse_obj``. Parsing ``pickle``
   data is also supported by setting the ``content_type`` argument
   appropriately.

* ``parse_file``: this takes in a file path, reads the file and
   passes the contents to ``parse_raw``. If ``content_type`` is omitted,
   it is inferred from the file's extension.

To quote the `official pickle docs <https://docs.python.org/3/library/pickle.html>`_,
'The pickle module is not secure against erroneous or maliciously
constructed data. Never unpickle data received from an untrusted
or unauthenticated source.'

Because it can result in arbitrary code execution, as a security measure,
you need to explicitly pass ``allow_pickle`` to the parsing function in
order to load ``pickle`` data.


Creating models without validation
----------------------------------
``pydantic`` also provides the ``construct()`` method which allows models
to be created **without validation** this can be useful when data has
already been validated or comes from a trusted source and you want to
create a model as efficiently as possible (``construct()`` is generally
around 30x faster than creating a model with full validation).

``construct()`` does not do any validation, meaning it can
create models which are invalid. **You should only ever use the
``construct()`` method with data which has already been validated, or
you trust.**

The ``_fields_set`` keyword argument to ``construct()`` is optional, but
allows you to be more precise about which fields were originally set and
which weren't. If it's omitted ``_fields_set__`` will just be the keys
of the data provided.

For example, in the example above, if ``_fields_set`` was not provided,
``new_user.__fields_set__`` would be ``{'id', 'age', 'name'}``.


Generic Models
--------------
Pydantic supports the creation of generic models to make it easier to
reuse a common model structure.

In order to declare a generic model, you perform the following steps:

* Declare one or more ``typing.TypeVar`` instances to use to
   parameterize your model.
* Declare a pydantic model that inherits from
   ``pydantic.generics.GenericModel`` and ``typing.Generic``, where you
   pass the ``TypeVar`` instances as parameters to ``typing.Generic``.
* Use the ``TypeVar`` instances as annotations where you will want to
   replace them with other types or pydantic models.

Here is an example using ``GenericModel`` to create an easily-reused
HTTP response payload wrapper:

If you set ``Config`` or make use of ``validator`` in your generic model
definition, it is applied to concrete subclasses in the same way as when
inheriting from ``BaseModel``. Any methods defined on your generic class
will also be inherited.

Pydantic's generics also integrate properly with mypy, so you get all
the type checking you would expect mypy to provide if you were to
declare the type without using ``GenericModel``.

Internally, pydantic uses ``create_model`` to generate a
(cached) concrete ``BaseModel`` at runtime, so there is essentially zero
overhead introduced by making use of ``GenericModel``.

To inherit from a GenericModel without replacing the ``TypeVar``
instance, a class must also inherit from ``typing.Generic``:

You can also create a generic subclass of a ``GenericModel`` that
partially or fully replaces the type parameters in the superclass.

If the name of the concrete subclasses is important, you can also
override the default behavior:

Using the same TypeVar in nested models allows you to enforce typing
relationships at different points in your model:

Pydantic also treats ``GenericModel`` similarly to how it treats
built-in generic types like ``List`` and ``Dict`` when it comes to
leaving them unparameterized, or using bounded ``TypeVar`` instances:

* If you don't specify parameters before instantiating the generic
   model, they will be treated as ``Any``
* You can parametrize models with one or more *bounded* parameters to
   add subclass checks

Also, like ``List`` and ``Dict``, any parameters specified using a
``TypeVar`` can later be substituted with concrete types.


Dynamic model creation
----------------------
There are some occasions where the shape of a model is not known until
runtime. For this ``pydantic`` provides the ``create_model`` method to
allow models to be created on the fly.

Here ``StaticFoobarModel`` and ``DynamicFoobarModel`` are identical.

See the note in `Required Optional Fields` for the distinction between an
ellipsis as a field default and annotation-only fields.

Fields are defined by either a tuple of the form
``(<type>, <default value>)`` or just a default value. The special key
word arguments ``_config__`` and ``_base__`` can be used to customise
the new model. This includes extending a base model with extra fields.

You can also add validators by passing a dict to the ``_validators__``
argument.


Model creation from ``NamedTuple`` or ``TypedDict``
---------------------------------------------------
Sometimes you already use in your application classes that inherit from
``NamedTuple`` or ``TypedDict`` and you don't want to duplicate all your
information to have a ``BaseModel``. For this ``pydantic`` provides
``create_model_from_namedtuple`` and ``create_model_from_typeddict``
methods. Those methods have the exact same keyword arguments as
``create_model``.


Custom Root Types
-----------------
Pydantic models can be defined with a custom root type by declaring the
``_root__`` field.

The root type can be any type supported by pydantic, and is specified by
the type hint on the ``_root__`` field. The root value can be passed to
the model ``_init__`` via the ``_root__`` keyword argument, or as the
first and only argument to ``parse_obj``.

If you call the ``parse_obj`` method for a model with a custom root type
with a ``dict`` as the first argument, the following logic is used:

* If the custom root type is a mapping type (eg., ``Dict`` or
   ``Mapping``), the argument itself is always validated against the
   custom root type.
* For other custom root types, if the dict has precisely one key with
   the value ``_root__``, the corresponding value will be validated
   against the custom root type.
* Otherwise, the dict itself is validated against the custom root type.

This is demonstrated in the following example:

Calling the ``parse_obj`` method on a dict with the single
key ``"__root__"`` for non-mapping custom root types is currently
supported for backwards compatibility, but is not recommended and may be
dropped in a future version.

If you want to access items in the ``_root__`` field directly or to
iterate over the items, you can implement custom ``_iter__`` and
``_getitem__`` functions, as shown in the following example.


Faux Immutability
-----------------
Models can be configured to be immutable via ``allow_mutation = False``.
When this is set, attempting to change the values of instance attributes
will raise errors. See `model config` for more details on ``Config``.

Immutability in python is never strict. If developers are
determined/stupid they can always modify a so-called 'immutable' object.

Trying to change ``a`` caused an error, and ``a`` remains unchanged.
However, the dict ``b`` is mutable, and the immutability of ``foobar``
doesn't stop ``b`` from being changed.


Abstract Base Classes
---------------------
Pydantic models can be used alongside Python's `Abstract Base
Classes <https://docs.python.org/3/library/abc.html>`_ (ABCs).


Field Ordering
--------------
Field order is important in models for the following reasons:

* validation is performed in the order fields are defined;
  `fields validators` can access the values of earlier fields,
  but not later ones
* field order is preserved in the model `schema`
* field order is preserved in `validation errors`
* field order is preserved by ```.dict()`` and ``.json()`` etc.

As of **v1.0** all fields with annotations (whether annotation-only or
with a default value) will precede all fields without an annotation.
Within their respective groups, fields remain in the order they were
defined.

As demonstrated by the example above, combining the use of
annotated and non-annotated fields in the same model can result in
surprising field orderings. (This is due to limitations of python)

Therefore, **we recommend adding type annotations to all fields**, even when a default value
would determine the type by itself to guarantee field order is preserved.


Required fields
---------------
To declare a field as required, you may declare it using just an
annotation, or you may use an ellipsis (``...``) as the value:

Where ``Field`` refers to the `field function`.

Here ``a``, ``b`` and ``c`` are all required. However, use of the
ellipses in ``b`` will not work well with `mypy`, and as of
**v1.0** should be avoided in most cases.


Required Optional fields
------------------------
Since version **v1.2** annotation only nullable
(``Optional[...]``, ``Union[None, ...]`` and ``Any``) fields and
nullable fields with an ellipsis (``...``) as the default value, no
longer mean the same thing. In some situations this may cause **v1.2**
to not be entirely backwards compatible with earlier **v1.*** releases.

If you want to specify a field that can take a ``None`` value while
still being required, you can use ``Optional`` with ``...``:

In this model, ``a``, ``b``, and ``c`` can take ``None`` as a value. But
``a`` is optional, while ``b`` and ``c`` are required. ``b`` and ``c``
require a value, even if the value is ``None``.


Field with dynamic default value
--------------------------------
When declaring a field with a default value, you may want it to be
dynamic (i.e. different for each model). To do this, you may want to use
a ``default_factory``.

'In Beta' The ``default_factory`` argument is in **beta**, it
has been added to ``pydantic`` in **v1.5** on a **provisional basis**. It
may change significantly in future releases and its signature or
behaviour will not be concrete until **v2**. Where ``Field`` refers to the
`field function`. The ``default_factory`` expects the field type to be set.


Automatically excluded attributes
---------------------------------
Class variables which begin with an underscore and attributes annotated
with ``typing.ClassVar`` will be automatically excluded from the model.


Private model attributes
------------------------
If you need to vary or manipulate internal attributes on instances of
the model, you can declare them using ``PrivateAttr``:

Private attribute names must start with underscore to prevent conflicts
with model fields: both ``_attr`` and ``_attr__`` are supported.

If ``Config.underscore_attrs_are_private`` is ``True``, any non-ClassVar
underscore attribute will be treated as private:

Upon class creation pydantic constructs ``_slots__`` filled with
private attributes.


Parsing data into a specified type
----------------------------------
Pydantic includes a standalone utility function ``parse_obj_as`` that
can be used to apply the parsing logic used to populate pydantic models
in a more ad-hoc way. This function behaves similarly to
``BaseModel.parse_obj``, but works with arbitrary pydantic-compatible
types.

This is especially useful when you want to parse results into a type
that is not a direct subclass of ``BaseModel``. For example:

This function is capable of parsing data into any of the types pydantic
can handle as fields of a ``BaseModel``.

Pydantic also includes two similar standalone functions called
``parse_file_as`` and ``parse_raw_as``, which are analogous to
``BaseModel.parse_file`` and ``BaseModel.parse_raw``.


Data Conversion
---------------
``pydantic`` may cast input data to force it to conform to model field
types, and in some cases this may result in a loss of information. This
is a deliberate decision of ``pydantic``, and in general it's the most
useful approach. Nevertheless, `strict type checking` is partially supported.


Model signature
---------------
All ``pydantic`` models will have their signature generated based on their
fields. An accurate signature is useful for introspection purposes and
libraries like ``FastAPI`` or ``hypothesis``.

The generated signature will also respect custom ``_init__`` functions.
To be included in the signature, a field's alias or name must be a valid
python identifier. ``pydantic`` prefers aliases over names, but may use
field names if the alias is not a valid python identifier.

If a field's alias and name are both invalid identifiers, a ``**data``
argument will be added. In addition, the ``**data`` argument will always
be present in the signature if ``Config.extra`` is ``Extra.allow``.

Types in the model signature are the same as declared in model
annotations, not necessarily all the types that can actually be provided
to that field.

FastAPI Config
==============


>>> from typing import Any, Type, Callable
>>> import json

>>> class Config:
...     title: str | None = None
...     anystr_lower: bool = False
...     anystr_strip_whitespace: bool = False
...     min_anystr_length: int = 0
...     max_anystr_length: int | None = None
...     validate_all: bool = False
...     extra: 'Extra' = 'Extra.ignore'
...     allow_mutation: bool = True
...     frozen: bool = False
...     allow_population_by_field_name: bool = False
...     use_enum_values: bool = False
...     fields: dict[str, str | dict[str,str]] = {}
...     validate_assignment: bool = False
...     error_msg_templates: dict[str, str] = {}
...     arbitrary_types_allowed: bool = False
...     from_attributes: bool = False
...     getter_dict: type['GetterDict'] = 'GetterDict'
...     alias_generator: Callable[[str], str] | None = None
...     keep_untouched: tuple[type, ...] = ()
...     json_schema_extra: dict[str, Any] = {}
...     json_loads: Callable[[str], Any] = json.loads
...     json_dumps: Callable[..., str] = json.dumps
...     # key type should include ForwardRef, but that breaks with python3.6
...     json_encoders: dict[type[Any] | str, Callable] = {}
...     underscore_attrs_are_private: bool = False
...
...     # whether inherited models as fields should be reconstructed as base model
...     copy_on_model_validation: bool = True
...
...     # whether `Union` should check all allowed types before even trying to coerce
...     smart_union: bool = False

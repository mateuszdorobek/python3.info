Regex RE Type Annotation
========================
* ``typing.Pattern``
* ``typing.Match``

These type aliases correspond to the return types from re.compile() and
re.match(). These types (and the corresponding functions) are generic in
AnyStr and can be made specific by writing Pattern[str], Pattern[bytes],
Match[str], or Match[bytes].

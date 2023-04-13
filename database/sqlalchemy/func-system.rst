Func Count
==========
* ``current_user`` - The CURRENT_USER() SQL function
* ``session_user`` - The SESSION_USER() SQL function
* ``sysdate`` - The SYSDATE() SQL function
* ``user`` - The USER() SQL function
* ``AnsiFunction`` - Define a function in 'ansi' format, which doesn't render parenthesis
* ``Function`` - Describe a named SQL function
* ``FunctionAsBinary`` -
* ``FunctionElement`` - Base for SQL function-oriented constructs
* ``GenericFunction`` - Define a 'generic' function
* ``OrderedSetAgg`` - Define a function where the return type is based on the sort expression type as defined by the expression passed to the ``FunctionElement.within_group()`` method
* ``register_function`` - Associate a callable with a particular func. name
* ``ReturnTypeFromArgs`` - Define a function whose return type is the same as its arguments
* ``ScalarFunctionColumn`` -


About
-----
.. csv-table:: System Functions
    :widths: 20,80
    :header: "Object", "Name Description"

    "``current_user``",          "The CURRENT_USER() SQL function"
    "``session_user``",          "The SESSION_USER() SQL function"
    "``sysdate``",               "The SYSDATE() SQL function"
    "``user``",                  "The USER() SQL function"

.. csv-table:: Function Operations
    :widths: 20,80
    :header: "Object", "Name Description"

    "``AnsiFunction``",          "Define a function in 'ansi' format, which doesn't render parenthesis"
    "``Function``",              "Describe a named SQL function"
    "``FunctionAsBinary``",      ""
    "``FunctionElement``",       "Base for SQL function-oriented constructs"
    "``GenericFunction``",       "Define a 'generic' function"
    "``OrderedSetAgg``",         "Define a function where the return type is based on the sort expression type as defined by the expression passed to the ``FunctionElement.within_group()`` method"
    "``register_function``",     "Associate a callable with a particular func. name"
    "``ReturnTypeFromArgs``",    "Define a function whose return type is the same as its arguments"
    "``ScalarFunctionColumn``",  ""

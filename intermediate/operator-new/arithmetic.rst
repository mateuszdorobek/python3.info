Operator Arithmetic
===================
* ``x + y`` - will call method "add" on object ``x`` (``x.__add__(y)``)
* ``x - y`` - will call method "sub" on object ``x`` (``x.__sub__(y)``)
* ``x * y`` - will call method "mul" on object ``x`` (``x.__mul__(y)``)
* ``x ** y`` - will call method "pow" on object ``x`` (``x.__pow__(y)``)
* ``x @ y`` - will call method "matmul" on object ``x`` (``x.__matmul__(y)``)
* ``x / y`` - will call method "truediv" on object ``x`` (``x.__truediv__(y)``)
* ``x // y`` - will call method "floordiv" on object ``x`` (``x.__floordiv__(y)``)
* ``x % y`` - will call method "mod" on object ``x`` (``x.__mod__(y)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"
    "``obj / other``",     "``obj.__truediv__(other)``"
    "``obj // other``",    "``obj.__floordiv__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"

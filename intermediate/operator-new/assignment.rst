Operator Assignment
===================
* := - Walrus operator
* ``x += y`` - will call method "iadd" on object ``x`` (``x.__iadd__(y)``)
* ``x -= y`` - will call method "isub" on object ``x`` (``x.__isub__(y)``)
* ``x *= y`` - will call method "imul" on object ``x`` (``x.__imul__(y)``)
* ``x **= y`` - will call method "ipow" on object ``x`` (``x.__ipow__(y)``)
* ``x @= y`` - will call method "imatmul" on object ``x`` (``x.__imatmul__(y)``)
* ``x /= y`` - will call method "itruediv" on object ``x`` (``x.__itruediv__(y)``)
* ``x //= y`` - will call method "ifloordiv" on object ``x`` (``x.__ifloordiv__(y)``)
* ``x %= y`` - will call method "imod" on object ``x`` (``x.__imod__(y)``)

.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj += other``",     "``obj.__iadd__(other)``"
    "``obj -= other``",     "``obj.__isub__(other)``"
    "``obj *= other``",     "``obj.__imul__(other)``"
    "``obj **= other``",    "``obj.__ipow__(other)``"
    "``obj @= other``",     "``obj.__imatmul__(other)``"
    "``obj /= other``",     "``obj.__itruediv__(other)``"
    "``obj //= other``",    "``obj.__ifloordiv__(other)``"
    "``obj %= other``",     "``obj.__imod__(other)``"

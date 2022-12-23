Performance CTypes
==================


Workflow
--------
Code:

.. code-block:: C

    long factorial(long n) {
        if (n == 0)
            return 1;

        return (n * factorial(n - 1));
    }

Build:

.. code-block:: console

    $ INCLUDES='-I/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/include/python3.7m/'
    $ FILE='mylibrary'
    $ gcc -fPIC -c -o ${FILE}.o ${FILE}.c ${INCLUDE}
    $ gcc -shared ${FILE}.o -o ${FILE}.so

Run:

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')

    lib.factorial(16)  # 2004189184
    lib.factorial(17)  # -288522240


Arguments
---------
* ``ctypes.c_double``
* ``ctypes.c_int``
* ``ctypes.c_char``
* ``ctypes.c_char_p``
* ``ctypes.POINTER(ctypes.c_double)``

.. code-block:: python

    lib.myfunction.argtypes = [
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_double),
    ]

.. code-block:: python

    lib.myfunction.restype = ctypes.c_char_p


Multi OS code
-------------
.. code-block:: python

    import sys
    import ctypes


    if sys.platform == 'darwin':
       lib = ctypes.CDLL('/usr/lib/libc.dylib')
    elif sys.platform == 'win32':
        lib = ctypes.CDLL('/usr/lib/libc.dll')
    else:
        lib = ctypes.CDLL('/usr/lib/libc.so')


    lib.printf("I'm C printf() function called from Python")

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')
    print(dir(lib))


Overflow
--------
.. code-block:: C

    #include <stdio.h>

    void echo(int number) {
        printf("Number: %d", number);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')

    lib.echo(10 ** 10)  # Number: 1410065408

    lib.echo(10 ** 30)
    # Traceback (most recent call last):
    # ctypes.ArgumentError: argument 1: <class 'OverflowError'>: int too long to convert


Use Case - 0x01
---------------
.. code-block:: C

    #include <stdio.h>

    void ehlo() {
        printf("Ehlo World");
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')
    lib.ehlo()


Use Case - 0x02
---------------
.. code-block:: C

    #include <stdio.h>

    void greeting(char *name) {
        printf("Ehlo %s!\n", name);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')

    lib.greeting.argtypes = [ctypes.c_char_p]
    name = ctypes.create_string_buffer('Watney'.encode('ASCII'))
    lib.greeting(name)


Use Case - 0x03
---------------
.. code-block:: C

    #include <stdio.h>

    void number(int num) {
        printf("My number %d\n", num);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')
    lib.number(10)


Use Case - 0x04
---------------
.. code-block:: C

    int return_int(int num) {
        return num;
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('mylibrary.so')

    i = lib.return_int(15)
    print(i)


Assignments
-----------
.. literalinclude:: assignments/ctypes_datetime.py
    :caption: :download:`Solution <assignments/ctypes_datetime.py>`
    :end-before: # Solution

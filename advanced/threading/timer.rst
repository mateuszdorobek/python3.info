Threading Timer
===============


Delay execution
---------------
* dlaczego nie ``time.sleep()``
* rekurencyjny timer

Delay execution:

.. code-block:: python

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Hello world!')


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')

Recurrent timer:

.. code-block:: python

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Timer Thread')
        Timer(DELAY_SECONDS, hello).start()


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')


Assignments
-----------
.. literalinclude:: assignments/threading_timer_a.py
    :caption: :download:`Solution <assignments/threading_timer_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/threading_timer_b.py
    :caption: :download:`Solution <assignments/threading_timer_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/threading_timer_c.py
    :caption: :download:`Solution <assignments/threading_timer_c.py>`
    :end-before: # Solution

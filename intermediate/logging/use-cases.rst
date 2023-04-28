Logging Use Cases
=================

Use Case - 0x01
---------------
.. code-block:: python

    import logging
    import os

    logging.basicConfig(
        format='"{asctime}", "{levelname}", "{message}"',
        filename='...',
        style='{'
    )

    log = logging.getLogger(__name__)
    level = os.getenv('LOG_LEVEL', 'INFO')
    log.setLevel(level)


    log.critical('Critical error... finishing')
    log.error('Some problem but can continue')
    log.warning('Warning, this is important')
    log.info('Typical message')
    log.debug('Debug message with extra information')


    logging.getLogger('requests').setLevel('DEBUG')
    logging.getLogger('_tmp').setLevel('ERROR')


Use Case - 0x02
---------------
.. code-block:: python

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[{levelname}] {message}',
        style='{'
    )


    def timeit(func):
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_end = datetime.now()
            time = time_end - time_start
            logging.debug(f'Time: {time}')
            return result
        return wrapper


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            logging.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            logging.debug(f'Result: {result}')
            return result
        return wrapper


    @timeit
    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # [DEBUG] Calling: function='add_numbers', args=(1, 2), kwargs={}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000105

    add_numbers(1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000042

    add_numbers(a=1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000040

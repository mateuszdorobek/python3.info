"""
* Assignment: Concurrency Threading Subprocess
* Complexity: easy
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz kolejkę `queue` do której dodasz różne polecenia systemowe do wykonania, np.:
        a. Linux/macOS: `['ls /tmp/', 'echo "test"', 'sleep 2']`,
        b. Windows: `['dir c:\\Windows', 'echo "test"', 'type %HOMEPATH%\Desktop\README.txt']`.
    2. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki
    3. Wątki powinny być uruchamiane jako `subprocess.run()` w systemie operacyjnym z timeoutem równym `TIMEOUT = 1.0` sekundy
    4. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
    5. Wątki mają być uruchomione w tle (ang. `daemon`)
    6. Uruchom doctesty - wszystkie muszą się powieść

:Extra task:
    1. Wątki powinny być uśpione za pomocą `Timer` przez `DELAY = 1.0` sekund, a następnie ruszyć do roboty
    2. Użyj logowania za pomocą biblioteki `logging` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku.

Hints:
    * Ustaw parametr `shell=True` dla `subprocess.run()`

Tests:
    TODO: Doctests
"""
import logging


TIMEOUT = 1.0
DELAY = 1.0
TODO = [
    'ls /tmp/',
    'echo "test"',
    'sleep 2',
]


# Solution
import subprocess
from queue import Queue
from threading import Timer


work_queue = Queue()


def run():
    while True:
        cmd = work_queue.get()

        try:
            subprocess.run(cmd, timeout=TIMEOUT, shell=True)
        except subprocess.TimeoutExpired:
            logging.error('Timeout')
            break

        work_queue.task_done()


t = Timer(DELAY, run)
t.start()

# Assign tasks
for todo in TODO:
    work_queue.put(todo)

# Wait to complete all tasks
t.join(timeout=TIMEOUT)

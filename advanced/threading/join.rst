Threading Join
==============


Example
-------
Joining Threads:

.. code-block:: python

    from queue import Queue
    from threading import Thread, Lock
    from time import sleep


    EXIT = False
    LOCK = Lock()
    TODO = Queue()
    RUNNING = []


    class MyThread(Thread):
        def run(self):
            while not EXIT:
                # Remove and return an item from the queue.
                job = TODO.get()

                # Execute work
                print(f'Will do the work: {job}')

                # Indicate that a formerly enqueued task is complete.
                TODO.task_done()
                sleep(1)

            print(f'Exiting {self.name}')


    # Create new threads
    def spawn_worker(count=1):
        for i in range(count):
            thread = MyThread()
            thread.start()
            RUNNING.append(thread)


    if __name__ == '__main__':
        spawn_worker(5)

        # Fill the queue
        with LOCK:
            for task in ['One', 'Two', 'Three', 'Four', 'Five']:
                TODO.put(task)

        # Wait for queue to empty
        while not TODO.empty():
            pass

        # Notify threads it's time to exit
        EXIT = True

        # Wait for all threads to complete
        for thread in RUNNING:
            thread.join()

        print(f'Exiting Main Thread')

import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
		print 'StoppableThread init'
		super(StoppableThread, self).__init__()
		self._stop_event = threading.Event()

    def stop(self):
		print 'StoppableThread init'
        self._stop_event.set()

    def stopped(self):
		print 'StoppableThread init'
        return self._stop_event.is_set()
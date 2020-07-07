import threading

class Chopstick(threading.Semaphore):

  def __init__(self, name):
    threading.Semaphore.__init__(self)
    self.name = name

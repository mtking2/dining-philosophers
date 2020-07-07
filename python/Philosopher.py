import threading, time, random

class Philosopher(threading.Thread):

  def __init__(self, name, left_chopstick, right_chopstick, color):
    threading.Thread.__init__(self)
    self.stopped = False
    self.name = color + name + '\033[00m'
    self.left_chopstick = left_chopstick
    self.right_chopstick = right_chopstick

  def pickup(self):
    if not self.stopped:
      self.left_chopstick.acquire()
      self.right_chopstick.acquire()

  def putdown(self):
    self.left_chopstick.release()
    self.right_chopstick.release()

  def stop(self):
    self.stopped = True

  def run(self):
    while not self.stopped:
      print(f'{self.name} is waiting.')
      self.pickup()
      if self.stopped: return

      print(f'{self.name} is eating.')
      time.sleep(random.randint(3, 10))
      self.putdown()

      print(f'{self.name} is thinking.')
      if not self.stopped: time.sleep(random.randint(3, 15))

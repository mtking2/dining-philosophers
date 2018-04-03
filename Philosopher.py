import threading, time, random

class Philosopher(threading.Thread):

  def __init__(self, name, left_chopstick, right_chopstick, color):
    threading.Thread.__init__(self)
    self.name = color + name + '\033[00m'
    self.left_chopstick = left_chopstick
    self.right_chopstick = right_chopstick

  def run(self):

    while True:
      print(f'{self.name} is waiting.')
      self.left_chopstick.acquire()
      self.right_chopstick.acquire()

      print(f'{self.name} is eating.')
      time.sleep(random.randint(3, 10))

      self.left_chopstick.release()
      self.right_chopstick.release()

      print(f'{self.name} is thinking.')
      time.sleep(random.randint(3, 15))

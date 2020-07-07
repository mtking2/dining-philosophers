import sys, random, signal
from Philosopher import Philosopher
from Chopstick import Chopstick

colors = {
  'red': '\033[0;31m',  # red
  'yellow': '\033[33m',  # yellow
  'green': '\033[32m',  # green
  'blue': '\033[34m',  # blue
  'purple': '\033[35m'  # purple
}

c1 = Chopstick('c1')
c2 = Chopstick('c2')
c3 = Chopstick('c3')
c4 = Chopstick('c4')
c5 = Chopstick('c5')

chopsticks = [c1, c2, c3, c4, c5]

names = ['Aristotle','Confucius','Descartes','Kant','Plato']
random.shuffle(names)

p1 = Philosopher(names[0], c1, c2, colors['red'])
p2 = Philosopher(names[1], c2, c3, colors['yellow'])
p3 = Philosopher(names[2], c3, c4, colors['green'])
p4 = Philosopher(names[3], c4, c5, colors['blue'])
p5 = Philosopher(names[4], c5, c1, colors['purple'])

philosophers = [p1, p2, p3, p4, p5]

def init():
  print('Philosophers:')
  for p in philosophers:
    print(f'{p.name} ', end='')
  print('\n\nDinner is served!\n')

def start():
  for p in philosophers:
    p.start()
  for p in philosophers:
    p.join()

def exit(signum, frame):
  for p in philosophers:
    p.stop()
  print('\nDinner has ended. Waiting for everyone to finish up!\n')

if __name__ == '__main__':
  signal.signal(signal.SIGINT, exit)
  init()
  start()
  print("\nDone! 👌")

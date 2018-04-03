from Philosopher import Philosopher
from Chopstick import Chopstick

colors = {
  'red': '\033[0;31m',  # red
  'yellow': '\033[33m',  # yellow
  'green': '\033[01;32m',  # green
  'blue': '\033[01;34m',  # blue
  'purple': '\033[35m'  # purple
}

c1 = Chopstick('c1')
c2 = Chopstick('c2')
c3 = Chopstick('c3')
c4 = Chopstick('c4')
c5 = Chopstick('c5')

chopsticks = [c1, c2, c3, c4, c5]

p1 = Philosopher('Aristotle', c1, c2, colors['red'])
p2 = Philosopher('Confucius', c2, c3, colors['yellow'])
p3 = Philosopher('Descartes', c3, c4, colors['green'])
p4 = Philosopher('Kant', c4, c5, colors['blue'])
p5 = Philosopher('Plato', c5, c1, colors['purple'])

philosophers = [p1, p2, p3, p4, p5]

print('Philosophers:')
for p in philosophers:
  print(f'{p.name} ', end='')

print('\n')
print('Dinner is served!\n')

for p in philosophers:
  p.start()
for p in philosophers:
  p.join()

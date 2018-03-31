from Philosopher import Philosopher
from Chopstick import Chopstick

'''
local RED="\033[0;31m"
local BLUE="\033[01;34m"
local GREEN="\033[01;32m"
local WHITE="\033[00m"
'''

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

p1 = Philosopher(c1, c2, colors['red'])
p2 = Philosopher(c2, c3, colors['yellow'])
p3 = Philosopher(c3, c4, colors['green'])
p4 = Philosopher(c4, c5, colors['blue'])
p5 = Philosopher(c5, c1, colors['purple'])

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

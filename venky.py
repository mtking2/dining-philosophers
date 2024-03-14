import threading
import time
import random

# Define the number of philosophers and forks
num_philosophers = 5
num_forks = num_philosophers

# Define semaphores for the forks and the mutex
forks = [threading.Semaphore(1) for i in range(num_forks)]
mutex = threading.Semaphore(1)

# Define the philosopher thread function
def philosopher(index):
	while True:
		print(f"Philosopher {index} is thinking...")
		time.sleep(random.randint(1, 5))
		
		mutex.acquire()
		
		left_fork_index = index
		right_fork_index = (index + 1) % num_forks
		
		forks[left_fork_index].acquire()
		forks[right_fork_index].acquire()
		
		mutex.release()
		
		print(f"Philosopher {index} is eating...")
		time.sleep(random.randint(1, 5))
		
		forks[left_fork_index].release()
		forks[right_fork_index].release()

# Create a thread for each philosopher
philosopher_threads = []
for i in range(num_philosophers):
	philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
	
# Start the philosopher threads
for thread in philosopher_threads:
	thread.start()
	
# Wait for the philosopher threads to complete
for thread in philosopher_threads:
	thread.join()

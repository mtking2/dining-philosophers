#include <array>
#include <iostream>
#include <mutex>
#include <signal.h>
#include <stdlib.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "philosopher.cpp"

using namespace std;

array<Philosopher *, 5> philosophers;
array<Chopstick *, 5> chopsticks;

mutex global_lock;

array<string, 5> names = {"Plato", "Socrates", "Kant", "Descartes", "Confucius"};

array<string, 5> colors = {
    "\033[31m", // red
    "\033[33m", // yellow
    "\033[32m", // green
    "\033[34m", // blue
    "\033[35m", // purple
};

string white = "\033[00m"; // white

void quit(int s) {
    for (Philosopher *p : philosophers)
        p->stop();
    cout << "\nDinner is over. Letting philosophers finish up..." << endl;
}

int main() {
    cout << "Dinner is served! (Ctl+C to end)" << endl;

    for (int i = 0; i < chopsticks.size(); i++)
        chopsticks[i] = new Chopstick();

    cout << "\nPhilosophers: " << endl;
    for (int i = 0; i < names.size(); i++) {
        int rc = (i + 1) % names.size();
        philosophers[i] = new Philosopher(colors[i] + names[i] + white, 5, *chopsticks[i], *chopsticks[rc], global_lock);
    }
    cout << endl << endl;

    signal(SIGINT, quit);

    for (Philosopher *p : philosophers)
        p->join();

    return 0;
}

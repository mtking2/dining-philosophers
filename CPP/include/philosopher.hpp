#include "chopstick.hpp"
#include <random>
#include <thread>

using namespace std;

class Philosopher {

    string name;
    int appetite;
    int food_eaten;
    Chopstick& left_chopstick;
    Chopstick& right_chopstick;
    thread td;
    mutex& g_lock;
    std::mt19937 rng{random_device{}()};
    bool stopped;

public:
    Philosopher(string, int, Chopstick&, Chopstick&, mutex&);
    ~Philosopher();

    void eat();
    void think();
    void ponder(int, int);
    void emote(string);
    void start();
    void stop();
    void run();
    void join();
};
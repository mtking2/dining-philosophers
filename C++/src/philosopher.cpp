#include <chrono>
#include <iostream>
#include <mutex>
#include <thread>
#include <time.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "../include/philosopher.hpp"
#include "chopstick.cpp"

using namespace std;

Philosopher::Philosopher(string name, int appetite, Chopstick& left_stick, Chopstick& right_stick, mutex& g_lock)
    : name(name), appetite(appetite), left_chopstick(left_stick), right_chopstick(right_stick), g_lock(g_lock),
      td(&Philosopher::run, this) {

    food_eaten = 0;
    stopped = false;
    emote("has joined");
}

Philosopher::~Philosopher() {
    // join();
    emote("is finished");
}

void Philosopher::eat() {
    // emote(" is waiting");
    lock_guard<mutex> lc(left_chopstick.mtx);
    lock_guard<mutex> rc(right_chopstick.mtx);

    emote("is eating (" + to_string(++food_eaten) + "/" + to_string(appetite) + ")");
    ponder(3, 5);
}

void Philosopher::think() {
    emote("is thinking");
    ponder(2, 4);
}

void Philosopher::ponder(int min_sec, int max_sec) {
    if (stopped) return;
    thread_local uniform_int_distribution<> dist(min_sec, max_sec);
    int t = dist(rng);
    this_thread::sleep_for(chrono::milliseconds(t * 1000));
    if (food_eaten >= appetite) stopped = true;
}

void Philosopher::emote(string str) {
    lock_guard<mutex> cout_lock(g_lock);
    cout << name << " " << str << endl;
}

void Philosopher::start() {
    thread td(&Philosopher::run, this);
    join();
}

void Philosopher::stop() {
    stopped = true;
}

void Philosopher::run() {
    this_thread::sleep_for(chrono::milliseconds(1000));

    while (!stopped) {
        think();
        if (stopped) break;
        eat();
    }
    emote("is finished");
}

void Philosopher::join() {
    td.join();
}

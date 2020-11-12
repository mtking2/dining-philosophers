#include <mutex>

using namespace std;

class Chopstick {

    string id;

public:
    mutable mutex mtx;

    Chopstick();
    Chopstick(string);
};
use std::thread;
use std::sync::{Mutex, Arc};
use std::time::Duration;
use rand::Rng;
use ansi_term::Color::{Red, Yellow, Green, Blue, Purple};

struct Table {
    forks: Vec<Mutex<()>>,
}

struct Philosopher {
    name: String,
    left: usize,
    right: usize,
}

impl Philosopher {
    fn new(name: &str, left: usize, right: usize) -> Philosopher {
        Philosopher {
            name: name.to_string(),
            left: left,
            right: right,
        }
    }

    fn think(&self) {
        let slp_time = rand::thread_rng().gen_range(1000, 4000);
        println!("{} is thinking", self.name);
        thread::sleep(Duration::from_millis(slp_time));
    }

    fn eat(&self, table: &Table) {
        println!("{} is waiting for forks", self.name);
        let _left = table.forks[self.left].lock();
        let _right = table.forks[self.right].lock();

        let slp_time = rand::thread_rng().gen_range(1000, 4000);
        println!("{} is eating", self.name);
        thread::sleep(Duration::from_millis(slp_time));

        // Mutexes unlock automatically once the MutexGuards (_left, _right) leave scope
        // https://doc.rust-lang.org/std/sync/struct.Mutex.html#method.lock
    }
}

fn main() {
    let table = Arc::new(Table { forks: vec![
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
    ]});

    let philosophers = vec![
        Philosopher::new(&Red.paint("Plato").to_string(), 0, 1),
        Philosopher::new(&Yellow.paint("Socrates").to_string(), 1, 2),
        Philosopher::new(&Green.paint("Marx").to_string(), 2, 3),
        Philosopher::new(&Blue.paint("Nietzsche").to_string(), 3, 4),
        Philosopher::new(&Purple.paint("Confucius").to_string(), 0, 4), // left-handed to prevent deadlock
    ];

    println!("\nDinner is served! (CTRL-C to stop)\n");

    let handles: Vec<_> = philosophers.into_iter().map( |p| {
        let table = table.clone();

        thread::spawn(move || {
            loop {
                p.eat(&table);
                p.think();
            }
        })
    }).collect();

    for h in handles {
        h.join().unwrap();
    }
}

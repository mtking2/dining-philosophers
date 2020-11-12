package main

import (
	"fmt"
	"os"
	"os/signal"
	"sync"
	"syscall"
)

func main() {

	exit, wg := setup()
	<-exit
	wg.Wait()

	fmt.Println("\nSupper is over!!")
}

func setup() (chan bool, *sync.WaitGroup) {

	var wg sync.WaitGroup

	var forks []*Fork
	for i := 0; i < 5; i++ {
		forks = append(forks, newFork())
	}

	var names = [...]string{"Aristotle", "Socrates", "Descartes", "Kant", "Plato"}
	var philosophers [5]*Philosopher

	var colors = [...]string{"\033[31m",
		"\033[32m",
		"\033[33m",
		"\033[34m",
		"\033[35m"}
	var white = "\033[00m"
	for i, name := range names {
		philosophers[i] = newPhilosopher(colors[i]+name+white, forks[i], forks[(i+1)%len(names)])
	}

	for _, p := range philosophers {
		wg.Add(1)
		go p.start(&wg)
	}
	sigs := make(chan os.Signal, 1)
	exit := make(chan bool, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	go func(philosophers [5]*Philosopher) {
		<-sigs
		for _, p := range philosophers {
			p.stop()
		}

		fmt.Println("\nDinner is over. Letting philosophers finish up...")
		exit <- true
	}(philosophers)

	return exit, &wg

}

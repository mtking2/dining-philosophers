package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// Philosopher structure
type Philosopher struct {
	name      string
	leftFork  *Fork
	rightFork *Fork
	stopped   bool
}

func newPhilosopher(name string, left *Fork, right *Fork) *Philosopher {
	p := Philosopher{name: name, leftFork: left, rightFork: right, stopped: false}
	return &p
}

func (p *Philosopher) think() {
	fmt.Println(p.name, " is thinking")
	p.execute()
}

func (p *Philosopher) eat() {
	fmt.Println(p.name, " is eating")
	p.execute()
}

func (p *Philosopher) execute() {
	if !p.stopped {
		rand.Seed(time.Now().UnixNano())
		min := 1000
		max := 4000
		time.Sleep(time.Duration(rand.Intn((max-min+1)+min)) * time.Millisecond)
	}
}

func (p *Philosopher) pickUp() {
	p.leftFork.mux.Lock()
	p.rightFork.mux.Lock()
}

func (p *Philosopher) putDown() {
	p.leftFork.mux.Unlock()
	p.rightFork.mux.Unlock()
}

func (p *Philosopher) waiting() {
	fmt.Println(p.name, " is waiting")
	p.execute()
}

func (p *Philosopher) start(wg *sync.WaitGroup) {
	fmt.Println(p.name, " has taken a seat")
	p.execute()
	for !p.stopped {
		p.think()
		if p.stopped {
			break
		}
		p.pickUp()
		p.eat()
		p.putDown()
	}
	fmt.Println(p.name, " has finished eating")
	wg.Done()
}

func (p *Philosopher) stop() {
	p.stopped = true
}

package main

import "sync"

// Fork structure
type Fork struct {
	mux sync.Mutex
}

func newFork() *Fork {
	fork := new(Fork)
	return fork
}

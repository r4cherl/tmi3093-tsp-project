# Member 1: baselines

import random 

def random_tour(n=50, seed=0):
    rng = random.Random(seed) #random.Random(seed) creates a new random number generator that is independent of the global one. It will always produce the same sequence of numbers for the same seed.
    tour = list(range(n)) #list(range(n)) is [0, 1, 2, ..., n-1]. This is the initial tour that visits the cities in order.
    rng.shuffle(tour) #rng.shuffle(tour) randomly permutes the list in place. The result is a random tour that visits all cities exactly once.
    return tour

def nearest_neighbor_tour(D, start=0):
    n = len(D)
    unvisited = set(range(n)) - {start} #unvisited is every city except the start.
    tour = [start]
    while unvisited: #The while loop runs until no cities are left. Each round it looks at the current city cur, which is the last one in the tour.
        cur = tour[-1]
        nxt = min(unvisited, key=lambda c: (D[cur][c], c)) #min(unvisited, key=lambda c: (D[cur][c], c)) picks the unvisited c with the smallest distance. 
        tour.append(nxt)
        unvisited.remove(nxt)
    return tour
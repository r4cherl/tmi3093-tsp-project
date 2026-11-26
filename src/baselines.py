# Member 1: baselines

import random 

def random_tour(n=50, seed=0):
    rng = random.Random(seed) #random.Random(seed) creates a new random number generator that is independent of the global one. It will always produce the same sequence of numbers for the same seed.
    tour = list(range(n)) #list(range(n)) is [0, 1, 2, ..., n-1]. This is the initial tour that visits the cities in order.
    rng.shuffle(tour) #rng.shuffle(tour) randomly permutes the list in place. The result is a random tour that visits all cities exactly once.
    return tour

def nearest_neighbor_tour(D, start=0):
    n = len(D)
    unvisited = set(range(n)) - {start}
    tour = [start]
    while unvisited:
        cur = tour[-1]
        nxt = min(unvisited, key=lambda c: (D[cur][c], c)) #min(unvisited, key=lambda c: (D[cur][c], c)) finds the unvisited city that is closest to the current city. If there are ties, it chooses the one with the smallest index.
        tour.append(nxt)
        unvisited.remove(nxt)
    return tour
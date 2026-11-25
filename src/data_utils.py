# Member 1: data utilities

import numpy as np
import pandas as pd


def load_cities(path):
    return pd.read_csv(path) 

def build_distance_matrix(cities):
    xy = cities[["x_km", "y_km"]].to_numpy(dtype=float)   # table of coordinates with shape (50, 2)
    diff = xy[:, None, :] - xy[None, :, :]                # pairs every city with every other city and substract their coordinates (xi-xj, yi-yj) for all 50x50 pairs, resulting in shape (50, 50, 2)
    D = np.sqrt((diff ** 2).sum(axis=2))                  # then we square, add xsq2 + ysq2 and take the square root to get the Euclidean distance for all pairs, resulting in shape (50, 50)
    return D 

def check_matrix(D, tol=1e-12):
    #assert means "stop with an error if this is false". If everything is fine, nothing happens and the function returns True.
    assert D.shape[0] == D.shape[1], "matrix not square" #square cheeck - the matrix must be 50x50, so the number of rows must equal the number of columns
    assert np.allclose(D, D.T, atol=tol), "not symmetric" #symettric check - D.T is the matrix flipped over its diagonal. If D equals D.T, then d(i,j) = d(j,i). We use allclose instead of == because decimal numbers can differ by tiny rounding amounts.
    assert np.all(np.diag(D) == 0), "diagonal not zero" #zero diagonal check - np.diag(D) gives the diagonal entries, which are each city's distance to itself. They must all be 0.
    return True 

#The roll is what adds the return journey to the start city. Without it, the closing edge would be missing and every distance would be too short.
def tour_length(tour, D): #e.g. tour_length([0, 1, 2], D) returns the total length of the tour that visits cities 0, 1, and 2 in that order and returns to city 0.
    t = np.asarray(tour) #np.roll(t, -1) shifts the list left by one, giving [2,1,0], D[t, roll] pairs them up and picks D[0][2], D[2][1] and D[1][0]. These are the edges 0→2, 2→1 and the closing edge 1→0.
    return float(D[t, np.roll(t, -1)].sum()) #.sum() adds the three distances, and float(...) turns the result into a normal Python number.
                                            

def is_valid_tour(tour, n=50): #A tour is valid only if both are true, 1.It has exactly 50 entries (len(tour) == n). 2.When sorted, it equals [0, 1, 2, ..., 49] (sorted(tour) == list(range(n))).
    return len(tour) == n and sorted(tour) == list(range(n)) #That second check catches both problems at once. If a city is missing, the sorted list has a gap. If a city is duplicated, the sorted list has a repeat. Either way it no longer equals [0, 1, ..., 49]

def validate_tour(tour, n=50):
    if len(tour) != n: # if the tour does not have 50 entries, it stops and says so.
        return False, f"length {len(tour)} != {n}"
    seen, dup = set(), set() #it walks through the tour. If it has already seen a city, that city goes into dup.
    for c in tour:
        if c in seen:
            dup.add(c)
        seen.add(c)
    missing = set(range(n)) - seen #set(range(n)) is every city that should be there. Subtracting the cities we seen leaves the ones that never appeared.
    if dup or missing: #It returns two things: True/False and a message.
        return False, f"duplicates={sorted(dup)}, missing={sorted(missing)}"
    return True, "valid" 

def rotate_to_start(tour, start=0): #e.g for tour = [7, 3, 0, 5] and start = 0:
    tour = list(tour) #tour.index(0) finds where city 0 is. Here i = 2.
    i = tour.index(start) #tour[i:] is everything from that position onward: [0, 5], tour[:i] is everything before it: [7, 3].
    return tour[i:] + tour[:i] #Joining them gives [0, 5, 7, 3], The cities are in the same circular order, so the loop is the same. Only the starting point changed.



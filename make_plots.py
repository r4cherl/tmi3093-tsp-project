import matplotlib.pyplot as plt
from src.data_utils import load_cities, build_distance_matrix
from src.baselines import random_tour, nearest_neighbor_tour
from src.plotting import plot_cities, plot_route

cities = load_cities("data/tsp50_cities.csv")
D = build_distance_matrix(cities)

plot_cities(cities, save="results/city_map.png")

rnd = random_tour(50, seed=0)
plot_route(cities, rnd, "Random baseline (seed 0)", D,
           save="results/route_random.png")

nn = nearest_neighbor_tour(D)
plot_route(cities, nn, "Nearest-neighbor baseline (start City 1)", D,
           save="results/route_nn.png")

plt.show()
# Member 1: plotting

import matplotlib.pyplot as plt
import numpy as np

from src.data_utils import tour_length


def plot_cities(cities, save=None):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(cities["x_km"], cities["y_km"], c="steelblue", s=40, label="Cities")
    c1 = cities.iloc[0]
    ax.scatter(c1["x_km"], c1["y_km"], c="red", s=200, marker="*", #scatter draws all 50 cities as blue dots.
               label="City 1 (Central_Depot)", zorder=3) #City 1 is drawn again as a big red star, so it stands out (a brief requirement).
    for _, r in cities.iterrows():
        ax.annotate(int(r["city_id"]), (r["x_km"], r["y_km"]), #annotate writes each city ID next to its dot.
                    fontsize=7, xytext=(3, 3), textcoords="offset points")
    ax.set_title("50-City Map")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2)
    ax.grid(alpha=0.3)
    if save:
        fig.savefig(save, dpi=200, bbox_inches="tight")
    return fig

def plot_route(cities, tour, title, D, save=None):
    xy = cities[["x_km", "y_km"]].to_numpy(dtype=float)
    order = list(tour) + [tour[0]]          # appends the first city to the end. Drawing a line through this list includes the closing edge back to the start, which the brief requires.
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot(xy[order, 0], xy[order, 1], "-o", color="steelblue", ms=4, lw=1) #pick the x and y coordinates in tour order.
    ax.scatter(xy[0, 0], xy[0, 1], c="red", s=200, marker="*", zorder=3,
               label="City 1 (start)")
    ax.set_title(f"{title}\nDistance = {tour_length(tour, D):.2f} km")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.grid(alpha=0.3)
    if save:
        fig.savefig(save, dpi=200, bbox_inches="tight")
    return fig
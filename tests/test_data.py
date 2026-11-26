# Member 1: tests
import numpy as np
import pytest

from src.data_utils import (
    load_cities, build_distance_matrix, tour_length,
    is_valid_tour, validate_tour, rotate_to_start,
)
from src.baselines import random_tour, nearest_neighbor_tour


@pytest.fixture
def cities():
    return load_cities("data/tsp50_cities.csv")


@pytest.fixture
def D(cities):
    return build_distance_matrix(cities)


def test_50_distinct_ids(cities):
    assert len(cities) == 50
    assert cities["city_id"].nunique() == 50


def test_valid_tour():
    assert is_valid_tour(list(range(50)))
    assert is_valid_tour(random_tour(50, seed=3))


def test_missing_city_detected():
    t = list(range(49))
    assert not is_valid_tour(t)


def test_duplicate_city_detected():
    t = list(range(50))
    t[10] = 5
    assert not is_valid_tour(t)
    ok, msg = validate_tour(t)
    assert not ok and "duplicates=[5]" in msg and "missing=[10]" in msg

def test_closing_edge_included():
    # right triangle 3-4-5: with closing edge = 12, without it = 7
    D3 = np.array([[0, 3, 5], [3, 0, 4], [5, 4, 0]], dtype=float)
    assert tour_length([0, 1, 2], D3) == pytest.approx(12.0)


def test_distances_symmetric(D):
    assert np.allclose(D, D.T)


def test_diagonal_zero(D):
    assert np.all(np.diag(D) == 0)


def test_example_distance_from_brief(D):
    # brief: d(1,50) = sqrt(205) = 14.3178 km
    assert D[0][49] == pytest.approx(205 ** 0.5)


def test_nn_valid_and_starts_at_city1(D):
    t = nearest_neighbor_tour(D)
    assert is_valid_tour(t)
    assert t[0] == 0


def test_nn_beats_random(D):
    nn = tour_length(nearest_neighbor_tour(D), D)
    rnd = tour_length(random_tour(50, seed=0), D)
    assert nn < rnd


def test_rotation_keeps_distance(D):
    t = random_tour(50, seed=1)
    r = rotate_to_start(t, 0)
    assert r[0] == 0
    assert tour_length(r, D) == pytest.approx(tour_length(t, D))


def test_seed_reproducible():
    assert random_tour(50, seed=7) == random_tour(50, seed=7)
    assert random_tour(50, seed=7) != random_tour(50, seed=8)

    
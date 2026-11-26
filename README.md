## Project structure

- `data/tsp50_cities.csv` : supplied 50-city dataset (unchanged)
- `src/data_utils.py` : CSV loading, distance matrix, tour length, validation
- `src/baselines.py` : random tour and nearest-neighbor baselines
- `src/plotting.py` : city map and route plots
- `src/sa.py` : Simulated Annealing
- `src/ga.py` : Genetic Algorithm
- `src/experiments.py` : experiment runner
- `tests/test_data.py` : automated tests
- `results/` : plots, CSV results

## Setup

pip install -r requirements.txt

## Run tests

python -m pytest -v

## Make baseline plots

python make_plots.py

## Conventions

- A tour is a list of 0-based city indices (0 to 49). City ID = index + 1.
- Distances keep full floating-point precision. Rounding is for display only.
- Baseline results: random tour (seed 0) = 2657.61 km, nearest neighbor from City 1 = 865.57 km.

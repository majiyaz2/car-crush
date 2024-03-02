from canvas import Canvas
from racetrack import Track
from network import FirstNetwork
import os

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(0), car_image_paths)

population_count = 3
networks = [FirstNetwork() for _ in range(population_count)]

simulation_round = 1
canvas.simulate_generation(networks, simulation_round)
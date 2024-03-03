from canvas import Canvas
from racetrack import Track
from network import Network
import os

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(0), car_image_paths)

network_dimensions = 5,4,2
population_count = 3
networks = [Network(network_dimensions) for _ in range(population_count)]

simulation_round = 1
canvas.simulate_generation(networks, simulation_round)
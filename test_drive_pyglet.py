from canvas import Canvas
from racetrack import Track
from network import Network
from storage import Storage
import os

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(0), car_image_paths)

network_dimensions = 5,4,2
population_count = 20
max_generation_iterations = 10
keep_count = 4

networks = [Network(network_dimensions) for _ in range(population_count)]
storage = Storage("brain.json")
best_chromosomes = storage.load()
for c, n in zip(best_chromosomes, networks):
    n.deserialize(c)

simulation_round = 1

while simulation_round <= max_generation_iterations and canvas.is_simulating:
    print(f"=== Round: {simulation_round} ===")
    canvas.simulate_generation(networks, simulation_round)
    simulation_round +=1
    
from canvas import Canvas
from racetrack import Track
from network import Network
import os

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(0), car_image_paths)

network_dimensions = 5,4,2
population_count = 50
max_generation_iterations = 5
networks = [Network(network_dimensions) for _ in range(population_count)]

simulation_round = 1

while simulation_round <= max_generation_iterations and canvas.is_simulating:
    print(f"=== Round: {simulation_round} ===")
    canvas.simulate_generation(networks, simulation_round)
    simulation_round +=1
    if canvas.is_simulating:
        print(f"-- Average checkpoint reached: {sum (n.highest_checkpoint for n in networks) / len(networks):.2f}.")
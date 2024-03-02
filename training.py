from canvas import Canvas
import os
from racetrack import Track


car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(), car_image_paths)

canvas.simulate_generation()
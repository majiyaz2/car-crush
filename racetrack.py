from pyglet import image
import os
import itertools

class Track:
    def __init__(self):
        self.track_image = image.load(os.path.join("images", "parkinglot.png"))
        pitch = self.track_image.width*len("RGBA")
        pixels = self.track_image.get_data("RGBA", pitch)
        map = [1 if b == (75,75,75,255) else 0 for b in itertools.batched(pixels, 4)]
        self.map_matrix = [map[n:n + self.track_image.width] for n in range(0, self.track_image.width * self.track_image.height, self.track_image.width)]

    def is_road(self,x,y):
        if x < 0 or x > 960 or y < 0 or y > 540:
            return False
        return self.map_matrix[int(y)][int(x)] == 1
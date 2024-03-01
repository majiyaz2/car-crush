from pyglet.window import Window, key
import time


class Canvas(Window):
    frame_duration = 1/60
    def __init__(self):
        super().__init__()
        self.is_simulating = True
        self.width = 960
        self.height = 540
    
    def simulate_generation(self):
        last_time = time.perf_counter()
        while self.is_simulating:
            elapsed_time = time.perf_counter() - last_time
            if elapsed_time > self.frame_duration:
                last_time = time.perf_counter()
                self.dispatch_events()
                self.update(elapsed_time)
                self.draw()
    
    def update(self, delta_time):
        pass

    def draw(self):
        self.clear()
        self.flip()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.is_simulating = False
            print("Simulation aborted")

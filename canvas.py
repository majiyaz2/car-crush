from pyglet.window import Window, key
from pyglet import image 
from pyglet.graphics import Batch
from pyglet.sprite import Sprite
import time
import random
from car import Car
from hud import Hud

class Canvas(Window):
    frame_duration = 1/60

    def __init__(self, track, car_image_paths):
        super().__init__()
        self.track = track
        self.is_simulating = True
        self.width = 960
        self.height = 540
        self.background_batch = Batch()
        self.cars_batch = Batch()
        self.overlay_batch = Batch()
        self.track_image_sprite = Sprite(track.track_image, batch=self.background_batch)
        self.car_images = [image.load(c) for c in car_image_paths]
       
    
    def simulate_generation(self, networks, simulation_round):
        self.hud = Hud(simulation_round, self.overlay_batch)
        self.car_sprites = []
        for network in networks:
            self.car_sprites.append(Car(network, random.choice(self.car_images), self.cars_batch))
        self.population_total = len(self.car_sprites)  
        self.population_alive = self.population_total
        last_time = time.perf_counter()
        while self.is_simulating and self.population_alive > 0:
            elapsed_time = time.perf_counter() - last_time
            if elapsed_time > self.frame_duration:
                last_time = time.perf_counter()
                self.dispatch_events()
                self.update(elapsed_time)
                self.draw()
    
    def update(self, delta_time):
        for car_sprite in self.car_sprites:
            car_sprite.update(delta_time)
            if car_sprite.is_running:
                if not self.track.is_road(car_sprite.body.x, car_sprite.body.y):
                    car_sprite.shut_off()
        running_cars = [c for c in self.car_sprites if c.is_running]
        self.population_alive = len(running_cars)
        if self.population_alive > 0:
            self.hud.update(self.population_alive, self.population_total, running_cars[0].speed)


    def draw(self):
        self.clear()
        self.background_batch.draw()
        self.cars_batch.draw()
        self.overlay_batch.draw()
        self.flip()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.is_simulating = False
            print("Simulation aborted")
    
   
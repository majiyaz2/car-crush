from pyglet.sprite import Sprite
from pyglet.window import key
import math

class Car:
    max_speed = 6.0

    def __init__(self, image, batch):
        image.anchor_x = 25
        image.anchor_y = 25
        self.body = Sprite(image, batch=batch)
        self.body.x , self.body.y = 480, 260
        self.speed = 0.0
        self.rotation = 0.0
        self.is_running = True
    
    def update(self, delta_time, keyboard):
        render_speed = delta_time * 60
        self.speed -= 0.05

        if self.is_running:
            acceleration = 0.0
            steer_position = 0.0
            if keyboard[key.UP]:
                acceleration = 1.0
            if keyboard[key.LEFT]:
                steer_position = -1.0
            elif keyboard[key.RIGHT]:
                steer_position = 1.0

            if acceleration > 0:
                self.speed += 0.1

            if self.speed > self.max_speed:
                self.speed = self.max_speed

            self.rotation -= steer_position * self.speed * render_speed
        else:
            self.speed-= 0.05 * self.speed
        if self.speed < 0:
            self.speed = 0.0

        self.body.rotation = -self.rotation
        self.body.x += self.speed * render_speed * math.cos(math.radians(self.rotation))
        self.body.y += self.speed * render_speed * math.sin(math.radians(self.rotation))

    def shut_off(self):
        self.is_running = False

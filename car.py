from pyglet.sprite import Sprite

class Car:
    def __init__(self, image, batch):
        image.anchor_x = 25
        image.anchor_y = 25
        self.body = Sprite(image, batch=batch)
        self.body.x , self.body.y = 480, 260
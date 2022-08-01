import random
import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Plane(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    def update(self):

class Cloud(arcade.Sprite):

    def __init__(self, filename, ,sprite_scaling, x, y, speed):
        super().__init__(filename, sprite_scaling)
        self.x = 0
        self.y = 0
        speed = random.randint(0,10)

    def update(self, speed):
        self.x += self.speed

import random
import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Plane(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    def update(self):
        
